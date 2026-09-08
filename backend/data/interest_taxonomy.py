# =============================================================
# backend/data/interest_taxonomy.py
# =============================================================
# PURPOSE:
#   A curated, bounded interest-tag vocabulary — the honest middle
#   ground between "6 rigid checkboxes" (too coarse to be useful)
#   and "unlimited free text" (can't be fed into a model at all).
#
#   Each tag belongs to exactly one broad Interest Domain, used to
#   build a coarse aggregate feature for the Level-1 Domain model,
#   while the individual tags themselves feed the more detailed
#   Level-2/3 models where fine-grained interest actually matters.
#
#   A student's "add your own" free-text interest (captured in the
#   frontend) is stored for later human review, NOT auto-converted
#   into a new tag/feature — that would be pretending an unreviewed
#   guess is structured data.
# =============================================================

INTEREST_TAXONOMY = {
    "Technology & Computing": [
        "Programming", "Web Development", "Mobile Apps", "Gaming",
        "Artificial Intelligence", "Cybersecurity", "Cloud Computing",
    ],
    "Design & Creative": [
        "Graphic Design", "UI/UX Design", "Photography", "Video Editing",
        "Animation", "Fashion Design", "Illustration",
    ],
    "Finance & Business": [
        "Investing", "Stock Market", "Entrepreneurship", "Accounting",
        "Marketing", "E-commerce", "Startups",
    ],
    "Public Service & Law": [
        "Law", "Politics", "Public Administration", "Military",
        "Policing & Security", "Human Rights", "Diplomacy",
    ],
    "Education": [
        "Teaching", "Mentoring", "Public Speaking", "Educational Technology",
    ],
    "Healthcare & Medicine": [
        "Medicine", "Nursing", "Mental Health", "Nutrition",
        "Fitness & Wellness", "Pharmacy",
    ],
    "Engineering": [
        "Mechanical Systems", "Electrical Systems", "Construction",
        "Robotics", "Automotive", "Renewable Energy",
    ],
    "Media & Communication": [
        "YouTube / Video Production", "Blogging", "Journalism",
        "Podcasting", "Content Creation", "Social Media Strategy",
    ],
    "Agriculture & Environment": [
        "Farming", "Sustainability", "Wildlife", "Environmental Conservation",
        "Climate Science",
    ],
    "Hospitality & Tourism": [
        "Travelling", "Cooking", "Hotel Management", "Event Planning", "Tour Guiding",
    ],
    "Social Work & Community": [
        "Volunteering", "Counseling", "Community Organizing",
        "Working with Children", "Non-profit Work",
    ],
    "Research & Science": [
        "Scientific Research", "Data Analysis", "Astronomy",
        "Chemistry", "Biology", "Physics",
    ],
    "Sports & Fitness": [
        "Football", "Cricket", "Swimming", "Coaching",
        "Sports Analytics", "Sports Journalism", "Esports",
    ],
}


# =============================================================
# ROLE-LEVEL interest affinity -- which of a domain's own tags
# actually relate to which specific role inside it.
#
# WHY THIS EXISTS: the Role-level Random Forest is trained on the raw
# domain tags as features, but the synthetic dataset only differentiates
# interest strength at the DOMAIN level (see generate_data.py) -- it
# never authored "Athlete students pick Football more than Fitness
# Trainer students do." Investigated a real user report (selecting
# "Football" recommended Fitness Trainer over Athlete) and confirmed
# via direct model inspection: Football didn't even crack the role
# model's top 15 feature importances, and the synthetic training data
# actually has Fitness Trainer's average Football tag strength (1.27)
# HIGHER than Athlete's (0.55) -- backwards from real-world intuition,
# and not fixable by any reweighting of that same data (there's no
# signal to reweight FROM). This is real-world domain knowledge the
# dataset never captured, so it's hand-authored here, the same way
# career_knowledge.py captures things the synthetic dataset can't.
#
# Not exhaustive for every role -- a role with no obvious tag mapping
# (e.g. Fitness Trainer, which has no dedicated tag of its own) is
# simply omitted; role-level scoring treats a missing entry as "no
# specific interest signal available" rather than guessing.
# =============================================================

