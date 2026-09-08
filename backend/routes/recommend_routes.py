# =============================================================
# backend/routes/recommend_routes.py
# =============================================================
# PURPOSE:
#   The hierarchical recommendation API: Domain -> Role ->
#   Specialization, plus skill-gap and roadmap for whichever depth
#   the student has drilled into.
# =============================================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
import numpy as np

from modules.ml_models import train_all_models, recommend_specializations
from modules.data_loader import (
    SKILL_COLS, SCORE_COLS, PREFERENCE_COLS, DOMAIN_FEATURE_COLS,
    ROLE_BASE_FEATURE_COLS, INTEREST_TAXONOMY, INTEREST_TAGS,
)
from modules.skill_gap import calculate_skill_gap
from modules.roadmap import generate_roadmap
from modules.hybrid_scoring import score_domain, score_role, select_top, generate_explanation
from career_taxonomy import CAREER_TAXONOMY
from career_knowledge import get_career_knowledge, is_regulated
from interest_taxonomy import role_interest_tags

router = APIRouter(prefix="/api/recommend", tags=["Recommendation"])

_models_cache = None


def get_models():
    global _models_cache
    if _models_cache is None:
        _models_cache = train_all_models()
    return _models_cache


class StudentProfile(BaseModel):
    name: Optional[str] = None   # identity isn't needed for the recommendation itself
    education_level: str = "Bachelor"

    communication: int = 3
    problem_solving: int = 3
    creativity: int = 3
    analytical_thinking: int = 3
    leadership: int = 3
    teamwork: int = 3
    technical_ability: int = 3
    research: int = 3
    organization: int = 3
    presentation: int = 3

    math_score: float = 70
    science_score: float = 70
    english_score: float = 70
    computer_score: float = 70
    business_score: float = 70
    arts_score: float = 70

    pref_people_vs_independent: int = 3
    pref_creative_vs_analytical: int = 3
    pref_indoor_vs_outdoor: int = 3
    pref_structured_vs_flexible: int = 3
    pref_handson_vs_theoretical: int = 3
    pref_tech_vs_people: int = 3

    interests: Dict[str, int] = {}   # { "Programming": 2, "Football": 1, ... }
    curious_interests: List[str] = []  # tags marked "curious to explore" -- light signal only
    tools: Dict[str, int] = {}       # { "git": 2, "python": 1, ... } -- self-assessed, optional
    na_subjects: List[str] = []      # score columns marked "not applicable to my stream"


def flatten_profile(profile: StudentProfile) -> dict:
    """Turn the nested profile into the flat dict every module expects."""
    student = profile.model_dump()
    interests = student.pop("interests")
    tools = student.pop("tools")

    for tag in INTEREST_TAGS:
        student[tag] = int(interests.get(tag, 0))
    for domain, tags in INTEREST_TAXONOMY.items():
        student[f"interest_agg__{domain}"] = sum(student[t] for t in tags)

    # Tool columns default to 0 (no exposure) unless self-reported
    from modules.data_loader import TOOL_COLS
    for tool in TOOL_COLS:
        student[tool] = int(tools.get(tool, 0))

    return student


class DomainRequest(BaseModel):
    student: StudentProfile
    recommendation_count: int = 3   # user-chosen MAXIMUM, not a requirement -- validated below


class RoleRequest(BaseModel):
    student: StudentProfile
    domain: str


class SpecializationRequest(BaseModel):
    student: StudentProfile
    domain: str
    role: str


class GapRequest(BaseModel):
    student: StudentProfile
    domain: str
    role: Optional[str] = None
    specialization: Optional[str] = None


# =============================================================
# LEVEL 1 — Domain recommendation
# =============================================================
@router.post("/domain")
def recommend_domain(request: DomainRequest):
    try:
        models = get_models()
        student = flatten_profile(request.student)
        na_subjects = set(request.student.na_subjects)
        curious_tags = set(request.student.curious_interests)

        dm = models["domain"]

        # Model Signal is the whole-profile RF's own probability -- NOT
        # blended with a second interest-only RF. See the "no double
        # counting" note at the top of modules/hybrid_scoring.py for why:
        # that blend used to inject interest signal a second time, on
        # top of the interest features already inside this RF's own
        # 35 inputs. Interest gets its full, transparent say through
        # the explicit Interest Fit component instead.
        X_full = np.array([student[c] for c in dm["feature_cols"]]).reshape(1, -1)
        probs = dm["model"].predict_proba(dm["scaler"].transform(X_full))[0]

        # Never trust an arbitrary frontend value for how many results
        # to return -- only 1/2/3 are valid, anything else safely defaults.
        requested_count = request.recommendation_count if request.recommendation_count in (1, 2, 3) else 3

        scored = [
            score_domain(student, name, float(p) * 100, models["df"], na_subjects, curious_tags)
            for name, p in zip(dm["domain_names"], probs)
        ]
        results, meta = select_top(scored, requested_count=requested_count)

        for r in results:
            r["explanation"] = generate_explanation(
                student, r["domain"], r["breakdown"], r["contradiction"],
                INTEREST_TAXONOMY.get(r["domain"], []))
            domain_roles = list(CAREER_TAXONOMY.get(r["domain"], {}).get("roles", {}).keys())
            r["roles_in_domain"] = domain_roles[:5]

        return {"student_name": request.student.name, "recommendations": results, **meta}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================
