# =============================================================
# backend/modules/hybrid_scoring.py
# =============================================================
# PURPOSE:
#   Turn a domain's ML signal into a defensible "Alignment Score" --
#   not a probability of success, a transparent blend of five things
#   that all plausibly matter to whether a career direction is a
#   good fit. See the formula/component notes below.
#
#   These thresholds (Strong/Possible/Weak, the interest/skill/
#   academic cutoffs used in contradiction handling) are practical,
#   hand-chosen UX cutoffs for THIS tool, tuned against a handful of
#   test profiles -- they are not statistically validated against
#   real-world outcome data, and the UI must not imply otherwise.
# =============================================================

import pandas as pd

from modules.data_loader import SKILL_COLS, SCORE_COLS, PREFERENCE_COLS, INTEREST_TAXONOMY
from interest_taxonomy import role_interest_tags

# --- component weights (sum to 1.0) -----------------------------------
# WHY these five, and why this split (see also the "no double counting"
# note below): Model Signal is what a Random Forest -- trained on the
# student's skills, academics, preferences, and interest totals --
# thinks, given population-level patterns in the dataset. But RF
# probability has no concept of "the student explicitly said no" --
# it just reflects resemblance to students who ended up in a domain.
# Interest Fit is the one component that exists specifically to let a
# student's STATED interest override a merely statistical resemblance,
# which is why it carries the single largest weight.
MODEL_WEIGHT = 0.30
INTEREST_WEIGHT = 0.35
PREFERENCE_WEIGHT = 0.15
SKILL_WEIGHT = 0.15
ACADEMIC_WEIGHT = 0.05

# NOTE ON DOUBLE-COUNTING INTEREST (audited): earlier this component
# blended TWO Random Forests into "Model Signal" -- a whole-profile RF
# and a second RF trained ONLY on interest totals, weighted 55/45.
# That second model existed only to inject interest signal a SECOND
# time, on top of the interest already sitting inside the whole-profile
# RF's own 35 input features -- an intentional double-boost that only
# applied to interest and not symmetrically to skills/academics/prefs.
# Model Signal is now ONLY the whole-profile RF's own probability.
# It still "sees" interest (13 of its 35 input features are the
# interest_agg__<domain> columns), the same way it sees skills,
# academics, and preferences -- each of those ALSO gets its own
# explicit Fit term below, exactly like interest does. So every
# component is treated the same way: one diffuse mention inside the
# RF's feature set, plus one explicit, transparent Fit term. Per this
# project's own earlier feature-importance measurement, interest_agg
# columns don't even crack the RF's top 10 features -- so the residual
# interest signal folded into Model Signal's 30% weight is a small
# fraction of that 30%, not a hidden second 30-45%. The EXPLICIT 35%
# Interest Fit term below is what actually and transparently carries
# the weight of "did the student say they want this."

# --- Interest Fit: strength of top tags + breadth, not raw tag count --
# Reward strength of the tags actually picked, capped so clicking MORE
# tags beyond a genuine, committed set (3, matching the wizard's own
# 3-tag minimum) can't inflate the score further -- and weight breadth
# only lightly, so a pile of many WEAK tags can't out-score one or two
# genuinely strong ones.
INTEREST_TOP_K = 3
INTEREST_STRENGTH_WEIGHT = 0.70
INTEREST_BREADTH_WEIGHT = 0.30
MAX_TAG_STRENGTH = 3.0

# "Curious to explore" tags register light interest -- clearly less
# than a genuine cycled-interest tag, and capped low enough that
# curiosity ALONE can never cross LOW_INTEREST_THRESHOLD below and
# read as "expressed interest." It can only nudge a domain that
# already has some real signal, or soften (not erase) a zero-interest
# read.
CURIOUS_TAG_VALUE = 4.0
CURIOUS_TAG_CAP = 8.0

# Below this, a domain is treated as "no expressed interest"
LOW_INTEREST_THRESHOLD = 15.0

