
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data"))
from career_knowledge import get_career_knowledge, is_regulated  # noqa: E402

ROADMAP_LABEL = "Suggested Development Roadmap"
ROADMAP_DISCLAIMER = "This is a starting direction, not a guarantee or fixed career plan."
REGULATED_NOTICE = (
    "This is a regulated, licensed field. Exploring and preparing for it is useful now, "
    "but only an accredited program, formal degree/diploma, and (where applicable) a "
    "licensing exam and supervised clinical training can actually qualify someone to "
    "practice. Nothing in this roadmap substitutes for that."
)

# --- fallback content for roles without an authored career_knowledge entry ---

DOMAIN_CONTEXT = {
    "Technology & Computing":   {"noun": "coding/technical", "drill": "structured programming challenges (LeetCode, HackerRank)"},
    "Finance & Business":       {"noun": "business/financial", "drill": "real company case studies (the Harvard Business case method is free to sample online)"},
    "Design & Creative":        {"noun": "design", "drill": "critiquing and redesigning a real interface, poster, or piece of visual work"},
    "Public Service & Law":     {"noun": "policy/legal", "drill": "mock case arguments or structured policy-brief writing"},
    "Education":                {"noun": "classroom", "drill": "practice-teaching a small group and reviewing what worked"},
    "Healthcare & Medicine":    {"noun": "clinical", "drill": "real case studies and differential-diagnosis style reasoning"},
    "Engineering":              {"noun": "technical design", "drill": "worked examples from real engineering design problems"},
    "Media & Communication":   {"noun": "storytelling/content", "drill": "producing a short piece of content and getting real feedback on it"},
    "Agriculture & Environment": {"noun": "field/environmental", "drill": "analyzing real agricultural or environmental case data"},
    "Hospitality & Tourism":    {"noun": "guest-service", "drill": "role-playing real guest-service or booking scenarios"},
    "Social Work & Community": {"noun": "community-facing", "drill": "practicing real case-management scenarios"},
    "Research & Science":       {"noun": "research", "drill": "designing a small study and critiquing its assumptions"},
    "Sports & Fitness":         {"noun": "performance/coaching", "drill": "analyzing real game or training-session decisions"},
}

SKILL_RESOURCE_TEMPLATES = {
    "communication":       'Practice explaining {noun} ideas to a non-expert — a 5-minute talk on something you know, reviewed by a peer.',
    "problem_solving":     'Work through {drill}, on a regular schedule (weekly is enough to see progress).',
    "creativity":          'Ship one small original {noun} idea every week or two, and share it for feedback.',
    "analytical_thinking": 'Practice structured reasoning through {drill}.',
    "leadership":          'Take a visible lead role in a {noun} group project or club activity this term.',
    "teamwork":            'Join a team-based {noun} project so collaboration is practiced, not just theorized.',
    "technical_ability":   'Build hands-on familiarity through {drill}.',
    "research":            'Practice a structured literature or background review on a {noun} topic you care about.',
    "organization":        'Run one {noun} task end-to-end using a simple tracking system (Notion/Trello), for 30 days.',
    "presentation":        'Record and review yourself explaining a {noun} topic in under 5 minutes.',
}

TOOL_RESOURCES = {
    "git": "Git & GitHub basics (freeCodeCamp or GitHub's own guide)",
    "python": "Python for Everybody (Coursera, free to audit)",
    "sql": "SQLBolt or Mode Analytics SQL tutorial",
    "statistics": "Khan Academy Statistics & Probability",
    "dart_or_js": "Dart or JavaScript fundamentals, depending on your target platform",
    "flutter_or_rn": "Flutter (flutter.dev codelabs) or React Native docs",
    "kotlin": "Kotlin Bootcamp for Programmers (Google)",
    "swift": "100 Days of SwiftUI (free)",
    "financial_modeling": "Corporate Finance Institute's free modeling intro",
    "design_software": "Figma's own beginner tutorials (free)",
    "excel": "ExcelJet or Microsoft's own Excel learning path",
}

