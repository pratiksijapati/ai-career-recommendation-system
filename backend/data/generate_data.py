
import numpy as np
import pandas as pd
import random
import os

from career_taxonomy import CAREER_TAXONOMY, flatten_roles
from interest_taxonomy import INTEREST_TAXONOMY, all_tags, tag_to_domain

np.random.seed(42)
random.seed(42)

# =============================================================
# COLUMN DEFINITIONS
# =============================================================

SKILL_COLS = [
    "communication", "problem_solving", "creativity", "analytical_thinking",
    "leadership", "teamwork", "technical_ability", "research",
    "organization", "presentation",
]

SCORE_COLS = [
    "math_score", "science_score", "english_score",
    "computer_score", "business_score", "arts_score",
]

PREFERENCE_COLS = [
    "pref_people_vs_independent",
    "pref_creative_vs_analytical",
    "pref_indoor_vs_outdoor",
    "pref_structured_vs_flexible",
    "pref_handson_vs_theoretical",
    "pref_tech_vs_people",
]

EDUCATION_LEVELS = ["+2 / High School", "Bachelor", "Master"]

INTEREST_TAGS = all_tags()          # 78 tags, one-hot-ish with 0-3 strength
TAG_TO_DOMAIN = tag_to_domain()


def _collect_tool_cols():
    tools = set()
    for ddata in CAREER_TAXONOMY.values():
        for rdata in ddata["roles"].values():
            for sdata in rdata.get("specializations", {}).values():
                tools.update(sdata.get("tools_required", {}).keys())
                for sub in sdata.get("sub_specializations", {}).values():
                    tools.update(sub.get("tools_required", {}).keys())
    return sorted(tools)


TOOL_COLS = _collect_tool_cols()