# What "skills/academics strongly contradict the low interest" means
STRONG_TRAITS_SKILL_MIN = 75.0
STRONG_TRAITS_ACADEMIC_MIN = 60.0

# --- contradiction handling: fixed-point deductions, not a multiplier -
# A MULTIPLIER is mathematically broken here: with zero interest, the
# highest a domain could ever score (interest term contributes 0) is
# the other four components at 100% each, i.e. 65 points (1 -
# INTEREST_WEIGHT). A 0.75x multiplier caps that theoretical max at
# 48.75 -- which can NEVER reach the 50% "Possible" threshold, no
# matter how strong the student's skills/academics/preferences/model
# signal are. That defeats the entire point of a "soft" contradiction
# path. Instead: recompute what the domain would score with the
# interest term set aside and the remaining four weights renormalized
# to fill the full 100%, then subtract a fixed point deduction -- large
# enough to matter, small enough that a genuinely strong non-interest
# profile can still land in "Possible."
CONTRADICTION_DEDUCTION = 10.0   # strong skills/academics despite low interest
SUPPRESSION_DEDUCTION = 25.0     # low interest AND nothing else strongly points here

STRONG_MATCH_THRESHOLD = 70.0
POSSIBLE_MATCH_THRESHOLD = 50.0

LABELS = {
    "interest": "your stated interests",
    "skill": "your current skills",
    "preference": "how you like to work",
    "academic": "your academic strengths",
}


def _domain_pool_means(df: pd.DataFrame, domain: str, cols: list) -> dict:
    pool = df[df["domain"] == domain]
    if pool.empty:
        pool = df
    return {c: float(pool[c].mean()) for c in cols}


def compute_interest_fit(student: dict, tags: list, curious_tags: set = None) -> float:
    """
    Strength of the top (up to 3) tags picked from `tags`, plus a
    lighter breadth component -- NOT a raw sum of every tag clicked.
    A single strength-3 tag scores well; three strength-3 tags score
    at the cap; a pile of many strength-1 tags scores clearly lower
    than either, since strength (not tag count) is 70% of this score.
    Picking a 4th, 5th, 6th strong tag beyond the top 3 adds nothing
    further -- there's no way to keep inflating this by clicking more.

    `tags` is whatever tag list is relevant to the thing being scored --
    a full domain's tags for score_domain(), or just the handful of
    tags that actually relate to one specific role for score_role().

    Tags marked "curious to explore" (not a genuine cycled interest)
    add a small, capped bonus on top -- enough to nudge a result the
    student is mildly curious about, never enough by itself to read
    as "expressed interest" (see CURIOUS_TAG_CAP vs LOW_INTEREST_THRESHOLD).
    """
    selected = sorted((int(student.get(t, 0)) for t in tags if int(student.get(t, 0)) > 0), reverse=True)

    if selected:
        top_k = selected[:INTEREST_TOP_K]
        strength_component = (sum(top_k) / len(top_k)) / MAX_TAG_STRENGTH * 100
        breadth_component = min(1.0, len(selected) / INTEREST_TOP_K) * 100
        fit = INTEREST_STRENGTH_WEIGHT * strength_component + INTEREST_BREADTH_WEIGHT * breadth_component
    else:
        fit = 0.0

    curious_tags = curious_tags or set()
    curious_here = [t for t in tags if t in curious_tags]
    if curious_here and fit < 100:
        bonus = min(CURIOUS_TAG_CAP, len(curious_here) * CURIOUS_TAG_VALUE)
        fit = min(100.0, fit + bonus)

    return round(fit, 1)


def compute_skill_fit(student: dict, avg_skills: dict) -> float:
    components = []
    for skill, avg in avg_skills.items():
        current = student.get(skill, 3)
        components.append(1.0 if avg <= 0 else min(1.0, current / avg))
    return round(sum(components) / len(components) * 100, 1)