PROJECT_ACTION_BY_DOMAIN = {
    "Technology & Computing":    "Build 2-3 small, finished coding projects in",
    "Finance & Business":        "Complete 2-3 real financial analysis case studies in",
    "Design & Creative":         "Build a small portfolio of 2-3 real design pieces in",
    "Public Service & Law":      "Draft 2-3 policy briefs or mock case arguments related to",
    "Education":                 "Design and deliver 2-3 small lesson plans or teaching sessions in",
    "Healthcare & Medicine":     "Complete 2-3 supervised case studies or clinical practicums in",
    "Engineering":               "Build 2-3 small engineering design projects in",
    "Media & Communication":     "Produce 2-3 real pieces of content (articles, videos, posts) related to",
    "Agriculture & Environment": "Complete 2-3 small field studies or case analyses in",
    "Hospitality & Tourism":     "Take on 2-3 real guest-service or event-planning tasks in",
    "Social Work & Community":  "Complete 2-3 supervised case-management exercises in",
    "Research & Science":        "Design and run 2-3 small research studies in",
    "Sports & Fitness":          "Coach or analyze 2-3 real training/performance sessions in",
}

EDUCATION_EXPOSURE_FALLBACK = {
    "+2 / High School": ["Shadow a working professional for a day, or volunteer somewhere adjacent to this field"],
    "Bachelor": ["Apply for an internship or a part-time/entry-level role in this area"],
    "Master": ["Seek a specialization-specific internship, research assistantship, or freelance project"],
}

EDUCATION_TIME_HINT = {
    "+2 / High School": "Next 1-2 months",
    "Bachelor": "Next 1-3 months",
    "Master": "Next 1-3 months",
}


def _skill_detail(skill_key: str, domain: str) -> str:
    template = SKILL_RESOURCE_TEMPLATES.get(skill_key)
    if not template:
        return "Practice deliberately, weekly."
    ctx = DOMAIN_CONTEXT.get(domain, {"noun": "relevant", "drill": "realistic practice problems in this field"})
    return template.format(**ctx)


def _phase(number, name, time_estimate, goal, items, milestone):
    return {"phase": number, "name": name, "time_estimate": time_estimate,
            "goal": goal, "items": items, "milestone": milestone}


def _phase1_understand(domain, role, goal, info):
    topics = info.get("foundational_topics") or [
        f"How {goal} actually works day-to-day, beyond the job title",
        f"The range of directions inside {domain}, before narrowing down",
    ]
    items = [{"title": t, "detail": ""} for t in topics]
    directions = info.get("possible_directions")
    milestone = (f"Identify which part of {goal} interests you most"
                 + (f" — options include {', '.join(directions[:3])}" if directions else "") + ".")
    return _phase(1, "Understand the Field", "1-2 weeks",
                  f"Get a real picture of what {goal} actually involves before investing time in it.",
                  items, milestone)


def _phase2_core_skills(gap_result, domain, goal):
    focus = gap_result.get("focus_first", [])
    strengths = gap_result.get("strengths", [])
    items = []
    for s in focus:
        items.append({
            "title": s["label"],
            "current": s["current"], "required": s["required"],
            "detail": _skill_detail(s["skill"], domain),
            "why": f"{s['label']} is currently {s['current']}/5, while this path's recommended "
                   f"profile is {s['required']}/5 — one of your largest relevant gaps.",
        })
    if not items:
        strong_names = ", ".join(s["label"] for s in strengths[:3]) if strengths else "your current skills"
        items.append({
            "title": "Apply what you already have",
            "detail": f"Your core skills ({strong_names}) already meet or exceed what this path "
                      f"typically needs — the priority now is applying them in real situations, "
                      f"not drilling them further.",
            "why": "No large skill gaps stood out relative to this path's recommended profile.",
        })
    return _phase(2, "Build Core Skills", "2-5 weeks",
                  "Strengthen the skills this path relies on most, starting with your biggest actual "
                  "gaps — not skills you've already got.",
                  items, "Notice a real improvement in your weakest priority skill above.")


