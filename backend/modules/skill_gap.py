
import pandas as pd

from modules.data_loader import SKILL_COLS, TOOL_COLS
from career_taxonomy import CAREER_TAXONOMY
from career_knowledge import get_career_knowledge


def _dataset_pattern_skills(df: pd.DataFrame, domain: str, role: str = None) -> dict:
    """Average skill levels of profiles in this project's synthetic dataset."""
    pool = df[df["domain"] == domain]
    if role:
        role_pool = pool[pool["role"] == role]
        if not role_pool.empty:
            pool = role_pool
    if pool.empty:
        pool = df
    return {skill: round(pool[skill].mean(), 1) for skill in SKILL_COLS}


def _authored_required_skills(domain: str, role: str, specialization: str = None) -> dict:
    """
    Hand-authored skill expectations from career_taxonomy.py, where they
    exist. Some roles author these at the specialization level (e.g.
    Software Developer's "Mobile Development"), others at the role
    level (e.g. Data Scientist) -- both patterns are checked. Returns
    {} if nothing has been authored for this role yet.
    """
    role_data = CAREER_TAXONOMY.get(domain, {}).get("roles", {}).get(role, {})

    if specialization:
        for spec, sdata in role_data.get("specializations", {}).items():
            if "sub_specializations" in sdata:
                for sub in sdata["sub_specializations"]:
                    if f"{spec} — {sub}" == specialization and "skills_required" in sdata:
                        return sdata["skills_required"]
            elif spec == specialization and "skills_required" in sdata:
                return sdata["skills_required"]

    return role_data.get("skills_required", {})


def _required_tools(domain: str, role: str, specialization: str) -> dict:
    """Tool/technology requirements for a specialization -- these come from
    the authored career_taxonomy (they don't exist as a trainable signal;
    see ml_models.py's design note on Level 3/4)."""
    role_data = CAREER_TAXONOMY.get(domain, {}).get("roles", {}).get(role, {})
    for spec, sdata in role_data.get("specializations", {}).items():
        if "sub_specializations" in sdata:
            for sub, subdata in sdata["sub_specializations"].items():
                if f"{spec} — {sub}" == specialization:
                    return subdata.get("tools_required", {})
        elif spec == specialization:
            return sdata.get("tools_required", {})
    return {}


def _tool_experience_label(current: int) -> str:
    """Honest framing for tool self-assessment -- never implies a tool
    was measured if the student was simply never asked yet."""
    if current <= 0:
        return "Not yet assessed"
    if current <= 2:
        return "Tried"
    return "Comfortable"


def _priority_score(skill_entry: dict, critical_skills: list, skill_importance: dict = None) -> float:
    """
    Gap size always drives the base score. Criticality is layered on top so a
    smaller gap in a career-critical skill can still outrank a larger gap in
    something this role barely needs -- an authored `skill_importance` float
    (0.0-1.0, see career_knowledge.py) is preferred when available since it
    expresses real, role-specific weighting; the `critical_skills` ORDER is
    the fallback for roles that only have the simpler ranked list.
    """
    gap = skill_entry["gap"]
    if gap <= 0:
        return -1.0
    skill_importance = skill_importance or {}
    skill = skill_entry["skill"]
    if skill in skill_importance:
        criticality_weight = skill_importance[skill] * 10
    elif skill in critical_skills:
        rank = critical_skills.index(skill)
        criticality_weight = len(critical_skills) - rank
    else:
        criticality_weight = 0
    return gap * 10 + criticality_weight


def bucket_skills(skills: list, critical_skills: list = None, skill_importance: dict = None) -> dict:
    """
    Split skills into three groups instead of one flat list of equally-
    weighted gaps: skills already at/above target ("strengths"), the
    2-4 gaps that matter most right now ("focus_first" -- ranked by
    gap size AND how career-critical the skill is for this specific
    role, not gap size alone), and the rest ("helpful_later").
    """
    critical_skills = critical_skills or []
    strengths = [s for s in skills if s["gap"] <= 0]
    gaps = [s for s in skills if s["gap"] > 0]
    ranked = sorted(gaps, key=lambda s: _priority_score(s, critical_skills, skill_importance), reverse=True)
    return {
        "strengths": strengths,
        "focus_first": ranked[:4],
        "helpful_later": ranked[4:],
    }


def calculate_skill_gap(student: dict, df: pd.DataFrame, domain: str,
                         role: str = None, specialization: str = None) -> dict:
    """
    Build the full skill-gap picture at whatever depth the student has
    drilled into: Domain-level general skills always, Role-level
    refines the target, Specialization-level adds tool/technology gaps.

    Skill targets prefer a hand-authored career_profile figure; any
    skill without one falls back to the dataset_pattern average. Each
    skill entry reports which source backed its target.
    """
    dataset_pattern = _dataset_pattern_skills(df, domain, role)
    authored = _authored_required_skills(domain, role, specialization)
    knowledge = get_career_knowledge(domain, role, specialization) if role else {}
    critical_skills = knowledge.get("critical_skills", [])
    skill_importance = knowledge.get("skill_importance", {})

    skills = []
    met, gap_count = 0, 0
    for skill in SKILL_COLS:
        current = int(student.get(skill, 3))
        if skill in authored:
            req = authored[skill]
            source = "career_profile"
        else:
            req = dataset_pattern[skill]
            source = "dataset_pattern"
        gap = round(req - current, 1)
        status = "Met" if gap <= 0 else ("Minor Gap" if gap <= 1 else "Needs Improvement")
        if gap <= 0:
            met += 1
        else:
            gap_count += 1
        skills.append({"skill": skill, "label": skill.replace("_", " ").title(),
                        "current": current, "required": req, "gap": max(gap, 0),
                        "status": status, "source": source})

    result = {
        "domain": domain, "role": role, "specialization": specialization,
        "skills": skills, "met_count": met, "gap_count": gap_count,
        "tools": [],
        **bucket_skills(skills, critical_skills, skill_importance),
    }

    if specialization:
        tool_reqs = _required_tools(domain, role, specialization)
        tools = []
        for tool, req_level in tool_reqs.items():
            current = int(student.get(tool, 0))
            gap = max(req_level - current, 0)
            tools.append({
                "tool": tool, "label": tool.replace("_", " ").title(),
                "current": current, "required": req_level, "gap": gap,
                "status": "Met" if gap <= 0 else "Building",
                "experience": _tool_experience_label(current),
            })
        result["tools"] = tools

    return result