def _subject_distinctiveness(df: pd.DataFrame, domain: str, cols: list) -> dict:
    """
    How unusual THIS domain's average is for each subject, relative to
    the spread across all domains -- used to weight Academic Fit so a
    subject where every domain wants roughly the same level doesn't
    carry equal say to one that actually distinguishes this domain.

    WHY THIS EXISTS: auditing Academic Fit found Social Work & Community
    and Sports & Fitness both scoring ~98-99% for an average student.
    That's not a formula bug -- both domains genuinely have similar,
    modestly-low authored academic baselines across all 6 subjects in
    this dataset (neither field's synthetic profile leans hard on any
    one subject), so an unweighted mean-of-6-ratios legitimately
    converges for them. A flat mean also gives a subject where ALL
    domains cluster near the same average (little real information)
    equal say to a subject like computer_score, where domains range
    from ~55 to ~92 (a lot of real information). Weighting by
    distinctiveness fixes the second problem without touching the
    underlying dataset or retraining anything -- domains that are
    genuinely similar can still end up with similar Academic Fit for a
    similar student; domains with real academic distinctiveness now
    get to show it.
    """
    weights = {}
    for c in cols:
        domain_avg = float(df[df["domain"] == domain][c].mean())
        overall_mean = float(df[c].mean())
        overall_std = max(float(df[c].std()), 1e-6)
        z = abs(domain_avg - overall_mean) / overall_std
        weights[c] = max(0.25, min(2.0, z))  # floor so no subject is fully zeroed, cap to limit any one subject dominating
    return weights


def compute_academic_fit(student: dict, avg_scores: dict, na_subjects: set = None,
                          subject_weights: dict = None) -> float:
    """
    Subjects the student marked N/A (not applicable to their stream)
    are excluded entirely, not defaulted to any value -- they must
    neither raise nor lower Academic Fit. If every subject is N/A,
    there's nothing to judge, so this returns a neutral 100 rather
    than penalizing or crashing.

    `subject_weights` (from _subject_distinctiveness) weight each
    subject's contribution by how much it actually distinguishes this
    domain from others -- see that function's note for why.
    """
    na_subjects = na_subjects or set()
    subject_weights = subject_weights or {}
    weighted_sum, weight_total = 0.0, 0.0
    for score, avg in avg_scores.items():
        if score in na_subjects:
            continue
        current = student.get(score, 0)
        ratio = 1.0 if avg <= 0 else min(1.0, current / avg)
        w = subject_weights.get(score, 1.0)
        weighted_sum += ratio * w
        weight_total += w
    if weight_total <= 0:
        return 100.0
    return round(weighted_sum / weight_total * 100, 1)


def compute_preference_fit(student: dict, avg_prefs: dict) -> float:
    components = []
    for pref, avg in avg_prefs.items():
        current = student.get(pref, 3)
        components.append(max(0.0, 1 - abs(current - avg) / 4))
    return round(sum(components) / len(components) * 100, 1)