def _phase3_tools_methods(gap_result, info, domain):
    items = []
    tool_gaps = [t for t in gap_result.get("tools", []) if t["gap"] > 0]
    for t in tool_gaps:
        items.append({"title": t["label"], "detail": TOOL_RESOURCES.get(t["tool"], f"Look for a beginner {t['label']} course.")})

    methods = info.get("field_methods", [])
    for m in methods:
        items.append({"title": m, "detail": ""})

    tools_context = info.get("tools_context", [])
    if tools_context and not tool_gaps:
        items.append({"title": "Tools worth getting familiar with", "detail": ", ".join(tools_context)})

    if not items:
        items.append({"title": "Explore common approaches in this field",
                       "detail": DOMAIN_CONTEXT.get(domain, {}).get("drill", "realistic practice in this field")})

    return _phase(3, "Learn Tools & Methods", "4-8 weeks",
                  "Pick up the practical tools and working methods people in this path actually use.",
                  items, "Be able to use at least one core tool/method here without hand-holding.")


def _phase4_project(info, goal, regulated, domain):
    if regulated:
        return _phase(4, "Understand the Formal Pathway", "Varies by program",
                      f"{goal} requires accredited formal education (and, where applicable, "
                      f"licensing and supervised clinical training) — not a self-directed project.",
                      [{"title": "Research accredited programs and their entry requirements", "detail": ""},
                       {"title": "Confirm licensing/registration requirements in your country", "detail": ""}],
                      "Have a clear, confirmed picture of the formal path required.")

    project = info.get("project")
    if project:
        items = [{"title": step, "detail": ""} for step in project["steps"]]
        milestone = f"A finished output: \"{project['title']}\"."
    else:
        action = PROJECT_ACTION_BY_DOMAIN.get(domain, "Get 2-3 pieces of real, hands-on practice in")
        items = [{"title": f"{action} {goal}",
                   "detail": "Real, demonstrable experience (even small) matters more than course "
                             "certificates alone. Document it where possible."}]
        milestone = "A small, finished piece of work you can show or describe in an interview."

    return _phase(4, "Complete a Practical Project", "2-4 weeks", "Turn what you've learned into one real, finished output.",
                  items, milestone)


def _phase5_exposure(info, education_level, goal, regulated):
    ideas = (info.get("experience_ideas") or {}).get(education_level) \
        or EDUCATION_EXPOSURE_FALLBACK.get(education_level, [])
    items = [{"title": idea, "detail": ""} for idea in ideas]
    time_hint = EDUCATION_TIME_HINT.get(education_level, "Next 1-3 months")
    goal_text = (f"Get real-world exposure to {goal} appropriate for your current stage."
                 if not regulated else
                 f"Get exposure to the field while you work toward the formal qualification.")
    return _phase(5, "Get Real Exposure", time_hint, goal_text, items,
                  "A real conversation, placement, or activity that tells you if this direction "
                  "still feels right.")


def _phase6_next_direction(info, goal, specialization):
    directions = info.get("possible_directions", [])
    if specialization:
        directions = [d for d in directions if d.lower() not in specialization.lower()]
    items = [{"title": d, "detail": ""} for d in directions] or \
        [{"title": f"Keep exploring within {goal}", "detail": ""}]
    return _phase(6, "Choose a Direction", "Ongoing",
                  "Use what you learned in the phases above to narrow down further.",
                  items, "Which part of the experience did you enjoy most? Let that guide what's next.")


def generate_roadmap(gap_result: dict, education_level: str = "Bachelor") -> dict:
    domain = gap_result["domain"]
    role = gap_result.get("role")
    specialization = gap_result.get("specialization")
    goal = specialization or role or domain

    info = get_career_knowledge(domain, role, specialization) if role else {}
    regulated = is_regulated(domain, role) if role else False

    phases = [
        _phase1_understand(domain, role, goal, info),
        _phase2_core_skills(gap_result, domain, goal),
        _phase3_tools_methods(gap_result, info, domain),
        _phase4_project(info, goal, regulated, domain),
        _phase5_exposure(info, education_level, goal, regulated),
        _phase6_next_direction(info, goal, specialization),
    ]

    return {
        "roadmap_label": ROADMAP_LABEL,
        "disclaimer": ROADMAP_DISCLAIMER,
        "regulated_notice": REGULATED_NOTICE if regulated else None,
        "education_note": info.get("education_preparation"),
        "phases": phases,
    }
