
CAREER_TAXONOMY = {

    "Technology & Computing": {
        "expandable": False,  # already has full depth
        "roles": {
            "Software Developer": {
                "specializations": {
                    "Web Development": {
                        "technologies": ["JavaScript", "React", "Node.js", "HTML/CSS"],
                        "skills_required": {"technical_ability": 4, "problem_solving": 4,
                                             "creativity": 3},
                        "tools_required": {"git": 3, "web_frameworks": 3, "databases": 2},
                    },
                    "Mobile Development": {
                        "sub_specializations": {
                            "Android Native": {
                                "technologies": ["Kotlin", "Java", "Android SDK"],
                                "tools_required": {"git": 3, "kotlin": 3, "mobile_ui": 3},
                            },
                            "iOS Native": {
                                "technologies": ["Swift", "Xcode", "SwiftUI"],
                                "tools_required": {"git": 3, "swift": 3, "mobile_ui": 3},
                            },
                            "Cross-Platform": {
                                "technologies": ["Flutter", "Dart", "React Native", "JavaScript"],
                                "tools_required": {"git": 3, "dart_or_js": 3, "flutter_or_rn": 3},
                            },
                        },
                        "skills_required": {"technical_ability": 4, "problem_solving": 4,
                                             "creativity": 3},
                    },
                    "Backend Development": {
                        "technologies": ["Python", "Java", "Node.js", "SQL", "REST APIs"],
                        "skills_required": {"technical_ability": 4, "analytical_thinking": 4,
                                             "problem_solving": 4},
                        "tools_required": {"git": 3, "databases": 4, "api_design": 3},
                    },
                    "Full-Stack Development": {
                        "technologies": ["JavaScript", "React", "Node.js", "SQL"],
                        "skills_required": {"technical_ability": 4, "problem_solving": 4,
                                             "organization": 3},
                        "tools_required": {"git": 3, "web_frameworks": 3, "databases": 3},
                    },
                    "Cloud / DevOps": {
                        "technologies": ["Docker", "Kubernetes", "AWS/Azure", "CI/CD"],
                        "skills_required": {"technical_ability": 4, "analytical_thinking": 4,
                                             "organization": 4},
                        "tools_required": {"git": 4, "cloud_platforms": 4, "scripting": 3},
                    },
                },
            },
            "Data Scientist": {
                "specializations": {
                    "Machine Learning": {
                        "technologies": ["Python", "scikit-learn", "TensorFlow/PyTorch"],
                        "tools_required": {"python": 4, "statistics": 4, "ml_libraries": 4},
                    },
                    "Natural Language Processing": {
                        "technologies": ["Python", "spaCy/NLTK", "Transformers"],
                        "tools_required": {"python": 4, "statistics": 3, "nlp_libraries": 3},
                    },
                    "Computer Vision": {
                        "technologies": ["Python", "OpenCV", "PyTorch"],
                        "tools_required": {"python": 4, "statistics": 3, "cv_libraries": 3},
                    },
                    "Predictive Analytics": {
                        "technologies": ["Python/R", "SQL", "Pandas"],
                        "tools_required": {"python": 3, "statistics": 4, "sql": 3},
                    },
                },
                "skills_required": {"analytical_thinking": 5, "technical_ability": 4,
                                     "research": 4},
            },
            "Data Analyst": {
                "specializations": {
                    "Business Intelligence": {
                        "technologies": ["SQL", "Power BI/Tableau", "Excel"],
                        "tools_required": {"sql": 3, "visualization_tools": 3, "excel": 3},
                    },
                    "Data Visualization": {
                        "technologies": ["Python/R", "Tableau", "D3.js"],
                        "tools_required": {"visualization_tools": 4, "python": 2, "design_sense": 3},
                    },
                },
                "skills_required": {"analytical_thinking": 4, "organization": 3,
                                     "communication": 3},
            },
            "Cybersecurity Analyst": {
                "specializations": {
                    "Network Security": {
                        "technologies": ["Firewalls", "VPN", "IDS/IPS"],
                        "tools_required": {"networking": 4, "security_tools": 3},
                    },
                    "Application Security": {
                        "technologies": ["OWASP", "Static Analysis Tools"],
                        "tools_required": {"programming": 3, "security_tools": 4},
                    },
                    "Penetration Testing": {
                        "technologies": ["Kali Linux", "Metasploit", "Burp Suite"],
                        "tools_required": {"security_tools": 4, "scripting": 3},
                    },
                },
                "skills_required": {"analytical_thinking": 4, "problem_solving": 4,
                                     "technical_ability": 4},
            },
            "Network Engineer": {"skills_required": {"technical_ability": 5, "problem_solving": 4, "analytical_thinking": 3}},
            "IT Support Specialist": {"skills_required": {"communication": 5, "problem_solving": 4, "technical_ability": 4}},
            "Cloud / DevOps Engineer": {"skills_required": {"technical_ability": 5, "problem_solving": 4, "analytical_thinking": 3, "organization": 3}},
        },
    },

    "Finance & Business": {
        "expandable": False,
        "roles": {
            "Financial Analyst": {
                "specializations": {
                    "Investment Analysis": {
                        "technologies": ["Excel", "Bloomberg Terminal", "Financial Modeling"],
                        "tools_required": {"financial_modeling": 4, "excel": 4},
                    },
                    "Equity Research": {
                        "technologies": ["Excel", "Valuation Models", "Industry Research"],
                        "tools_required": {"financial_modeling": 4, "research_tools": 3},
                    },
                    "Corporate Finance": {
                        "technologies": ["Excel", "Budgeting Software", "SAP/ERP"],
                        "tools_required": {"financial_modeling": 3, "erp_systems": 3},
                    },
                    "Risk Analysis": {
                        "technologies": ["Excel", "Statistical Software", "Risk Models"],
                        "tools_required": {"statistics": 3, "financial_modeling": 3},
                    },
                },
                "skills_required": {"analytical_thinking": 4, "technical_ability": 2,
                                     "organization": 3},
            },
            "Marketing Manager": {
                "specializations": {
                    "Digital Marketing": {
                        "technologies": ["Google Ads", "SEO Tools", "Social Media Platforms"],
                        "tools_required": {"digital_tools": 3, "analytics": 3},
                    },
                    "Brand Management": {
                        "technologies": ["Brand Strategy Frameworks"],
                        "tools_required": {"design_sense": 2, "communication_tools": 3},
                    },
                    "Market Research": {
                        "technologies": ["Survey Tools", "Statistical Software"],
                        "tools_required": {"research_tools": 3, "statistics": 2},
                    },
                },
                "skills_required": {"creativity": 4, "communication": 4, "leadership": 3},
            },
            "Banking Officer": {"skills_required": {"communication": 5, "organization": 4, "analytical_thinking": 3}},
            "Chartered Accountant": {"skills_required": {"analytical_thinking": 5, "organization": 4, "problem_solving": 3}},
            "Business Analyst": {"skills_required": {"analytical_thinking": 5, "communication": 4, "problem_solving": 4}},
            "Entrepreneur": {"skills_required": {"problem_solving": 5, "creativity": 4, "leadership": 4}},
            "Human Resources Manager": {"skills_required": {"communication": 5, "organization": 4, "problem_solving": 3}},
            "Supply Chain Manager": {"skills_required": {"organization": 5, "problem_solving": 4, "analytical_thinking": 4}},
            "Insurance Agent": {"skills_required": {"communication": 5, "presentation": 4, "organization": 3}},
        },
    },

    "Design & Creative": {
        "expandable": False,
        "roles": {
            "UX/UI Designer": {
                "specializations": {
                    "UX Research": {
                        "technologies": ["User Interviews", "Usability Testing", "Surveys"],
                        "tools_required": {"research_tools": 4, "communication_tools": 3},
                    },
                    "Interaction Design": {
                        "technologies": ["Figma", "Prototyping Tools"],
                        "tools_required": {"design_software": 4, "prototyping": 4},
                    },
                    "Visual UI Design": {
                        "technologies": ["Figma", "Adobe XD", "Illustrator"],
                        "tools_required": {"design_software": 4, "visual_design": 4},
                    },
                    "Product Design": {
                        "technologies": ["Figma", "Design Systems"],
                        "tools_required": {"design_software": 3, "systems_thinking": 3},
                    },
                },
                "skills_required": {"creativity": 4, "communication": 4,
                                     "research": 3},
            },
            "Graphic Designer": {
                "skills_required": {"creativity": 4, "presentation": 3, "organization": 3},
            },
            "Video Editor": {"skills_required": {"creativity": 5, "technical_ability": 4, "organization": 3}},
            "Photographer": {"skills_required": {"creativity": 5, "technical_ability": 4, "communication": 3}},
        },
    },

    # ── The following domains are Role-level only for now — the
    # taxonomy is written so any of them can be deepened later the
    # same way the three above were, without touching this file's
    # structure. ──

    "Public Service & Law": {
        "expandable": True,
        "roles": {
            "Civil Servant (Loksewa)": {"skills_required": {"organization": 4, "communication": 4, "analytical_thinking": 3}}, "Police Officer": {"skills_required": {"problem_solving": 4, "communication": 3, "teamwork": 3}}, "Army Officer": {"skills_required": {"leadership": 5, "problem_solving": 3, "organization": 3}},
            "Diplomat / Foreign Affairs": {"skills_required": {"communication": 5, "analytical_thinking": 4, "research": 3}}, "Lawyer / Advocate": {"skills_required": {"analytical_thinking": 5, "research": 4, "communication": 4}}, "Legal Consultant": {"skills_required": {"analytical_thinking": 4, "research": 4, "communication": 3, "organization": 3}},
        },
    },
    "Education": {
        "expandable": True,
        "roles": {
            "School Teacher": {"skills_required": {"communication": 4, "organization": 3, "creativity": 3}}, "University Professor": {"skills_required": {"research": 5, "analytical_thinking": 4, "communication": 3}},
            "Education Counselor": {"skills_required": {"communication": 4, "problem_solving": 3, "organization": 3}}, "Instructional Designer": {"skills_required": {"organization": 4, "creativity": 4, "technical_ability": 3}},
        },
    },
    "Healthcare & Medicine": {
        "expandable": True,
        "roles": {
            "Medical Doctor": {"skills_required": {"analytical_thinking": 5, "problem_solving": 4, "communication": 4}}, "Public Health Officer": {"skills_required": {"analytical_thinking": 4, "research": 4, "communication": 3}},
            "Nurse": {
                "skills_required": {"communication": 4, "analytical_thinking": 4, "organization": 4},
            },
            "Pharmacist": {"skills_required": {"analytical_thinking": 5, "organization": 4, "communication": 3}}, "Dentist": {"skills_required": {"technical_ability": 5, "analytical_thinking": 4, "communication": 3}},
        },
    },
    "Engineering": {
        "expandable": True,
        "roles": {
            "Civil Engineer": {"skills_required": {"analytical_thinking": 4, "technical_ability": 4, "problem_solving": 4}}, "Electrical Engineer": {"skills_required": {"technical_ability": 5, "analytical_thinking": 4, "problem_solving": 4}}, "Mechanical Engineer": {"skills_required": {"technical_ability": 5, "analytical_thinking": 4, "creativity": 3}},
            "Environmental Engineer": {"skills_required": {"analytical_thinking": 4, "research": 4, "technical_ability": 3}}, "Architect": {"skills_required": {"creativity": 5, "technical_ability": 4, "communication": 3}},
        },
    },
    "Media & Communication": {
        "expandable": True,
        "roles": {
            "Journalist": {"skills_required": {"communication": 5, "research": 4, "analytical_thinking": 3, "organization": 3}}, "Content Creator": {"skills_required": {"creativity": 5, "communication": 4, "technical_ability": 3}},
            "Radio/TV Presenter": {"skills_required": {"communication": 5, "presentation": 5, "creativity": 3}}, "Social Media Strategist": {"skills_required": {"analytical_thinking": 4, "organization": 4, "communication": 4, "creativity": 3}},
        },
    },
    "Agriculture & Environment": {
        "expandable": True,
        "roles": {
            "Agricultural Scientist": {"skills_required": {"research": 4, "analytical_thinking": 4, "problem_solving": 3, "communication": 3}}, "Veterinary Doctor": {"skills_required": {"problem_solving": 4, "technical_ability": 4, "communication": 3}}, "Environmental Scientist": {"skills_required": {"research": 4, "analytical_thinking": 4, "problem_solving": 3}},
        },
    },
    "Hospitality & Tourism": {
        "expandable": True,
        "roles": {
            "Hotel Manager": {"skills_required": {"leadership": 5, "organization": 5, "communication": 4, "problem_solving": 3}}, "Tour Guide": {"skills_required": {"communication": 5, "presentation": 4, "organization": 3}}, "Chef / Culinary Artist": {"skills_required": {"technical_ability": 5, "creativity": 4, "organization": 3}}, "Event Planner": {"skills_required": {"organization": 5, "problem_solving": 4, "communication": 4}},
        },
    },
    "Social Work & Community": {
        "expandable": True,
        "roles": {
            "Social Worker": {}, "NGO Program Officer": {"skills_required": {"organization": 4, "communication": 4, "research": 3}}, "Psychologist": {"skills_required": {"research": 5, "analytical_thinking": 5, "communication": 4}},
        },
    },
    "Research & Science": {
        "expandable": True,
        "roles": {
            "Research Scientist": {"skills_required": {"research": 5, "analytical_thinking": 5, "problem_solving": 4, "technical_ability": 3}}, "Geologist": {"skills_required": {"analytical_thinking": 4, "research": 4, "technical_ability": 4}}, "Lab Technician": {"skills_required": {"technical_ability": 5, "organization": 4, "analytical_thinking": 3}},
        },
    },
    "Sports & Fitness": {
        "expandable": True,
        "roles": {
            "Sports Coach": {"skills_required": {"leadership": 5, "communication": 4, "teamwork": 3}}, "Fitness Trainer": {"skills_required": {"technical_ability": 4, "communication": 4, "problem_solving": 3}}, "Sports Analyst": {"skills_required": {"analytical_thinking": 5, "research": 4, "technical_ability": 3}}, "Athlete": {"skills_required": {"technical_ability": 5, "organization": 4, "problem_solving": 3}},
        },
    },
}


def flatten_roles():
    """Return [(domain, role), ...] for every role in the taxonomy."""
    return [
        (domain, role)
        for domain, ddata in CAREER_TAXONOMY.items()
        for role in ddata["roles"]
    ]


def flatten_specializations():
    """Return [(domain, role, specialization), ...] for every leaf specialization
    (sub_specializations, if present, are expanded too)."""
    out = []
    for domain, ddata in CAREER_TAXONOMY.items():
        for role, rdata in ddata["roles"].items():
            for spec, sdata in rdata.get("specializations", {}).items():
                if "sub_specializations" in sdata:
                    for sub in sdata["sub_specializations"]:
                        out.append((domain, role, f"{spec} — {sub}"))
                else:
                    out.append((domain, role, spec))
    return out


if __name__ == "__main__":
    roles = flatten_roles()
    specs = flatten_specializations()
    print(f"Domains: {len(CAREER_TAXONOMY)}")
    print(f"Roles: {len(roles)}")
    print(f"Specializations (leaf-level, incl. sub-specializations): {len(specs)}")
    for domain, role, spec in specs:
        print(f"  {domain} -> {role} -> {spec}")