def _blend_and_score(model_signal_pct: float, interest_fit: float, skill_fit: float,
                      academic_fit: float, preference_fit: float) -> tuple:
    """
    The shared weighted-blend + contradiction-handling core used by both
    score_domain() and score_role() -- same formula, same thresholds,
    applied at whichever level (domain or role) the caller is scoring.
    Returns (overall, tier, contradiction).
    """
    raw = (MODEL_WEIGHT * model_signal_pct + INTEREST_WEIGHT * interest_fit +
           PREFERENCE_WEIGHT * preference_fit + SKILL_WEIGHT * skill_fit +
           ACADEMIC_WEIGHT * academic_fit)

    contradiction = False
    if interest_fit < LOW_INTEREST_THRESHOLD:
        # Set interest aside and renormalize the remaining four weights
        # to fill 100% -- see the design note above for why a plain
        # multiplier on `raw` can't work here.
        remaining_weight = MODEL_WEIGHT + PREFERENCE_WEIGHT + SKILL_WEIGHT + ACADEMIC_WEIGHT
        raw_without_interest = (
            MODEL_WEIGHT * model_signal_pct + PREFERENCE_WEIGHT * preference_fit +
            SKILL_WEIGHT * skill_fit + ACADEMIC_WEIGHT * academic_fit
        ) / remaining_weight

        strong_traits = skill_fit >= STRONG_TRAITS_SKILL_MIN and academic_fit >= STRONG_TRAITS_ACADEMIC_MIN
        if strong_traits:
            overall = raw_without_interest - CONTRADICTION_DEDUCTION
            contradiction = True
        else:
            overall = raw_without_interest - SUPPRESSION_DEDUCTION
        overall = max(0.0, overall)
    else:
        overall = raw

    overall = round(min(100.0, overall), 1)

    if overall >= STRONG_MATCH_THRESHOLD:
        tier = "Strong"
    elif overall >= POSSIBLE_MATCH_THRESHOLD:
        tier = "Possible"
    else:
        tier = "Weak"

    return overall, tier, contradiction


def score_domain(student: dict, domain: str, model_signal_pct: float, df: pd.DataFrame,
                  na_subjects: set = None, curious_tags: set = None) -> dict:
    avg_skills = _domain_pool_means(df, domain, SKILL_COLS)
    avg_scores = _domain_pool_means(df, domain, SCORE_COLS)
    avg_prefs = _domain_pool_means(df, domain, PREFERENCE_COLS)
    subject_weights = _subject_distinctiveness(df, domain, SCORE_COLS)

    interest_fit = compute_interest_fit(student, INTEREST_TAXONOMY.get(domain, []), curious_tags)
    skill_fit = compute_skill_fit(student, avg_skills)
    academic_fit = compute_academic_fit(student, avg_scores, na_subjects, subject_weights)
    preference_fit = compute_preference_fit(student, avg_prefs)

    overall, tier, contradiction = _blend_and_score(
        model_signal_pct, interest_fit, skill_fit, academic_fit, preference_fit)

    return {
        "domain": domain,
        "alignment_pct": overall,
        "confidence": tier,
        "contradiction": contradiction,
        "breakdown": {
            "model_signal": round(model_signal_pct, 1),
            "interest_fit": interest_fit,
            "skill_fit": skill_fit,
            "preference_fit": preference_fit,
            "academic_fit": academic_fit,
        },
    }


def _role_pool_means(df: pd.DataFrame, domain: str, role: str, cols: list) -> dict:
    pool = df[(df["domain"] == domain) & (df["role"] == role)]
    if pool.empty:
        pool = df[df["domain"] == domain]
    if pool.empty:
        pool = df
    return {c: float(pool[c].mean()) for c in cols}


def score_role(student: dict, domain: str, role: str, model_signal_pct: float, df: pd.DataFrame,
               curious_tags: set = None) -> dict:
    """
    Same hybrid formula as score_domain(), applied one level down. The
    critical difference is WHERE the interest signal comes from: not
    the domain's full tag list (which can't distinguish between roles
    inside the same domain -- e.g. Football says nothing about Athlete
    vs Fitness Trainer if you count every Sports & Fitness tag equally),
    but interest_taxonomy.ROLE_INTEREST_TAGS -- the hand-curated subset
    of tags that actually relate to THIS specific role. See that file's
    design note for the real bug this fixes (a real user report: picking
    "Football" recommended Fitness Trainer over Athlete, because the
    role-level Random Forest barely used the tag at all, and the
    synthetic training data itself doesn't tie individual tags to
    specific roles within a domain).

    Skill/Academic/Preference Fit are compared against the ROLE's own
    average profile (students in this domain AND role), not the whole
    domain's -- a sharper, more specific comparison than domain-level.
    """
    avg_skills = _role_pool_means(df, domain, role, SKILL_COLS)
    avg_scores = _role_pool_means(df, domain, role, SCORE_COLS)
    avg_prefs = _role_pool_means(df, domain, role, PREFERENCE_COLS)

    interest_fit = compute_interest_fit(student, role_interest_tags(domain, role), curious_tags)
    skill_fit = compute_skill_fit(student, avg_skills)
    academic_fit = compute_academic_fit(student, avg_scores)
    preference_fit = compute_preference_fit(student, avg_prefs)

    overall, tier, contradiction = _blend_and_score(
        model_signal_pct, interest_fit, skill_fit, academic_fit, preference_fit)

    return {
        "role": role,
        "alignment_pct": overall,
        "confidence": tier,
        "contradiction": contradiction,
        "breakdown": {
            "model_signal": round(model_signal_pct, 1),
            "interest_fit": interest_fit,
            "skill_fit": skill_fit,
            "preference_fit": preference_fit,
            "academic_fit": academic_fit,
        },
    }