ROLE_INTEREST_TAGS = {
    "Technology & Computing": {
        "Software Developer": ["Programming", "Web Development", "Mobile Apps", "Gaming"],
        "Data Scientist": ["Artificial Intelligence", "Programming"],
        "Data Analyst": ["Artificial Intelligence"],
        "Cybersecurity Analyst": ["Cybersecurity", "Programming"],
        "Network Engineer": ["Cloud Computing", "Cybersecurity"],
        "IT Support Specialist": ["Cloud Computing"],
        "Cloud / DevOps Engineer": ["Cloud Computing", "Programming"],
    },
    "Finance & Business": {
        "Financial Analyst": ["Investing", "Stock Market"],
        "Marketing Manager": ["Marketing", "E-commerce", "Entrepreneurship"],
        "Banking Officer": ["Investing", "Accounting"],
        "Chartered Accountant": ["Accounting"],
        "Business Analyst": ["Entrepreneurship", "Startups"],
        "Entrepreneur": ["Entrepreneurship", "Startups", "E-commerce"],
        "Supply Chain Manager": ["E-commerce"],
        "Insurance Agent": ["Investing", "Accounting"],
    },
    "Design & Creative": {
        "UX/UI Designer": ["UI/UX Design"],
        "Graphic Designer": ["Graphic Design", "Illustration"],
        "Video Editor": ["Video Editing", "Animation"],
        "Photographer": ["Photography"],
    },
    "Public Service & Law": {
        "Civil Servant (Loksewa)": ["Public Administration"],
        "Police Officer": ["Policing & Security"],
        "Army Officer": ["Military"],
        "Diplomat / Foreign Affairs": ["Diplomacy", "Politics"],
        "Lawyer / Advocate": ["Law", "Human Rights"],
        "Legal Consultant": ["Law"],
    },
    "Education": {
        "School Teacher": ["Teaching", "Mentoring"],
        "University Professor": ["Teaching", "Educational Technology"],
        "Education Counselor": ["Mentoring", "Public Speaking"],
        "Instructional Designer": ["Educational Technology", "Teaching"],
    },
    "Healthcare & Medicine": {
        "Medical Doctor": ["Medicine"],
        "Public Health Officer": ["Medicine", "Nutrition"],
        "Nurse": ["Nursing", "Medicine"],
        "Pharmacist": ["Pharmacy"],
        "Dentist": ["Medicine"],
    },
    "Engineering": {
        "Civil Engineer": ["Construction"],
        "Electrical Engineer": ["Electrical Systems", "Renewable Energy"],
        "Mechanical Engineer": ["Mechanical Systems", "Automotive"],
        "Environmental Engineer": ["Renewable Energy"],
        "Architect": ["Construction"],
    },
    "Media & Communication": {
        "Journalist": ["Journalism", "Blogging"],
        "Content Creator": ["Content Creation", "YouTube / Video Production", "Social Media Strategy"],
        "Radio/TV Presenter": ["Podcasting", "YouTube / Video Production"],
        "Social Media Strategist": ["Social Media Strategy", "Content Creation"],
    },
    "Agriculture & Environment": {
        "Agricultural Scientist": ["Farming"],
        "Veterinary Doctor": ["Wildlife"],
        "Environmental Scientist": ["Sustainability", "Environmental Conservation", "Climate Science"],
    },
    "Hospitality & Tourism": {
        "Hotel Manager": ["Hotel Management"],
        "Tour Guide": ["Tour Guiding", "Travelling"],
        "Chef / Culinary Artist": ["Cooking"],
        "Event Planner": ["Event Planning"],
    },
    "Social Work & Community": {
        "Social Worker": ["Volunteering", "Non-profit Work", "Community Organizing"],
        "NGO Program Officer": ["Non-profit Work", "Community Organizing"],
        "Psychologist": ["Counseling"],
    },
    "Research & Science": {
        "Research Scientist": ["Scientific Research"],
        "Geologist": ["Scientific Research"],
        "Lab Technician": ["Chemistry", "Biology"],
    },
    "Sports & Fitness": {
        # Deliberately just "Coaching" -- liking/playing Football or Cricket
        # is interest in the SPORT, not evidence of wanting to coach it.
        # Those tags stay under Athlete, where playing interest actually
        # belongs; conflating the two overstated how much a sports fan's
        # tag choices say about wanting a coaching career specifically.
        "Sports Coach": ["Coaching"],
        "Sports Analyst": ["Sports Analytics", "Sports Journalism"],
        "Athlete": ["Football", "Cricket", "Swimming", "Esports"],
        # Fitness Trainer has no dedicated tag in this taxonomy -- left
        # unmapped rather than guessing.
    },
}


def role_interest_tags(domain: str, role: str) -> list:
    """The subset of a domain's tags that actually relate to this role.
    Returns [] if nothing has been authored for this role."""
    return ROLE_INTEREST_TAGS.get(domain, {}).get(role, [])


def all_tags() -> list:
    """Flat list of every interest tag, in a stable order."""
    return [tag for tags in INTEREST_TAXONOMY.values() for tag in tags]


def tag_to_domain() -> dict:
    """{tag: parent_domain} lookup, used to build the coarse Domain feature."""
    return {
        tag: domain
        for domain, tags in INTEREST_TAXONOMY.items()
        for tag in tags
    }


if __name__ == "__main__":
    tags = all_tags()
    print(f"Interest domains: {len(INTEREST_TAXONOMY)}")
    print(f"Total tags: {len(tags)}")
    for domain, tags_in_domain in INTEREST_TAXONOMY.items():
        print(f"  {domain}: {len(tags_in_domain)} tags")