DOMAIN_PROFILES = {
    "Technology & Computing": {
        "skills": {"communication": 3.0, "problem_solving": 4.3, "creativity": 3.2,
                   "analytical_thinking": 4.3, "leadership": 2.8, "teamwork": 3.3,
                   "technical_ability": 4.5, "research": 3.5, "organization": 3.2,
                   "presentation": 2.8},
        "scores": {"math_score": 88, "science_score": 80, "english_score": 72,
                   "computer_score": 92, "business_score": 62, "arts_score": 55},
        "prefs": {"pref_people_vs_independent": 2.0, "pref_creative_vs_analytical": 2.0,
                  "pref_indoor_vs_outdoor": 2.0, "pref_structured_vs_flexible": 3.0,
                  "pref_handson_vs_theoretical": 3.5, "pref_tech_vs_people": 1.5},
    },
    "Finance & Business": {
        "skills": {"communication": 3.8, "problem_solving": 3.8, "creativity": 3.0,
                   "analytical_thinking": 4.2, "leadership": 3.8, "teamwork": 3.5,
                   "technical_ability": 2.5, "research": 3.3, "organization": 4.0,
                   "presentation": 3.5},
        "scores": {"math_score": 85, "science_score": 65, "english_score": 82,
                   "computer_score": 70, "business_score": 92, "arts_score": 58},
        "prefs": {"pref_people_vs_independent": 3.5, "pref_creative_vs_analytical": 2.5,
                  "pref_indoor_vs_outdoor": 2.0, "pref_structured_vs_flexible": 2.3,
                  "pref_handson_vs_theoretical": 3.0, "pref_tech_vs_people": 3.5},
    },
    "Design & Creative": {
        "skills": {"communication": 4.0, "problem_solving": 3.5, "creativity": 4.8,
                   "analytical_thinking": 3.0, "leadership": 2.8, "teamwork": 3.2,
                   "technical_ability": 2.5, "research": 3.2, "organization": 3.0,
                   "presentation": 3.8},
        "scores": {"math_score": 65, "science_score": 62, "english_score": 80,
                   "computer_score": 75, "business_score": 60, "arts_score": 92},
        "prefs": {"pref_people_vs_independent": 3.0, "pref_creative_vs_analytical": 4.5,
                  "pref_indoor_vs_outdoor": 2.5, "pref_structured_vs_flexible": 4.0,
                  "pref_handson_vs_theoretical": 4.0, "pref_tech_vs_people": 3.0},
    },
    "Public Service & Law": {
        "skills": {"communication": 4.3, "problem_solving": 3.8, "creativity": 2.8,
                   "analytical_thinking": 4.0, "leadership": 4.2, "teamwork": 3.8,
                   "technical_ability": 1.8, "research": 3.5, "organization": 3.8,
                   "presentation": 4.0},
        "scores": {"math_score": 75, "science_score": 68, "english_score": 88,
                   "computer_score": 62, "business_score": 75, "arts_score": 62},
        "prefs": {"pref_people_vs_independent": 4.2, "pref_creative_vs_analytical": 2.5,
                  "pref_indoor_vs_outdoor": 2.5, "pref_structured_vs_flexible": 2.0,
                  "pref_handson_vs_theoretical": 3.0, "pref_tech_vs_people": 4.0},
    },
    "Education": {
        "skills": {"communication": 4.5, "problem_solving": 3.3, "creativity": 3.5,
                   "analytical_thinking": 3.5, "leadership": 3.8, "teamwork": 3.8,
                   "technical_ability": 2.2, "research": 3.3, "organization": 3.5,
                   "presentation": 4.3},
        "scores": {"math_score": 72, "science_score": 70, "english_score": 85,
                   "computer_score": 65, "business_score": 65, "arts_score": 68},
        "prefs": {"pref_people_vs_independent": 4.3, "pref_creative_vs_analytical": 3.0,
                  "pref_indoor_vs_outdoor": 2.5, "pref_structured_vs_flexible": 2.8,
                  "pref_handson_vs_theoretical": 2.8, "pref_tech_vs_people": 4.3},
    },
    "Healthcare & Medicine": {
        "skills": {"communication": 4.2, "problem_solving": 4.3, "creativity": 2.8,
                   "analytical_thinking": 4.5, "leadership": 3.5, "teamwork": 3.8,
                   "technical_ability": 2.2, "research": 3.8, "organization": 3.5,
                   "presentation": 3.0},
        "scores": {"math_score": 82, "science_score": 93, "english_score": 78,
                   "computer_score": 65, "business_score": 60, "arts_score": 58},
        "prefs": {"pref_people_vs_independent": 4.3, "pref_creative_vs_analytical": 2.0,
                  "pref_indoor_vs_outdoor": 2.5, "pref_structured_vs_flexible": 2.0,
                  "pref_handson_vs_theoretical": 3.5, "pref_tech_vs_people": 4.3},
    },
    "Engineering": {
        "skills": {"communication": 3.2, "problem_solving": 4.4, "creativity": 3.5,
                   "analytical_thinking": 4.4, "leadership": 3.3, "teamwork": 3.3,
                   "technical_ability": 4.2, "research": 3.5, "organization": 3.5,
                   "presentation": 2.8},
        "scores": {"math_score": 90, "science_score": 88, "english_score": 72,
                   "computer_score": 75, "business_score": 62, "arts_score": 62},
        "prefs": {"pref_people_vs_independent": 2.5, "pref_creative_vs_analytical": 2.2,
                  "pref_indoor_vs_outdoor": 2.5, "pref_structured_vs_flexible": 2.5,
                  "pref_handson_vs_theoretical": 4.0, "pref_tech_vs_people": 1.8},
    },
    "Media & Communication": {
        "skills": {"communication": 4.6, "problem_solving": 3.3, "creativity": 4.5,
                   "analytical_thinking": 3.2, "leadership": 3.2, "teamwork": 3.0,
                   "technical_ability": 2.5, "research": 3.3, "organization": 2.8,
                   "presentation": 4.0},
        "scores": {"math_score": 65, "science_score": 62, "english_score": 90,
                   "computer_score": 70, "business_score": 65, "arts_score": 78},
        "prefs": {"pref_people_vs_independent": 3.8, "pref_creative_vs_analytical": 4.2,
                  "pref_indoor_vs_outdoor": 2.8, "pref_structured_vs_flexible": 4.0,
                  "pref_handson_vs_theoretical": 3.3, "pref_tech_vs_people": 3.5},
    },
    "Agriculture & Environment": {
        "skills": {"communication": 3.2, "problem_solving": 3.8, "creativity": 3.0,
                   "analytical_thinking": 4.0, "leadership": 3.0, "teamwork": 3.3,
                   "technical_ability": 2.5, "research": 4.0, "organization": 3.2,
                   "presentation": 2.8},
        "scores": {"math_score": 78, "science_score": 87, "english_score": 72,
                   "computer_score": 63, "business_score": 65, "arts_score": 58},
        "prefs": {"pref_people_vs_independent": 2.8, "pref_creative_vs_analytical": 2.3,
                  "pref_indoor_vs_outdoor": 4.2, "pref_structured_vs_flexible": 3.0,
                  "pref_handson_vs_theoretical": 3.8, "pref_tech_vs_people": 2.5},
    },
    "Hospitality & Tourism": {
        "skills": {"communication": 4.3, "problem_solving": 3.2, "creativity": 3.5,
                   "analytical_thinking": 2.8, "leadership": 3.5, "teamwork": 3.8,
                   "technical_ability": 2.0, "research": 2.5, "organization": 3.5,
                   "presentation": 3.5},
        "scores": {"math_score": 65, "science_score": 60, "english_score": 82,
                   "computer_score": 62, "business_score": 75, "arts_score": 68},
        "prefs": {"pref_people_vs_independent": 4.5, "pref_creative_vs_analytical": 3.2,
                  "pref_indoor_vs_outdoor": 3.0, "pref_structured_vs_flexible": 3.5,
                  "pref_handson_vs_theoretical": 3.8, "pref_tech_vs_people": 4.3},
    },
    "Social Work & Community": {
        "skills": {"communication": 4.5, "problem_solving": 3.5, "creativity": 3.2,
                   "analytical_thinking": 3.3, "leadership": 3.5, "teamwork": 4.0,
                   "technical_ability": 1.8, "research": 3.2, "organization": 3.2,
                   "presentation": 3.2},
        "scores": {"math_score": 62, "science_score": 65, "english_score": 82,
                   "computer_score": 60, "business_score": 62, "arts_score": 65},
        "prefs": {"pref_people_vs_independent": 4.6, "pref_creative_vs_analytical": 3.0,
                  "pref_indoor_vs_outdoor": 3.0, "pref_structured_vs_flexible": 3.3,
                  "pref_handson_vs_theoretical": 3.3, "pref_tech_vs_people": 4.5},
    },
    "Research & Science": {
        "skills": {"communication": 3.0, "problem_solving": 4.3, "creativity": 3.5,
                   "analytical_thinking": 4.7, "leadership": 2.8, "teamwork": 3.0,
                   "technical_ability": 3.2, "research": 4.6, "organization": 3.3,
                   "presentation": 2.8},
        "scores": {"math_score": 90, "science_score": 92, "english_score": 75,
                   "computer_score": 75, "business_score": 60, "arts_score": 58},
        "prefs": {"pref_people_vs_independent": 2.0, "pref_creative_vs_analytical": 1.8,
                  "pref_indoor_vs_outdoor": 2.8, "pref_structured_vs_flexible": 2.5,
                  "pref_handson_vs_theoretical": 3.2, "pref_tech_vs_people": 1.8},
    },
    "Sports & Fitness": {
        "skills": {"communication": 3.8, "problem_solving": 3.2, "creativity": 3.2,
                   "analytical_thinking": 2.8, "leadership": 4.0, "teamwork": 4.2,
                   "technical_ability": 2.2, "research": 2.5, "organization": 3.0,
                   "presentation": 3.3},
        "scores": {"math_score": 62, "science_score": 63, "english_score": 72,
                   "computer_score": 58, "business_score": 60, "arts_score": 62},
        "prefs": {"pref_people_vs_independent": 4.2, "pref_creative_vs_analytical": 3.0,
                  "pref_indoor_vs_outdoor": 4.3, "pref_structured_vs_flexible": 3.3,
                  "pref_handson_vs_theoretical": 4.3, "pref_tech_vs_people": 4.0},
    },
}

