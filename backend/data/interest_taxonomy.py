
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
     
        "Sports Coach": ["Coaching"],
        "Sports Analyst": ["Sports Analytics", "Sports Journalism"],
        "Athlete": ["Football", "Cricket", "Swimming", "Esports"],
    
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