# LEVEL 2 — Role recommendation within a chosen domain
# =============================================================
@router.post("/role")
def recommend_role(request: RoleRequest):
    try:
        models = get_models()
        student = flatten_profile(request.student)
        curious_tags = set(request.student.curious_interests)

        role_model = models["roles"].get(request.domain)
        if not role_model or not role_model.get("trained"):
            # Fall back: rank roles by frequency among profiles in this dataset
            df = models["df"]
            pool = df[df["domain"] == request.domain]
            roles = pool["role"].unique().tolist()
            results = [{"role": r, "alignment_pct": round(100 / len(roles), 1)} for r in roles]
            return {"domain": request.domain, "recommendations": results[:3],
                    "note": "Not enough data to train a dedicated role model for this domain yet."}

        feature_cols = role_model["feature_cols"]
        X = np.array([student.get(c, 0) for c in feature_cols]).reshape(1, -1)
        X_scaled = role_model["scaler"].transform(X)
        probs = role_model["model"].predict_proba(X_scaled)[0]

        # Same hybrid approach as domain-level, and for the same reason:
        # raw role-model probability barely uses the specific interest
        # tags a student picked (a real user report -- selecting "Football"
        # recommended Fitness Trainer over Athlete -- traced this exactly:
        # Football didn't crack the role model's top 15 features, and the
        # synthetic training data doesn't tie individual tags to specific
        # roles within a domain). score_role() adds an explicit Interest
        # Fit sourced from interest_taxonomy.ROLE_INTEREST_TAGS, the
        # hand-curated "which tags actually relate to this role" mapping.
        scored = [
            score_role(student, request.domain, name, float(p) * 100, models["df"], curious_tags)
            for name, p in zip(role_model["role_names"], probs)
        ]
        results, _meta = select_top(scored, requested_count=3)

        for r in results:
            r["explanation"] = generate_explanation(
                student, r["role"], r["breakdown"], r["contradiction"],
                role_interest_tags(request.domain, r["role"]))

        return {"domain": request.domain, "recommendations": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================
# LEVEL 3 — Specialization (similarity-based, honestly labeled)
# =============================================================
@router.post("/specialization")
def recommend_specialization(request: SpecializationRequest):
    try:
        models = get_models()
        student = flatten_profile(request.student)

        vec = np.array([student.get(c, 0) for c in ROLE_BASE_FEATURE_COLS], dtype=float)
        results = recommend_specializations(vec, request.domain, request.role, models["df"])

        return {
            "domain": request.domain, "role": request.role,
            "specializations": results,
            "method_note": ("Profile-based specialization relevance -- ranked by similarity to "
                             "other profiles in this project's dataset who chose this role, not a "
                             "trained prediction. There isn't honest ground truth to predict "
                             "specialization choice from academic profile alone."),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================
# SKILL GAP
# =============================================================
@router.post("/skill-gap")
def skill_gap(request: GapRequest):
    try:
        models = get_models()
        student = flatten_profile(request.student)
        result = calculate_skill_gap(student, models["df"], request.domain,
                                      request.role, request.specialization)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================
# ROADMAP
# =============================================================
@router.post("/roadmap")
def roadmap(request: GapRequest):
    try:
        models = get_models()
        student = flatten_profile(request.student)
        gap_result = calculate_skill_gap(student, models["df"], request.domain,
                                          request.role, request.specialization)
        return generate_roadmap(gap_result, request.student.education_level)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# =============================================================
# ROLE DETAIL — curated career guidance for a specific role
# =============================================================
@router.get("/role-detail")
def role_detail(domain: str, role: str, specialization: Optional[str] = None):
    try:
        info = get_career_knowledge(domain, role, specialization)
        role_data = CAREER_TAXONOMY.get(domain, {}).get("roles", {}).get(role, {})
        specializations = []
        for spec, sdata in role_data.get("specializations", {}).items():
            if "sub_specializations" in sdata:
                specializations.extend(f"{spec} — {sub}" for sub in sdata["sub_specializations"])
            else:
                specializations.append(spec)

        return {
            "domain": domain, "role": role, "specialization": specialization,
            "has_curated_content": bool(info),
            "regulated": is_regulated(domain, role),
            "description": info.get("description"),
            "typical_activities": info.get("typical_activities", []),
            "useful_strengths": info.get("useful_strengths", []),
            "useful_academic_areas": info.get("useful_academic_areas", []),
            "work_preferences": info.get("work_preferences", {}),
            "work_settings": info.get("work_settings", []),
            "tools_context": info.get("tools_context", []),
            "field_methods": info.get("field_methods", []),
            "project_ideas": info.get("project_ideas", []),
            "education_preparation": info.get("education_preparation"),
            "possible_directions": info.get("possible_directions", []),
            "specializations": specializations,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