# Role-level deltas -- only the dimensions that genuinely distinguish a
# role from its domain baseline are listed. Everything else is
# inherited unchanged from DOMAIN_PROFILES. Roles with no entry here
# just use the domain baseline as-is.
ROLE_OVERRIDES = {
    # Technology & Computing
    "Software Developer":      {"skills": {"creativity": 3.6}},
    "Data Scientist":          {"skills": {"analytical_thinking": 4.8, "research": 4.2}},
    "Data Analyst":            {"skills": {"organization": 3.8, "analytical_thinking": 4.0}},
    "Cybersecurity Analyst":   {"skills": {"analytical_thinking": 4.5, "technical_ability": 4.4}},
    "Network Engineer":        {"skills": {"technical_ability": 4.0, "problem_solving": 4.0}},
    "IT Support Specialist":   {"skills": {"communication": 3.8, "technical_ability": 3.3}},
    "Cloud / DevOps Engineer": {"skills": {"organization": 4.0, "technical_ability": 4.4}},

    # Finance & Business
    "Financial Analyst":        {"skills": {"analytical_thinking": 4.5}},
    "Marketing Manager":        {"skills": {"creativity": 4.0, "communication": 4.3}},
    "Banking Officer":          {"skills": {"communication": 4.0}},
    "Chartered Accountant":     {"skills": {"analytical_thinking": 4.4, "organization": 4.3}},
    "Business Analyst":         {"skills": {"communication": 4.2, "analytical_thinking": 4.0}},
    "Entrepreneur":             {"skills": {"leadership": 4.5, "creativity": 4.0}},
    "Human Resources Manager":  {"skills": {"communication": 4.4, "leadership": 4.0}},
    "Supply Chain Manager":     {"skills": {"organization": 4.4, "analytical_thinking": 4.0}},
    "Insurance Agent":          {"skills": {"communication": 4.3}},

    # Design & Creative
    "UX/UI Designer":   {"skills": {"analytical_thinking": 3.4}},
    "Graphic Designer": {"skills": {"creativity": 4.9, "analytical_thinking": 2.6}},
    "Video Editor":     {"skills": {"creativity": 4.6, "technical_ability": 3.0}},
    "Photographer":     {"skills": {"creativity": 4.7, "communication": 3.5}},

    # Public Service & Law
    "Civil Servant (Loksewa)":     {"skills": {"organization": 4.0}},
    "Police Officer":              {"skills": {"leadership": 4.4, "technical_ability": 1.3},
                                     "prefs": {"pref_indoor_vs_outdoor": 3.5}},
    "Army Officer":                {"skills": {"leadership": 4.7},
                                     "prefs": {"pref_indoor_vs_outdoor": 3.8}},
    "Diplomat / Foreign Affairs":  {"skills": {"communication": 4.6, "research": 4.0}},
    "Lawyer / Advocate":           {"skills": {"analytical_thinking": 4.4, "communication": 4.6}},
    "Legal Consultant":            {"skills": {"analytical_thinking": 4.4, "research": 4.0}},

    # Education
    "School Teacher":         {"skills": {"presentation": 4.4}},
    "University Professor":   {"skills": {"research": 4.3, "analytical_thinking": 4.2}},
    "Education Counselor":    {"skills": {"communication": 4.6}},
    "Instructional Designer": {"skills": {"creativity": 3.8, "technical_ability": 3.0}},

    # Healthcare & Medicine
    "Medical Doctor":        {"skills": {"analytical_thinking": 4.8, "leadership": 4.0},
                               "scores": {"science_score": 95}},
    "Nurse":                 {"skills": {"communication": 4.4}},
    "Pharmacist":            {"skills": {"analytical_thinking": 4.3},
                               "scores": {"science_score": 90}},
    "Dentist":               {"skills": {"technical_ability": 3.0},
                               "scores": {"science_score": 90}},
    "Public Health Officer": {"skills": {"research": 4.2, "leadership": 4.0}},

    # Engineering
    "Civil Engineer":         {"skills": {"analytical_thinking": 4.5}},
    "Electrical Engineer":    {"skills": {"technical_ability": 4.5}},
    "Mechanical Engineer":    {"skills": {"technical_ability": 4.3}},
    "Environmental Engineer": {"skills": {"research": 4.0}},
    "Architect":              {"skills": {"creativity": 4.5, "technical_ability": 3.5}},

    # Media & Communication
    "Journalist":              {"skills": {"communication": 4.8, "research": 3.8}},
    "Content Creator":         {"skills": {"creativity": 4.7, "technical_ability": 2.8}},
    "Radio/TV Presenter":      {"skills": {"communication": 4.9, "presentation": 4.6}},
    "Social Media Strategist": {"skills": {"creativity": 4.2, "organization": 3.5}},

    # Agriculture & Environment
    "Agricultural Scientist":   {"skills": {"research": 4.2}},
    "Veterinary Doctor":        {"skills": {"analytical_thinking": 4.2},
                                  "scores": {"science_score": 90}},
    "Environmental Scientist":  {"skills": {"research": 4.4}},

    # Hospitality & Tourism
    "Hotel Manager":         {"skills": {"leadership": 4.2, "organization": 4.0}},
    "Tour Guide":            {"skills": {"communication": 4.7}},
    "Chef / Culinary Artist": {"skills": {"creativity": 4.3, "technical_ability": 2.8}},
    "Event Planner":         {"skills": {"organization": 4.4, "creativity": 3.8}},

    # Social Work & Community
    "Social Worker":       {"skills": {"communication": 4.6}},
    "NGO Program Officer": {"skills": {"organization": 3.8, "leadership": 3.8}},
    "Psychologist":        {"skills": {"analytical_thinking": 4.0, "research": 3.8}},

    # Research & Science
    "Research Scientist": {"skills": {"research": 4.8}},
    "Geologist":          {"skills": {"research": 4.3, "technical_ability": 3.5}},
    "Lab Technician":     {"skills": {"organization": 3.8, "technical_ability": 3.3}},

    # Sports & Fitness
    "Sports Coach":     {"skills": {"leadership": 4.4}},
    "Fitness Trainer":  {"skills": {"communication": 4.0}},
    "Sports Analyst":   {"skills": {"analytical_thinking": 4.0},
                          "prefs": {"pref_indoor_vs_outdoor": 3.0}},
    "Athlete":          {"skills": {"teamwork": 4.5},
                          "prefs": {"pref_indoor_vs_outdoor": 4.5}},
}