def select_top(scored: list, requested_count: int = 3,
               possible_threshold: float = POSSIBLE_MATCH_THRESHOLD) -> tuple:
    """
    Sort by alignment, keep only Strong/Possible matches, then cap at
    the user's REQUESTED count -- never pad up to it. `requested_count`
    is a ceiling, not a target: if only 1 or 2 domains clear the
    threshold, that's all that's returned, regardless of what was
    asked for. Falls back to the single best result (still labeled
    Weak) only so the UI is never left completely blank.

    Returns (results, meta) where meta reports what actually happened
    so the frontend can explain it honestly (e.g. "you asked for 3,
    only 2 passed the threshold").
    """
    ranked = sorted(scored, key=lambda r: r["alignment_pct"], reverse=True)
    qualified = [r for r in ranked if r["alignment_pct"] >= possible_threshold]

    fallback = False
    if qualified:
        results = qualified[:requested_count]
    elif ranked:
        results = ranked[:1]
        fallback = True
    else:
        results = []

    meta = {
        "requested_count": requested_count,
        "qualified_count": len(qualified),
        "returned_count": len(results),
        "fallback": fallback,
    }
    return results, meta


def generate_explanation(student: dict, label: str, breakdown: dict, contradiction: bool,
                          tags: list = None) -> list:
    """
    Plain-language explanation built from this student's actual breakdown
    numbers. `tags` is whichever tag list is relevant to what's being
    explained (a domain's full tags, or one role's curated subset) --
    defaults to [] so a caller with no tag list at all still gets the
    breakdown-based sentence, just without the "interests you selected"
    line.
    """
    tags = tags or []
    reasons = []
    ranked = sorted(
        [("interest", breakdown["interest_fit"]), ("skill", breakdown["skill_fit"]),
         ("preference", breakdown["preference_fit"]), ("academic", breakdown["academic_fit"])],
        key=lambda x: x[1], reverse=True,
    )
    top_label, top_val = ranked[0]
    second_label, second_val = ranked[1]

    if contradiction:
        reasons.append(
            f"Your skills and academics line up strongly with {label}, but your stated interest "
            f"in this area is low right now — this ranking is driven mainly by aptitude, not by "
            f"what you said you want."
        )
    elif top_val >= 50:
        reasons.append(
            f"This ranked highly mainly because of {LABELS[top_label]} ({round(top_val)}%), "
            f"with {LABELS[second_label]} also contributing ({round(second_val)}%)."
        )
    else:
        reasons.append("Your overall profile is closest to this option among those considered.")

    selected = [t for t in tags if student.get(t, 0) > 0]
    if selected:
        tag_list = ', '.join(selected[:3]) + ('...' if len(selected) > 3 else '')
        reasons.append(f"Interests you selected here: {tag_list}")
    elif tags and breakdown["interest_fit"] < LOW_INTEREST_THRESHOLD:
        reasons.append("You didn't select any interests in this area.")

    return reasons