# Specialization-level tool-skill means, pulled straight from
# career_taxonomy.py's "tools_required" dicts -- no separate
# authoring needed, single source of truth.
def _spec_tool_means(role_data: dict) -> dict:
    """{ 'Specialization' or 'Specialization — Sub': {tool: mean_level} }"""
    out = {}
    for spec, sdata in role_data.get("specializations", {}).items():
        if "sub_specializations" in sdata:
            for sub, subdata in sdata["sub_specializations"].items():
                out[f"{spec} — {sub}"] = subdata.get("tools_required", {})
        else:
            out[spec] = sdata.get("tools_required", {})
    return out


NEPALI_NAMES_MALE = [
    "Aarav", "Aditya", "Arjun", "Ayush", "Bibek", "Bikash", "Binod", "Bishal",
    "Deepak", "Dinesh", "Gaurav", "Hari", "Krishna", "Manish", "Milan",
    "Nabin", "Nirajan", "Pradip", "Prashant", "Pratik", "Rajesh", "Ramesh",
    "Roshan", "Sagar", "Sandesh", "Sanjay", "Santosh", "Saroj", "Sujit",
    "Suraj", "Suresh", "Ujjwal", "Utsav", "Yuvraj", "Bimal", "Diwash",
]
NEPALI_NAMES_FEMALE = [
    "Aakriti", "Alisha", "Anita", "Anjali", "Anuja", "Archana", "Astha",
    "Barsha", "Bhumika", "Deepa", "Diksha", "Gita", "Jyoti", "Kabita",
    "Kritika", "Laxmi", "Manisha", "Mina", "Namrata", "Nisha", "Pooja",
    "Priya", "Radhika", "Rekha", "Rojina", "Sabina", "Sarita", "Shreya",
    "Shristi", "Sita", "Smriti", "Sunita", "Sweta", "Anisha", "Sangita",
]
PROVINCES = ["Koshi", "Madhesh", "Bagmati", "Gandaki", "Lumbini", "Karnali", "Sudurpashchim"]


def clip5(v):
    return int(np.clip(round(v), 1, 5))


def clip100(v):
    return int(np.clip(round(v), 30, 100))


def clippref(v):
    return int(np.clip(round(v), 1, 5))


def get_role_profile(domain: str, role: str, amplify: float = 2.5) -> dict:
    """
    Merge domain baseline with role-level overrides. Overrides are
    AMPLIFIED relative to the domain baseline rather than substituted
    outright -- the hand-authored deltas were written small (e.g.
    "slightly more analytical"), and widening the base skill/score
    noise to fix domain-level leakage would otherwise drown those
    small role-level distinctions out completely.
    """
    base = DOMAIN_PROFILES[domain]
    override = ROLE_OVERRIDES.get(role, {})
    merged = {"skills": dict(base["skills"]), "scores": dict(base["scores"]),
              "prefs": dict(base["prefs"])}

    for group in ("skills", "scores", "prefs"):
        for key, value in override.get(group, {}).items():
            baseline = base[group][key]
            merged[group][key] = baseline + amplify * (value - baseline)

    return merged


def generate_student(student_id: int, domain: str, role: str,
                      specialization: str = None) -> dict:
    profile = get_role_profile(domain, role)

    gender = random.choice(["Male", "Female"])
    name = random.choice(NEPALI_NAMES_MALE if gender == "Male" else NEPALI_NAMES_FEMALE)
    education = random.choices(EDUCATION_LEVELS, weights=[0.45, 0.4, 0.15])[0]

    record = {
        "student_id": student_id, "name": name, "gender": gender,
        "province": random.choice(PROVINCES), "education_level": education,
        "domain": domain, "role": role,
        "specialization": specialization if specialization else "",
    }

    for skill, mean in profile["skills"].items():
        record[skill] = clip5(np.random.normal(mean, 0.85))
    for score, mean in profile["scores"].items():
        record[score] = clip100(np.random.normal(mean, 13))
    for pref, mean in profile["prefs"].items():
        record[pref] = clippref(np.random.normal(mean, 1.0))

    # Interest tags: real people aren't cleanly one-domain. Moderate
    # strength on this role's own domain tags, a *secondary* domain
    # (randomly picked, different from the primary) gets a smaller
    # boost to model genuine side-interests, and everything else gets
    # low-level background noise. This keeps domain the dominant
    # signal without making it a giveaway -- a dataset where interest
    # tags perfectly encode the label would make the Domain model's
    # accuracy meaningless (99%+ is a leakage red flag, not a good
    # result).
    domain_tags = INTEREST_TAXONOMY[domain]
    other_domains = [d for d in INTEREST_TAXONOMY if d != domain]
    secondary_domain = random.choice(other_domains)
    secondary_tags = INTEREST_TAXONOMY[secondary_domain] if random.random() < 0.4 else []

    for tag in INTEREST_TAGS:
        if tag in domain_tags:
            record[tag] = int(np.clip(round(np.random.normal(1.6, 0.85)), 0, 3)) \
                if random.random() < 0.55 else 0
        elif tag in secondary_tags:
            record[tag] = int(np.clip(round(np.random.normal(1.1, 0.75)), 0, 3)) \
                if random.random() < 0.4 else 0
        else:
            # Kept deliberately low: a realistic user only selects a
            # handful of tags in their real domain of interest (2-3
            # tags, not all of them), so unrelated-domain background
            # noise must stay well below what 2-3 genuine selections
            # produce, or a small real selection can't be told apart
            # from pure noise in an unrelated domain.
            record[tag] = random.choices([0, 1, 2], weights=[0.80, 0.14, 0.06])[0]

    # Tool skills: 0 for everyone except students in the matching
    # specialization, where a modest, mostly-beginner level is sampled
    # (nobody is already expert in a specialization they're just
    # entering -- this models "current exposure", not aspiration)
    role_data = CAREER_TAXONOMY[domain]["roles"][role]
    spec_tools = _spec_tool_means(role_data)
    for tool in TOOL_COLS:
        record[tool] = 0
    if specialization and specialization in spec_tools:
        for tool, required_level in spec_tools[specialization].items():
            beginner_mean = max(1.0, required_level - 2.0)
            record[tool] = clip5(np.random.normal(beginner_mean, 0.6))

    return record


def generate_dataset(students_per_role: int = 40) -> pd.DataFrame:
    all_students = []
    student_id = 1

    for domain, ddata in CAREER_TAXONOMY.items():
        for role, rdata in ddata["roles"].items():
            spec_tools = _spec_tool_means(rdata)
            if spec_tools:
                # Split this role's quota evenly across its specializations
                per_spec = max(25, students_per_role // len(spec_tools))
                for spec in spec_tools:
                    for _ in range(per_spec):
                        all_students.append(
                            generate_student(student_id, domain, role, spec))
                        student_id += 1
            else:
                for _ in range(students_per_role):
                    all_students.append(generate_student(student_id, domain, role))
                    student_id += 1

    df = pd.DataFrame(all_students)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df["student_id"] = range(1, len(df) + 1)
    return df


if __name__ == "__main__":
    df = generate_dataset(students_per_role=40)

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "career_data.csv")
    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Domains: {df['domain'].nunique()}")
    print(f"Roles: {df['role'].nunique()}")
    print(f"Specializations (non-empty): {df[df['specialization'] != '']['specialization'].nunique()}")
    print("\nRows per domain:")
    print(df["domain"].value_counts().to_string())
