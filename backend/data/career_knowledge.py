# =============================================================
# backend/data/career_knowledge.py
# =============================================================
# PURPOSE:
#   Curated career guidance -- descriptions, activities, strengths,
#   work settings, and roadmap content -- kept DELIBERATELY SEPARATE
#   from the synthetic ML dataset (see modules/roadmap.py's design
#   note and skill_gap.py's "career_profile vs dataset_pattern" split
#   for the same separation applied to numeric skill targets).
#
#   This file answers "what does this job actually involve and how
#   would someone prepare for it" -- content a Random Forest trained
#   on synthetic rows has no way to know. It is hand-authored career
#   guidance, not a statistically derived requirement, and every
#   description here should read that way: "recommended skill
#   profile," "useful skills," "common tools," "suggested
#   preparation" -- never "proven requirement" or "guaranteed path."
#
#   Complements career_taxonomy.py rather than duplicating it:
#   career_taxonomy.py owns the STRUCTURE (domain -> role ->
#   specialization -> technologies) and numeric skills_required /
#   tools_required used by skill_gap.py. This file owns the
#   NARRATIVE layer -- description, activities, project ideas,
#   work settings, roadmap phase content -- keyed the same way.
#
#   Coverage: fully authored for 6 roles spanning very different
#   fields (Social Worker, Data Analyst, Graphic Designer, Software
#   Developer with two specialization overrides, Financial Analyst,
#   Nurse as a regulated-career example). Not every role in
#   career_taxonomy.py has an entry yet -- callers must fall back
#   gracefully (see roadmap.py's GENERIC_FALLBACK) rather than
#   assume every role is covered.
# =============================================================

# Roles that require formal licensed education/clinical training --
# the roadmap must never imply that completing it makes someone
# qualified to practice, and must say so explicitly.
REGULATED_ROLES = {
    ("Healthcare & Medicine", "Nurse"),
    ("Healthcare & Medicine", "Medical Doctor"),
    ("Healthcare & Medicine", "Pharmacist"),
    ("Healthcare & Medicine", "Dentist"),
    ("Public Service & Law", "Lawyer / Advocate"),
    ("Finance & Business", "Chartered Accountant"),
    ("Engineering", "Architect"),
}

CAREER_KNOWLEDGE = {

    ("Social Work & Community", "Social Worker"): {
        "description": (
            "Social workers support individuals, families, and communities dealing with "
            "social, educational, health, or economic challenges. The work often involves "
            "listening, assessing needs, connecting people with services, and coordinating "
            "support across schools, health systems, and community organizations."
        ),
        "typical_activities": [
            "Meeting individuals and families to understand their situation",
            "Assessing community or household needs",
            "Coordinating support services across organizations",
            "Maintaining case records and documentation",
            "Working with schools, NGOs, or local government institutions",
        ],
        "useful_strengths": ["communication", "teamwork", "organization", "problem_solving"],
        "critical_skills": ["communication", "teamwork", "organization", "problem_solving"],
        "skill_importance": {"communication": 1.0, "teamwork": 0.85,
                              "organization": 0.75, "problem_solving": 0.65},
        "useful_academic_areas": ["English", "Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 5, "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 3.5, "pref_structured_vs_flexible": 3.5,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 5,
        },
        "work_settings": ["NGOs / INGOs", "Schools", "Community organizations",
                           "Local government", "Hospitals", "Social service organizations"],
        "possible_directions": ["Community Development", "Child & Family Services",
                                 "School Social Work", "Public Health Outreach"],
        "foundational_topics": [
            "How community, school, health, and NGO social-work settings differ",
            "A few simple real-world social/community case examples",
            "The range of directions inside social work, before narrowing down",
        ],
        "field_methods": [
            "Needs assessment basics",
            "Structured case documentation",
            "Interview and questionnaire design",
            "Simple community mapping",
            "Clear, factual report writing",
        ],
        "tools_context": ["Google Forms (for simple surveys)", "Google Sheets / Excel (for records)",
                           "Basic document tools for reports"],
        "project_ideas": ["Awareness campaign plan for a local issue", "Community resource map"],
        "project": {
            "title": "Small Community Needs Assessment",
            "steps": [
                "Choose one simple, local community issue to look at",
                "Prepare 5-10 clear questions about it",
                "Gather responses respectfully and appropriately",
                "Organize what you found into themes",
                "Identify the 2-3 needs that came up most often",
                "Write a short report summarizing findings",
                "Suggest a few possible responses or next steps",
            ],
        },
        "education_preparation": (
            "Many social workers study social work, sociology, or a related social-science "
            "field, though people enter from varied backgrounds. Volunteer or field experience "
            "matters as much as coursework for this path."
        ),
        "experience_ideas": {
            "+2 / High School": ["Volunteer with a local community or youth organization",
                                  "Talk to someone who works in social work about their day-to-day"],
            "Bachelor": ["Volunteer with an NGO on a specific project",
                         "Look for a structured internship or field-placement opportunity"],
            "Master": ["Seek a supervised field placement in a specific specialization",
                       "Take on a small applied research or program-evaluation project"],
        },
    },

    ("Technology & Computing", "Data Analyst"): {
        "description": (
            "Data analysts turn raw data into information people can act on. The work "
            "involves cleaning messy data, looking for patterns, and communicating what "
            "the numbers mean in a way that non-technical people can use to make decisions."
        ),
        "typical_activities": [
            "Cleaning and organizing raw data",
            "Writing queries to pull the data you need",
            "Building charts, dashboards, and summary reports",
            "Looking for patterns and explaining what they might mean",
            "Presenting findings to people who aren't data specialists",
        ],
        "useful_strengths": ["analytical_thinking", "organization", "communication", "research"],
        "critical_skills": ["analytical_thinking", "organization", "communication", "technical_ability"],
        "skill_importance": {"analytical_thinking": 1.0, "technical_ability": 0.85,
                              "organization": 0.7, "communication": 0.6},
        "useful_academic_areas": ["Mathematics", "Computer", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 2.5, "pref_creative_vs_analytical": 1.5,
            "pref_indoor_vs_outdoor": 1.5, "pref_structured_vs_flexible": 2.5,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 2,
        },
        "work_settings": ["Tech companies", "Banks & financial firms", "NGOs / research organizations",
                           "Government data units", "Any company with a data/BI team"],
        "possible_directions": ["Business Intelligence", "Data Visualization",
                                 "Moving toward Data Science over time"],
        "foundational_topics": [
            "Basic statistics (mean, median, distributions, correlation vs causation)",
            "How spreadsheets model data (rows, columns, pivot tables)",
            "What \"clean\" vs \"messy\" data actually means",
        ],
        "field_methods": [
            "Data cleaning workflows",
            "Writing and reading SQL queries",
            "Choosing the right chart for the question you're answering",
            "Structuring a short, clear insight report",
        ],
        "tools_context": ["Excel / Google Sheets", "SQL", "Power BI or Tableau",
                           "Python with Pandas (once comfortable with the basics)"],
        "project_ideas": ["Build an interactive dashboard", "Prepare a data insight report"],
        "project": {
            "title": "Public Dataset Dashboard",
            "steps": [
                "Find a public dataset you're genuinely curious about",
                "Clean and organize it in a spreadsheet or SQL",
                "Identify 3-4 interesting questions the data can answer",
                "Build a simple dashboard or set of charts",
                "Write a short summary of your key findings",
            ],
        },
        "education_preparation": (
            "Common entry paths include statistics, computer science, economics, or business "
            "degrees, but many analysts build skills through self-study and practice (SQL, "
            "Excel, small projects) — a strong portfolio often matters as much as the degree title."
        ),
        "experience_ideas": {
            "+2 / High School": ["Try a free beginner Excel or SQL course",
                                  "Explore a public dataset just to see what's in it"],
            "Bachelor": ["Look for a data/analytics internship",
                         "Contribute to a small open-data or student research project"],
            "Master": ["Take on a research assistantship involving real data work",
                       "Build a portfolio case study from a real or public dataset"],
        },
    },

    ("Design & Creative", "Graphic Designer"): {
        "description": (
            "Graphic designers communicate ideas visually -- through layout, color, "
            "typography, and imagery -- for things like branding, posters, social media, "
            "and digital products. The work blends creative judgment with practical "
            "constraints like audience, medium, and message."
        ),
        "typical_activities": [
            "Sketching and iterating on visual concepts",
            "Choosing typography, color, and layout for a piece of communication",
            "Preparing designs for print or digital use",
            "Getting and responding to feedback from clients or teams",
            "Building and maintaining a consistent visual style across a project",
        ],
        "useful_strengths": ["creativity", "communication", "organization", "presentation"],
        "critical_skills": ["creativity", "presentation", "communication", "organization"],
        "skill_importance": {"creativity": 1.0, "presentation": 0.85,
                              "communication": 0.65, "organization": 0.5},
        "useful_academic_areas": ["Arts", "Computer", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 4.5,
            "pref_indoor_vs_outdoor": 1.5, "pref_structured_vs_flexible": 3.5,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 2.5,
        },
        "work_settings": ["Design agencies", "In-house marketing/brand teams", "Freelance/client work",
                           "Publishing & media", "Startups needing brand/product visuals"],
        "possible_directions": ["Brand & identity design", "UI visual design",
                                 "Illustration-led design", "Motion/social content design"],
        "foundational_topics": [
            "Visual hierarchy -- guiding the eye through a layout",
            "Color theory basics",
            "Typography fundamentals",
            "Composition and balance",
        ],
        "field_methods": [
            "Building a mood board before starting a design",
            "Iterating through several rough concepts before refining one",
            "Presenting design decisions, not just the final image",
        ],
        "tools_context": ["Figma", "Adobe Illustrator or a free alternative (Inkscape, Canva for basics)"],
        "project_ideas": ["Poster campaign for an event", "Social media visual system"],
        "project": {
            "title": "Fictional Local Brand Identity",
            "steps": [
                "Invent a simple fictional local business (a cafe, shop, or event)",
                "Define its personality in a few words (e.g. \"warm, simple, local\")",
                "Design a logo and a small color/type system for it",
                "Apply it to 2-3 real-world formats (a poster, a social post, a sign)",
                "Write a short case study explaining your design choices",
            ],
        },
        "education_preparation": (
            "A design, fine arts, or visual communication background helps, but a strong "
            "portfolio of real work usually matters more to employers and clients than the "
            "specific degree title."
        ),
        "experience_ideas": {
            "+2 / High School": ["Redesign a poster or flyer for a school event, just for practice",
                                  "Start a small sketchbook or digital portfolio folder"],
            "Bachelor": ["Design for a college club, event, or student publication",
                         "Take on a small volunteer design project for a local organization"],
            "Master": ["Build a focused portfolio around one design direction",
                       "Seek a design internship or small freelance client project"],
        },
    },

    ("Technology & Computing", "Software Developer"): {
        "description": (
            "Software developers design, build, and maintain applications -- websites, "
            "mobile apps, or the systems behind them. The work involves breaking a "
            "problem into logical steps, writing and testing code, and continuously "
            "learning as tools and requirements change."
        ),
        "typical_activities": [
            "Breaking a feature or problem down into smaller coding tasks",
            "Writing, testing, and debugging code",
            "Reading other people's code and documentation",
            "Using version control to track and share changes",
            "Fixing bugs reported by users or teammates",
        ],
        "useful_strengths": ["technical_ability", "problem_solving", "analytical_thinking", "organization"],
        "critical_skills": ["technical_ability", "problem_solving", "analytical_thinking"],
        "skill_importance": {"technical_ability": 1.0, "problem_solving": 0.9,
                              "analytical_thinking": 0.7, "organization": 0.5},
        "useful_academic_areas": ["Computer", "Mathematics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 2, "pref_creative_vs_analytical": 2.5,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 1.5,
        },
        "work_settings": ["Software companies & startups", "IT departments", "Freelance/contract work",
                           "Remote-first companies"],
        "possible_directions": ["Web Development", "Mobile Development", "Backend Development",
                                 "Full-Stack Development", "Cloud / DevOps"],
        "foundational_topics": [
            "How programs are structured (variables, functions, control flow)",
            "The difference between frontend, backend, and how they connect",
            "Reading error messages and debugging systematically",
        ],
        "field_methods": [
            "Version control workflows (branches, commits, pull requests)",
            "Breaking a feature into small, testable pieces",
            "Basic testing practices before considering something \"done\"",
        ],
        "tools_context": ["Git & GitHub", "A code editor (VS Code)"],
        "project_ideas": ["Build a REST API for a small idea", "Create and deploy a portfolio project"],
        "project": {
            "title": "Small Working Application",
            "steps": [
                "Pick a small, real problem you'd actually use a solution for",
                "Plan the 2-3 core features it needs -- nothing more",
                "Build a working version, even if it's rough",
                "Test it yourself and fix the obvious issues",
                "Deploy it somewhere it can actually be used or viewed",
            ],
        },
        "education_preparation": (
            "Computer science or a related technical degree is common, but many developers "
            "are self-taught or bootcamp-trained — demonstrated ability (working projects, "
            "code you can explain) tends to matter more than the credential itself."
        ),
        "experience_ideas": {
            "+2 / High School": ["Work through a free intro programming course",
                                  "Build a tiny personal project just to practice"],
            "Bachelor": ["Contribute to an open-source project or a friend's project",
                        "Look for a development internship"],
            "Master": ["Build a more substantial portfolio project in your specialization",
                      "Seek an internship or research role with real engineering exposure"],
        },
        # Specialization-level overrides, merged on top of the role-level
        # content above when the student has picked a specialization.
        "specializations": {
            "Mobile Development": {
                "description": (
                    "Mobile developers build apps that run on phones and tablets -- "
                    "designing for touch, small screens, and platform-specific behavior, "
                    "whether targeting one platform natively or both with one codebase."
                ),
                "foundational_topics": [
                    "How mobile apps differ from websites (lifecycle, offline behavior, permissions)",
                    "Mobile UI/UX conventions (navigation patterns, touch targets)",
                    "Choosing native (Kotlin/Swift) vs. cross-platform (Flutter/React Native)",
                ],
                "tools_context": ["Git", "Flutter or React Native (cross-platform) "
                                   "OR Kotlin/Swift (native)"],
                "project": {
                    "title": "Small Cross-Platform Mobile App",
                    "steps": [
                        "Pick one simple, useful idea (a tracker, list, or small tool)",
                        "Design 2-3 core screens on paper first",
                        "Build it in Flutter or React Native",
                        "Test it on an actual device or emulator",
                        "Package and share it (even informally) for real feedback",
                    ],
                },
            },
            "Backend Development": {
                "description": (
                    "Backend developers build the systems behind an application -- "
                    "servers, databases, and APIs -- that power what users see on the "
                    "frontend. The work leans more on data structure, performance, and "
                    "reliability than on visual design."
                ),
                "foundational_topics": [
                    "How client-server communication works (requests, responses, APIs)",
                    "Database basics (tables, relationships, queries)",
                    "Designing a simple REST API",
                ],
                "tools_context": ["Git", "A backend language (Python/Node.js/Java)", "SQL databases"],
                "project": {
                    "title": "Small API-Backed Service",
                    "steps": [
                        "Design a simple data model for a small idea (e.g. a to-do or notes API)",
                        "Build the database and a REST API around it",
                        "Add basic validation and error handling",
                        "Test the API with a tool like Postman",
                        "Write short documentation for how to use it",
                    ],
                },
            },
        },
    },

    ("Finance & Business", "Financial Analyst"): {
        "description": (
            "Financial analysts study financial data -- company statements, market "
            "trends, budgets -- to support business or investment decisions. The work "
            "combines careful, structured analysis with clear written and verbal "
            "communication of what the numbers mean."
        ),
        "typical_activities": [
            "Reviewing financial statements and reports",
            "Building spreadsheet models to project outcomes",
            "Comparing performance across time periods or companies",
            "Researching market or industry context",
            "Presenting findings and recommendations",
        ],
        "useful_strengths": ["analytical_thinking", "organization", "research", "presentation"],
        "critical_skills": ["analytical_thinking", "organization", "research"],
        "skill_importance": {"analytical_thinking": 1.0, "organization": 0.8,
                              "research": 0.7, "presentation": 0.55},
        "useful_academic_areas": ["Mathematics", "Business/Economics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 2.5, "pref_creative_vs_analytical": 1.5,
            "pref_indoor_vs_outdoor": 1.5, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 2.5, "pref_tech_vs_people": 2.5,
        },
        "work_settings": ["Banks", "Investment firms", "Corporate finance teams",
                           "Consulting firms", "Insurance companies"],
        "possible_directions": ["Investment Analysis", "Equity Research",
                                 "Corporate Finance", "Risk Analysis"],
        "foundational_topics": [
            "Accounting basics (what a balance sheet and income statement actually show)",
            "How to read a company's financial statements",
            "Core business fundamentals (revenue, margin, growth)",
        ],
        "field_methods": [
            "Ratio analysis (comparing key financial ratios)",
            "Building a simple spreadsheet financial model",
            "Structuring a short analysis or recommendation report",
        ],
        "tools_context": ["Excel (advanced formulas, pivot tables)", "Basic spreadsheet modeling"],
        "project_ideas": ["Build a simple financial model", "Compare two companies' performance"],
        "project": {
            "title": "Company Financial Statement Analysis",
            "steps": [
                "Pick a public company whose reports are freely available",
                "Read through its most recent annual financial statements",
                "Calculate a handful of key ratios (profitability, liquidity, growth)",
                "Compare them to a competitor or to the prior year",
                "Write a short analysis with your observations and questions",
            ],
        },
        "education_preparation": (
            "A finance, accounting, business, or economics degree is the most common path. "
            "Professional certifications (like the CFA) are typically pursued later in a "
            "career, not required to start exploring this field."
        ),
        "experience_ideas": {
            "+2 / High School": ["Take a free intro accounting or finance course",
                                  "Follow financial news for a company you're curious about"],
            "Bachelor": ["Look for a finance/accounting internship",
                        "Join a student investment or finance club if available"],
            "Master": ["Seek an analyst internship with real modeling work",
                      "Build a small independent equity research write-up as a portfolio piece"],
        },
    },

    ("Healthcare & Medicine", "Nurse"): {
        "description": (
            "Nurses provide direct patient care -- monitoring health, administering "
            "treatment, and supporting patients and families -- working closely with "
            "doctors and other health professionals. Nursing is a licensed clinical "
            "profession: this roadmap is about exploring and preparing for that path, "
            "not a substitute for the required formal education and clinical training."
        ),
        "typical_activities": [
            "Monitoring patients' condition and recording observations",
            "Assisting with treatments and procedures under clinical protocols",
            "Communicating clearly with patients, families, and the care team",
            "Following strict hygiene, safety, and documentation standards",
            "Responding calmly and accurately in time-sensitive situations",
        ],
        "useful_strengths": ["communication", "analytical_thinking", "problem_solving", "organization"],
        "critical_skills": ["communication", "analytical_thinking", "organization"],
        "skill_importance": {"communication": 1.0, "analytical_thinking": 0.85,
                              "organization": 0.7, "problem_solving": 0.6},
        "useful_academic_areas": ["Science", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 4.5, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1.5, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 4.5,
        },
        "work_settings": ["Hospitals", "Clinics", "Community health centers", "Public health programs"],
        "possible_directions": ["General/ward nursing", "Community & public health nursing",
                                 "Pediatric care", "Critical/emergency care (with further training)"],
        "foundational_topics": [
            "What day-to-day nursing work actually involves across different settings",
            "The formal education path required (a recognized nursing degree/diploma "
            "and licensing exam) -- this varies by country and must be confirmed locally",
            "Basic human biology and health literacy as background reading",
        ],
        "field_methods": [
            "Careful observation and accurate record-keeping",
            "Clear, calm communication under pressure",
            "Following structured protocols exactly, not improvising",
        ],
        "tools_context": [],
        "project_ideas": ["Research accredited nursing programs in your region",
                           "Summarize basic health/hygiene guidance for a community"],
        "project": None,  # deliberately no "build a project" step for a clinical, licensed field
        "education_preparation": (
            "Nursing requires completing an accredited nursing degree or diploma program and "
            "passing the relevant licensing/registration exam — exact requirements vary by "
            "country and must be confirmed locally. This roadmap supports exploration and "
            "preparation only, not a substitute for that formal, supervised training."
        ),
        "experience_ideas": {
            "+2 / High School": ["Research accredited nursing programs and their entry requirements",
                                  "Talk to a working nurse about their day-to-day experience",
                                  "Volunteer in a non-clinical support role at a health facility if possible"],
            "Bachelor": ["Confirm you're enrolled in (or applying to) an accredited nursing program",
                        "Focus on your program's supervised clinical placements -- that structured "
                        "training is what actually builds clinical competence, not this roadmap"],
            "Master": ["Consider a specialization track (e.g. pediatric, critical care) through "
                      "formal advanced study", "Look for structured clinical or research exposure "
                      "in your area of interest"],
        },
    },
    # --- from group1_tech_design.py ---
    ("Technology & Computing", "Data Scientist"): {
        "description": (
            "Data scientists use statistics and machine learning to find patterns in data "
            "and build models that predict or explain outcomes. The work involves more "
            "experimentation and model-building than standard data analysis, along with "
            "explaining uncertain, probabilistic results to people who need to make decisions."
        ),
        "typical_activities": [
            "Formulating a testable question from a vague business or research problem",
            "Cleaning messy data and engineering useful features from it",
            "Building, training, and validating statistical or machine learning models",
            "Designing and interpreting experiments such as A/B tests",
            "Communicating model results and their limitations to non-technical stakeholders",
            "Handing off or deploying models for others to use in production",
        ],
        "useful_strengths": ["analytical_thinking", "problem_solving", "research", "technical_ability", "communication"],
        "critical_skills": ["analytical_thinking", "problem_solving", "technical_ability", "research", "communication"],
        "skill_importance": {
            "analytical_thinking": 1.0,
            "problem_solving": 0.9,
            "technical_ability": 0.85,
            "research": 0.7,
            "communication": 0.6,
        },
        "useful_academic_areas": ["Mathematics", "Computer", "Science"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 1.5,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 2,
        },
        "work_settings": ["Tech companies", "Research labs", "Banking & finance analytics teams",
                           "E-commerce companies", "Healthcare data teams"],
        "possible_directions": ["Machine Learning Engineering", "NLP / Computer Vision",
                                 "Applied Research", "Business & Product Analytics"],
        "foundational_topics": ["Statistics & probability", "Python or R programming",
                                 "Linear algebra basics", "Machine learning fundamentals"],
        "field_methods": ["Hypothesis testing", "Experimental design (A/B testing)",
                           "Exploratory data analysis", "Peer review of methodology"],
        "tools_context": ["Python (Pandas, scikit-learn)", "SQL", "Jupyter notebooks",
                           "Visualization libraries", "Cloud ML platforms (optional)"],
        "project_ideas": [
            "Build a predictive model from a public dataset",
            "Design and simulate a simple A/B test",
            "Create an end-to-end mini ML pipeline",
        ],
        "project": {
            "title": "Predictive Model From a Public Dataset",
            "steps": [
                "Choose a public dataset with a clear prediction target",
                "Clean the data and engineer a few relevant features",
                "Split into training and test sets and try 2-3 modeling approaches",
                "Evaluate the models with appropriate metrics and compare them",
                "Write up findings, including where the model performs poorly",
                "Optionally wrap the best model in a notebook or script others can rerun",
            ],
        },
        "education_preparation": (
            "Most data scientists come from math, statistics, computer science, or another "
            "quantitative field, but a portfolio of real analysis and modeling projects often "
            "matters as much as the degree title, and many people enter through self-directed "
            "learning combined with demonstrated project work."
        ),
        "experience_ideas": {
            "+2 / High School": ["Take an intro statistics or Python course online",
                                  "Try a beginner-friendly data analysis challenge or competition"],
            "Bachelor": ["Do a data science or analytics internship",
                         "Complete an end-to-end project on a public dataset for a portfolio"],
            "Master": ["Take on a research assistantship involving real modeling work",
                       "Present or publish an applied data science project"],
        },
    },

    ("Technology & Computing", "Cybersecurity Analyst"): {
        "description": (
            "Cybersecurity analysts monitor systems for security threats, investigate "
            "incidents, and help organizations reduce their exposure to attacks. The work "
            "mixes technical monitoring tools with careful documentation and judgment calls "
            "about how serious a given risk actually is."
        ),
        "typical_activities": [
            "Monitoring security alerts and system logs for suspicious activity",
            "Investigating and responding to security incidents",
            "Running vulnerability scans and recommending fixes",
            "Reviewing access controls and security policies",
            "Documenting incidents and writing security reports",
            "Tracking new threats and attack techniques as they emerge",
        ],
        "useful_strengths": ["analytical_thinking", "technical_ability", "problem_solving", "organization", "research"],
        "critical_skills": ["analytical_thinking", "technical_ability", "problem_solving", "organization", "research"],
        "skill_importance": {
            "analytical_thinking": 1.0,
            "technical_ability": 0.9,
            "problem_solving": 0.85,
            "organization": 0.6,
            "research": 0.55,
        },
        "useful_academic_areas": ["Computer", "Mathematics", "Science"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 1.5,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2.5,
            "pref_handson_vs_theoretical": 3.5,
            "pref_tech_vs_people": 1.5,
        },
        "work_settings": ["Corporate IT/security teams", "Banks & financial institutions",
                           "Government agencies", "Managed security service providers",
                           "Any organization handling sensitive data"],
        "possible_directions": ["Incident Response", "Penetration Testing",
                                 "Security Operations (SOC)", "Governance, Risk & Compliance"],
        "foundational_topics": ["Networking fundamentals", "Operating system security basics",
                                 "Common attack types (phishing, malware, etc.)", "Basic scripting"],
        "field_methods": ["Threat & vulnerability assessment", "Log analysis",
                           "Incident response procedures", "Security audits"],
        "tools_context": ["SIEM / log monitoring platforms", "Vulnerability scanners",
                           "Firewall & endpoint protection dashboards", "Basic scripting (Python/Bash)"],
        "project_ideas": [
            "Set up a home lab and simulate a basic attack",
            "Complete a beginner capture-the-flag challenge",
            "Write a security policy for a sample small company",
        ],
        "project": {
            "title": "Home Lab Security Monitoring Setup",
            "steps": [
                "Set up a small virtual lab with two or three machines",
                "Install basic monitoring and logging on the lab machines",
                "Simulate a simple attack, such as repeated failed logins or a port scan",
                "Practice identifying that activity in the logs",
                "Document what happened and how you would respond",
                "Write a short incident report summarizing the exercise",
            ],
        },
        "education_preparation": (
            "Many cybersecurity analysts start with a computer science or IT background, but "
            "the field is unusually open to people who build hands-on skill through labs, "
            "capture-the-flag challenges, and industry certifications rather than a specific "
            "degree; demonstrated practical ability tends to carry real weight."
        ),
        "experience_ideas": {
            "+2 / High School": ["Try a beginner cybersecurity awareness course",
                                  "Play beginner-level capture-the-flag (CTF) challenges"],
            "Bachelor": ["Set up a home lab and practice basic attack/defense scenarios",
                         "Look for a security or IT internship with exposure to monitoring tools"],
            "Master": ["Work through a focused incident-response simulation project",
                       "Seek an internship or assistantship in a security operations team"],
        },
    },

    ("Technology & Computing", "Network Engineer"): {
        "description": (
            "Network engineers design, build, and maintain the infrastructure that lets "
            "computers and devices communicate, including routers, switches, firewalls, and "
            "wireless systems. The work involves both planning network architecture ahead of "
            "time and troubleshooting connectivity problems when they come up."
        ),
        "typical_activities": [
            "Designing and configuring network infrastructure such as routers and switches",
            "Monitoring network performance and uptime",
            "Troubleshooting connectivity and performance issues",
            "Setting up and maintaining wireless networks",
            "Documenting network architecture and configurations",
            "Planning capacity for network growth",
        ],
        "useful_strengths": ["technical_ability", "problem_solving", "analytical_thinking", "organization", "communication"],
        "critical_skills": ["technical_ability", "problem_solving", "analytical_thinking", "organization", "communication"],
        "skill_importance": {
            "technical_ability": 1.0,
            "problem_solving": 0.9,
            "analytical_thinking": 0.75,
            "organization": 0.55,
            "communication": 0.5,
        },
        "useful_academic_areas": ["Computer", "Mathematics", "Science"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 1.5,
        },
        "work_settings": ["Corporate IT departments", "Internet service providers",
                           "Data centers", "Educational institutions", "Government offices"],
        "possible_directions": ["Network Security", "Cloud Networking",
                                 "Wireless & Telecom Systems", "Network Architecture"],
        "foundational_topics": ["TCP/IP and networking fundamentals", "Routing & switching concepts",
                                 "Network security basics", "Common protocols (DNS, DHCP, HTTP)"],
        "field_methods": ["Network diagramming", "Cable and hardware installation",
                           "Performance testing", "Structured troubleshooting"],
        "tools_context": ["Router/switch configuration interfaces (e.g., Cisco IOS)",
                           "Network monitoring software", "Packet analysis tools (e.g., Wireshark)",
                           "Basic scripting for automation"],
        "project_ideas": [
            "Build a small home lab network",
            "Map and document an existing network",
            "Simulate network troubleshooting scenarios",
        ],
        "project": {
            "title": "Small Office Network Simulation",
            "steps": [
                "Use free network simulation software such as Cisco Packet Tracer",
                "Design a simple network layout for a small office with a few devices",
                "Configure basic routing and a wireless access point",
                "Set up basic security rules such as firewall or access rules",
                "Test connectivity between devices and troubleshoot issues you introduce",
                "Document the network design and the configuration choices you made",
            ],
        },
        "education_preparation": (
            "Network engineers commonly come from computer science, IT, or telecommunications "
            "backgrounds, though many build core skill through hands-on labs and vendor-aligned "
            "certifications; being able to actually configure and troubleshoot real equipment "
            "matters at least as much as the degree title."
        ),
        "experience_ideas": {
            "+2 / High School": ["Set up and troubleshoot a home Wi-Fi network",
                                  "Try a free network simulator to build a basic topology"],
            "Bachelor": ["Pursue an IT or networking internship",
                         "Build a home lab with used or budget networking equipment"],
            "Master": ["Take on a networking-focused capstone or research project",
                       "Seek an internship involving enterprise network design"],
        },
    },

    ("Technology & Computing", "IT Support Specialist"): {
        "description": (
            "IT support specialists help people solve everyday technology problems, from "
            "broken software and hardware issues to account access and connectivity. Much of "
            "the work is direct interaction with users who are frustrated or non-technical, "
            "combined with systematic troubleshooting, often under time pressure."
        ),
        "typical_activities": [
            "Responding to help desk tickets and support requests",
            "Diagnosing and fixing hardware and software issues",
            "Setting up new devices, accounts, and software for users",
            "Walking non-technical users through solutions step by step",
            "Escalating complex issues to specialized teams",
            "Maintaining equipment inventory and basic documentation",
        ],
        "useful_strengths": ["communication", "problem_solving", "technical_ability", "organization", "teamwork"],
        "critical_skills": ["communication", "problem_solving", "technical_ability", "organization", "teamwork"],
        "skill_importance": {
            "communication": 1.0,
            "problem_solving": 0.9,
            "technical_ability": 0.8,
            "organization": 0.55,
            "teamwork": 0.45,
        },
        "useful_academic_areas": ["Computer", "English", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 4,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2.5,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Corporate IT help desks", "Schools & universities",
                           "Retail & electronics stores", "Managed service providers",
                           "Government offices"],
        "possible_directions": ["Systems Administration", "Network Support",
                                 "IT Service Management", "moving toward Cybersecurity or Cloud roles"],
        "foundational_topics": ["Operating systems basics (Windows/Mac/Linux)",
                                 "Common hardware troubleshooting", "Basic networking concepts",
                                 "Customer service fundamentals"],
        "field_methods": ["Structured troubleshooting steps", "Ticket triage & prioritization",
                           "Remote desktop support", "Basic hardware diagnostics"],
        "tools_context": ["Ticketing / helpdesk software", "Remote support tools",
                           "Basic OS administration tools", "Diagnostic utilities"],
        "project_ideas": [
            "Build a personal tech troubleshooting guide",
            "Set up and configure a small computer lab",
            "Practice remote support scenarios with a friend",
        ],
        "project": {
            "title": "Personal Tech Support Playbook",
            "steps": [
                "List 10-15 common tech problems people run into, such as Wi-Fi or printer issues",
                "Research and write clear step-by-step solutions for each one",
                "Test the steps on a real device or a willing volunteer",
                "Organize the guide by category and difficulty",
                "Practice walking someone through one issue without touching their device yourself",
                "Refine the guide based on what was confusing for them",
            ],
        },
        "education_preparation": (
            "IT support is one of the more accessible entry points into tech; many specialists "
            "start with foundational certifications or self-taught troubleshooting skills rather "
            "than a computer science degree, and hands-on comfort with fixing real problems "
            "usually matters more than formal credentials early on."
        ),
        "experience_ideas": {
            "+2 / High School": ["Become the informal tech-helper for family or friends and keep notes on issues solved",
                                  "Try a free IT fundamentals course"],
            "Bachelor": ["Get a part-time or internship help desk role",
                         "Earn a foundational IT certification while studying"],
            "Master": ["Take on a systems administration project or internship",
                       "Move toward a specialization such as networking or security support"],
        },
    },

    ("Technology & Computing", "Cloud / DevOps Engineer"): {
        "description": (
            "Cloud and DevOps engineers build and maintain the infrastructure and deployment "
            "pipelines that let software get built, tested, and released reliably. The role "
            "sits between development and operations, automating repetitive tasks and keeping "
            "systems running smoothly as they scale."
        ),
        "typical_activities": [
            "Setting up and maintaining cloud infrastructure such as servers and storage",
            "Building and maintaining CI/CD pipelines for automated deployment",
            "Writing scripts to automate repetitive operational tasks",
            "Monitoring system performance, uptime, and cloud costs",
            "Responding to and resolving production incidents",
            "Working with development teams to improve deployment processes",
        ],
        "useful_strengths": ["technical_ability", "problem_solving", "analytical_thinking", "organization", "teamwork"],
        "critical_skills": ["technical_ability", "problem_solving", "analytical_thinking", "organization", "teamwork"],
        "skill_importance": {
            "technical_ability": 1.0,
            "problem_solving": 0.9,
            "analytical_thinking": 0.75,
            "organization": 0.6,
            "teamwork": 0.5,
        },
        "useful_academic_areas": ["Computer", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 1.5,
        },
        "work_settings": ["Tech companies (startups to large firms)", "Cloud service providers",
                           "E-commerce platforms", "Financial technology firms",
                           "Any company running production software"],
        "possible_directions": ["Site Reliability Engineering", "Cloud Architecture",
                                 "Platform Engineering", "Infrastructure Security"],
        "foundational_topics": ["Linux & command line fundamentals",
                                 "Cloud computing basics (compute, storage, networking)",
                                 "Version control (Git)", "Automation & scripting concepts"],
        "field_methods": ["Infrastructure as code", "Continuous integration / continuous deployment",
                           "Incident response and postmortems", "Capacity planning"],
        "tools_context": ["Cloud platforms (AWS/Azure/GCP)", "Containerization (Docker)",
                           "Orchestration (Kubernetes)", "CI/CD tools",
                           "Scripting languages (Python/Bash)"],
        "project_ideas": [
            "Deploy a simple app through a CI/CD pipeline",
            "Containerize an existing application",
            "Set up basic cloud infrastructure with automation scripts",
        ],
        "project": {
            "title": "Automated Deployment Pipeline for a Small App",
            "steps": [
                "Build or use a simple existing web app",
                "Put the app in a container using a tool such as Docker",
                "Set up a free-tier cloud account and deploy the container",
                "Build a basic CI/CD pipeline that tests and deploys on every code change",
                "Add simple monitoring or logging to see the app's health",
                "Document the setup so someone else could reproduce it",
            ],
        },
        "education_preparation": (
            "DevOps and cloud engineers often start in software development or IT and grow "
            "into the role, since it blends coding, systems knowledge, and operations; a "
            "computer science background helps, but hands-on experience with cloud platforms "
            "and automation tools, often built through personal projects, is usually what "
            "actually gets tested."
        ),
        "experience_ideas": {
            "+2 / High School": ["Try a free-tier cloud platform account and deploy a basic project",
                                  "Learn command-line basics through an online course"],
            "Bachelor": ["Pursue a DevOps, cloud, or backend development internship",
                         "Earn a foundational cloud certification at the associate level"],
            "Master": ["Contribute to infrastructure automation on a real project or lab",
                       "Pursue an advanced cloud or platform certification alongside applied work"],
        },
    },

    ("Design & Creative", "UX/UI Designer"): {
        "description": (
            "UX/UI designers design how digital products look, feel, and function for the "
            "people who use them, researching user needs, sketching flows, and creating "
            "interfaces that are both usable and visually coherent. The role often spans "
            "research, wireframing, visual design, and testing with real users."
        ),
        "typical_activities": [
            "Researching user needs through interviews or surveys",
            "Sketching wireframes and user flows for a product",
            "Creating high-fidelity visual designs and interactive prototypes",
            "Testing designs with real users and iterating based on feedback",
            "Building and maintaining a consistent design system",
            "Collaborating with developers to make sure designs are implemented accurately",
        ],
        "useful_strengths": ["creativity", "problem_solving", "research", "communication", "analytical_thinking"],
        "critical_skills": ["creativity", "problem_solving", "research", "communication", "analytical_thinking"],
        "skill_importance": {
            "creativity": 1.0,
            "problem_solving": 0.85,
            "research": 0.75,
            "communication": 0.7,
            "analytical_thinking": 0.55,
        },
        "useful_academic_areas": ["Arts", "Computer", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 3.5,
            "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3.5,
            "pref_handson_vs_theoretical": 3.5,
            "pref_tech_vs_people": 3.5,
        },
        "work_settings": ["Tech & product companies", "Design agencies",
                           "Freelance / independent practice",
                           "In-house design teams at non-tech companies", "Startups"],
        "possible_directions": ["Product Design", "User Research",
                                 "Interaction Design", "Design Systems"],
        "foundational_topics": ["Design principles (layout, color, typography)",
                                 "User research methods", "Prototyping & usability testing",
                                 "Basic understanding of how software gets built"],
        "field_methods": ["User interviews", "Usability testing",
                           "Wireframing & sketching", "Design critique sessions"],
        "tools_context": ["Figma or similar design tools", "Prototyping tools",
                           "User research / survey tools",
                           "Basic HTML/CSS understanding (optional but useful)"],
        "project_ideas": [
            "Redesign an app screen you find frustrating to use",
            "Conduct user research and design from the findings",
            "Build a small design system for a fictional product",
        ],
        "project": {
            "title": "Redesign an Existing App Screen",
            "steps": [
                "Pick an app or website with a confusing or clunky screen",
                "Talk to three to five people about their experience using it",
                "Sketch a few alternative layouts addressing the issues found",
                "Create a higher-fidelity mockup or clickable prototype",
                "Test the new design with a couple of users",
                "Write up what changed and why, based on the feedback you gathered",
            ],
        },
        "education_preparation": (
            "UX/UI designers come from varied backgrounds such as graphic design, psychology, "
            "computer science, or self-taught paths, and a strong portfolio showing real design "
            "process and problem-solving usually matters more to employers than the specific "
            "degree; many people build that portfolio through personal or redesign projects."
        ),
        "experience_ideas": {
            "+2 / High School": ["Try a free introductory design tool tutorial",
                                  "Redesign a simple app screen just for practice"],
            "Bachelor": ["Build a portfolio with two or three real or redesign projects",
                         "Look for a UX/UI internship or small freelance projects"],
            "Master": ["Take on a research-heavy design project or thesis",
                       "Seek an internship at a product-focused design team"],
        },
    },

    ("Design & Creative", "Video Editor"): {
        "description": (
            "Video editors assemble raw footage into a finished, coherent video, cutting "
            "scenes, adding sound and effects, and pacing the story so it holds attention. "
            "Work ranges from short social content to longer-form film, documentary, or "
            "corporate video."
        ),
        "typical_activities": [
            "Reviewing and organizing raw footage",
            "Cutting and assembling footage into a coherent sequence",
            "Adding music, sound effects, and basic color correction",
            "Creating titles, transitions, and simple motion graphics",
            "Revising edits based on director or client feedback",
            "Exporting final videos in formats suited to the target platform",
        ],
        "useful_strengths": ["creativity", "technical_ability", "organization", "problem_solving", "communication"],
        "critical_skills": ["creativity", "technical_ability", "organization", "problem_solving", "communication"],
        "skill_importance": {
            "creativity": 1.0,
            "technical_ability": 0.85,
            "organization": 0.65,
            "problem_solving": 0.55,
            "communication": 0.5,
        },
        "useful_academic_areas": ["Arts", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 4.5,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 4.5,
            "pref_tech_vs_people": 2.5,
        },
        "work_settings": ["Production houses & media companies", "Freelance / independent work",
                           "Marketing & advertising agencies", "In-house content teams",
                           "Broadcast / streaming platforms"],
        "possible_directions": ["Motion Graphics", "Colorist",
                                 "Documentary / Film Editing", "Social Media Content Editing"],
        "foundational_topics": ["Editing software fundamentals", "Storytelling & pacing basics",
                                 "File formats & codecs", "Basic color and sound principles"],
        "field_methods": ["Storyboarding & rough cuts", "Client/director feedback rounds",
                           "Color grading", "Sound mixing basics"],
        "tools_context": ["Editing software (Premiere Pro, DaVinci Resolve, Final Cut)",
                           "Motion graphics tools (After Effects)", "Audio editing tools",
                           "Stock footage / music libraries"],
        "project_ideas": [
            "Edit a short film from raw footage",
            "Create a highlight reel from an event",
            "Recut an existing scene in a different style",
        ],
        "project": {
            "title": "Short-Form Video From Raw Footage",
            "steps": [
                "Shoot or source 10-15 minutes of raw footage on a simple topic",
                "Organize and log the footage by scene or shot type",
                "Cut a rough assembly that tells a clear, short story",
                "Add music, sound effects, and simple color correction",
                "Get feedback from a few viewers and revise the cut",
                "Export a polished final version for a specific platform",
            ],
        },
        "education_preparation": (
            "Video editing is heavily portfolio-driven; many editors are self-taught or come "
            "from film and media programs, but what usually gets someone hired is a reel of "
            "finished, well-paced work rather than a specific credential, so practicing on "
            "real footage matters more than formal training alone."
        ),
        "experience_ideas": {
            "+2 / High School": ["Edit videos from personal footage using free editing software",
                                  "Recreate the style of a video you admire as practice"],
            "Bachelor": ["Freelance small editing projects for local creators or events",
                         "Look for an internship at a media or production company"],
            "Master": ["Take on a larger portfolio project such as a short documentary",
                       "Seek specialized training or mentorship in a niche like color grading"],
        },
    },

    ("Design & Creative", "Photographer"): {
        "description": (
            "Photographers capture images for a purpose, whether documenting events, telling "
            "stories, or creating commercial visuals. The work combines the technical skill "
            "of operating a camera with creative judgment about composition, lighting, and "
            "timing, and much of it also happens after the shoot, in selecting and editing images."
        ),
        "typical_activities": [
            "Planning shoots, including location, lighting, and shot list",
            "Operating cameras and lighting equipment during shoots",
            "Directing subjects or coordinating with clients or models",
            "Selecting and culling the best images from a shoot",
            "Editing and retouching photos in post-production",
            "Delivering final images and managing client expectations",
        ],
        "useful_strengths": ["creativity", "technical_ability", "communication", "problem_solving", "organization"],
        "critical_skills": ["creativity", "technical_ability", "communication", "problem_solving", "organization"],
        "skill_importance": {
            "creativity": 1.0,
            "technical_ability": 0.85,
            "communication": 0.6,
            "problem_solving": 0.55,
            "organization": 0.45,
        },
        "useful_academic_areas": ["Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3.5,
            "pref_creative_vs_analytical": 4.5,
            "pref_indoor_vs_outdoor": 3.5,
            "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 4.5,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Freelance / independent studio", "Event & wedding photography",
                           "Media & publishing companies", "Advertising & commercial agencies",
                           "Portrait / studio businesses"],
        "possible_directions": ["Portrait / Wedding Photography", "Commercial / Product Photography",
                                 "Photojournalism", "Fine Art Photography"],
        "foundational_topics": ["Camera fundamentals (exposure, composition)", "Lighting principles",
                                 "Photo editing basics",
                                 "Basic business & client management (if freelancing)"],
        "field_methods": ["Location scouting", "Shot planning & storyboarding",
                           "Studio lighting setup", "Client briefing sessions"],
        "tools_context": ["Camera & lens equipment", "Editing software (Lightroom, Photoshop)",
                           "Lighting equipment", "Portfolio / website platforms"],
        "project_ideas": [
            "Build a themed photo portfolio series",
            "Shoot and edit a mock product photography set",
            "Document a local event or place over time",
        ],
        "project": {
            "title": "Themed Photo Portfolio Series",
            "steps": [
                "Choose a specific theme or subject, such as portraits, street, or nature",
                "Plan three to five shoots with different settings or lighting conditions",
                "Shoot a wide range of images for each session",
                "Cull down to the strongest images from each shoot",
                "Edit the selected photos for a consistent look and style",
                "Assemble a small portfolio and get feedback from others",
            ],
        },
        "education_preparation": (
            "Photography is largely portfolio- and skill-driven; many photographers are "
            "self-taught or learn through workshops and assisting other photographers rather "
            "than a formal degree, though some pursue photography or fine arts programs for "
            "structured training. A strong, consistent body of work is usually what clients "
            "and employers look at first."
        ),
        "experience_ideas": {
            "+2 / High School": ["Practice regularly with any available camera, including a phone, and study composition basics",
                                  "Enter a beginner photo contest or challenge"],
            "Bachelor": ["Assist an established photographer on real shoots",
                         "Take on small freelance or personal-project shoots to build a portfolio"],
            "Master": ["Pursue a specialized area, such as commercial or documentary work, through a focused body of work",
                       "Seek mentorship or a fellowship in a specific photography niche"],
        },
    },

    # --- from group2_finance.py ---
    ("Finance & Business", "Marketing Manager"): {
        "description": (
            "Marketing managers plan and oversee campaigns that promote a product, "
            "service, or brand -- figuring out who the audience is, what message "
            "will resonate, and which channels to use. The job mixes creative "
            "judgment with reading data on what's actually working, and usually "
            "involves coordinating other people (designers, writers, agencies) "
            "rather than doing all the creative work personally."
        ),
        "typical_activities": [
            "Developing marketing plans and campaign strategies",
            "Analyzing market research and customer data",
            "Coordinating with designers, content creators, or outside agencies",
            "Managing budgets across different marketing channels",
            "Tracking campaign performance (reach, engagement, conversion)",
            "Presenting results and recommendations to leadership",
        ],
        "useful_strengths": ["creativity", "communication", "analytical_thinking", "leadership", "presentation"],
        "critical_skills": ["creativity", "communication", "analytical_thinking", "leadership"],
        "skill_importance": {
            "creativity": 1.0,
            "communication": 0.9,
            "analytical_thinking": 0.75,
            "leadership": 0.6,
        },
        "useful_academic_areas": ["Business/Economics", "Arts", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 4,
            "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["Corporate marketing departments", "Advertising or marketing agencies",
                           "Retail and consumer brands", "Startups", "E-commerce companies"],
        "possible_directions": ["Digital Marketing", "Brand Management", "Product Marketing", "Marketing Analytics"],
        "foundational_topics": ["Basics of consumer behavior", "The marketing mix (product, price, place, promotion)",
                                 "Reading basic campaign metrics"],
        "field_methods": ["Market research and surveys", "Competitor analysis", "Customer segmentation",
                           "A/B testing of messaging or offers"],
        "tools_context": ["Social media and ad platforms (as marketing channels)",
                           "Spreadsheet tools for budgets and tracking metrics",
                           "Basic design tools like Canva (optional)",
                           "Email marketing platforms (optional)"],
        "project_ideas": ["Mini campaign plan for a local business", "Social media content calendar",
                           "Competitor marketing analysis"],
        "project": {
            "title": "Mock Marketing Campaign for a Local Business",
            "steps": [
                "Pick a small, real local business (with permission, or hypothetically)",
                "Research who its target customers likely are",
                "Define one clear campaign goal and pick 2-3 channels to reach that audience",
                "Draft sample messaging or content for the campaign",
                "Outline how you would measure whether the campaign worked",
                "Put it together as a short campaign brief",
            ],
        },
        "education_preparation": (
            "A business, marketing, or communications degree is common but not the only path in; "
            "employers often care as much about a portfolio of real or self-directed campaign work "
            "as the specific degree."
        ),
        "experience_ideas": {
            "+2 / High School": ["Run a small social media page for a club, event, or hobby and track what content performs",
                                  "Take a free introductory marketing course"],
            "Bachelor": ["Seek a marketing internship, even part-time or unpaid at a small business",
                        "Volunteer to handle marketing/promotion for a student club or event"],
            "Master": ["Take on a marketing role with real budget or campaign ownership",
                      "Build a portfolio case study showing a campaign you planned and its measured results"],
        },
    },

    ("Finance & Business", "Banking Officer"): {
        "description": (
            "Banking officers work in a bank branch or department handling customer "
            "accounts, deposits, and loans -- opening accounts, processing "
            "applications, explaining products, and making sure transactions follow "
            "banking regulations. Much of the work is direct customer interaction "
            "combined with careful documentation and rule-following."
        ),
        "typical_activities": [
            "Opening and managing customer accounts",
            "Processing loan or credit applications and checking basic eligibility",
            "Explaining banking products and terms to customers",
            "Ensuring transactions follow compliance and documentation requirements",
            "Reconciling daily transactions and reports",
            "Referring customers to the right banking service or specialist",
        ],
        "useful_strengths": ["communication", "organization", "analytical_thinking", "teamwork"],
        "critical_skills": ["communication", "organization", "analytical_thinking"],
        "skill_importance": {
            "communication": 1.0,
            "organization": 0.85,
            "analytical_thinking": 0.7,
        },
        "useful_academic_areas": ["Business/Economics", "Mathematics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 4,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Bank branches", "Retail banking divisions", "Commercial or corporate banking teams",
                           "Credit unions"],
        "possible_directions": ["Retail Banking", "Loan/Credit Officer", "Relationship Banking", "Branch Operations"],
        "foundational_topics": ["Basics of common banking products (savings, loans, deposits)",
                                 "Basic financial literacy", "Introductory banking regulations and documentation (e.g. KYC)"],
        "field_methods": ["Customer needs assessment conversations", "Basic document and identity verification",
                           "Cash handling and reconciliation procedures"],
        "tools_context": ["Core banking software (used on the job)", "Spreadsheet tools for reports",
                           "Basic financial calculators"],
        "project_ideas": ["Compare loan products from different banks", "Mock customer needs interview",
                           "Basic budgeting guide for a customer"],
        "project": {
            "title": "Comparing Everyday Banking Products",
            "steps": [
                "Pick three banks and look up their publicly listed savings or loan products",
                "Compare interest rates, fees, and terms across them",
                "Note which type of customer each product would likely suit best",
                "Write a short plain-language comparison guide as if explaining it to a customer",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in commerce, finance, or business is commonly preferred; many banks "
            "provide their own product and systems training, so entry-level hiring often weighs "
            "communication skills and reliability as much as the specific degree."
        ),
        "experience_ideas": {
            "+2 / High School": ["Take a free intro personal finance or banking course",
                                  "Practice explaining a financial concept (like interest or loans) to someone unfamiliar with it"],
            "Bachelor": ["Apply for a bank internship or part-time teller/customer service role",
                        "Volunteer for a finance literacy program if available"],
            "Master": ["Seek an internship in credit analysis or relationship banking",
                      "Study for a professional banking or credit certification, if pursuing a specialization"],
        },
    },

    ("Finance & Business", "Chartered Accountant"): {
        "description": (
            "Chartered Accountants prepare and audit financial statements, advise "
            "on tax and regulatory compliance, and ensure an organization's "
            "financial records are accurate and legally sound. Becoming a CA is a "
            "regulated path: it requires completing a formal articleship/practical "
            "training period and passing a structured series of professional exams "
            "through the relevant accounting body. This roadmap is only for "
            "exploring and preparing for that path -- it is not a substitute for "
            "the formal qualification."
        ),
        "typical_activities": [
            "Reviewing and preparing financial statements",
            "Conducting audits of company accounts",
            "Advising on tax planning and regulatory compliance",
            "Maintaining and checking bookkeeping records",
            "Ensuring statutory filings are accurate and submitted on time",
        ],
        "useful_strengths": ["analytical_thinking", "organization", "problem_solving", "research"],
        "critical_skills": ["analytical_thinking", "organization", "problem_solving"],
        "skill_importance": {
            "analytical_thinking": 1.0,
            "organization": 0.85,
            "problem_solving": 0.7,
        },
        "useful_academic_areas": ["Mathematics", "Business/Economics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 1,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 2,
            "pref_tech_vs_people": 2,
        },
        "work_settings": ["Accounting and audit firms", "Corporate finance departments", "Tax consultancies",
                           "Government finance bodies"],
        "possible_directions": ["Audit", "Taxation", "Financial Reporting", "Management Accounting"],
        "foundational_topics": ["Bookkeeping basics", "How financial statements are structured (balance sheet, income statement)",
                                 "Basics of taxation"],
        "field_methods": ["Manual bookkeeping practice with sample transactions", "Reading and interpreting published financial statements"],
        "tools_context": ["Spreadsheet software", "Accounting software (for familiarity only, not certification)"],
        "project_ideas": ["Learn double-entry bookkeeping with sample transactions",
                           "Read and summarize a public company's annual report",
                           "Track personal or household finances in a simple ledger"],
        "project": None,
        "education_preparation": (
            "Becoming a Chartered Accountant requires enrolling in a formal CA program that combines "
            "practical articleship training with a structured series of professional exams administered "
            "by the relevant accounting body (exact structure and timelines vary by country). A "
            "bachelor's degree in commerce or accounting is a common preparatory step, but nothing in "
            "this roadmap substitutes for that formal, regulated qualification -- it is meant only to "
            "help you explore whether the field is a fit before committing to it."
        ),
        "experience_ideas": {
            "+2 / High School": ["Research CA program entry requirements in your country",
                                  "Take a free introductory bookkeeping or accounting course"],
            "Bachelor": ["Confirm eligibility for, or enroll in, a recognized CA program",
                        "Seek an internship or articleship placement at an accounting firm"],
            "Master": ["Pursue advanced specialization (e.g. tax, forensic accounting) through formal study after qualifying"],
        },
    },

    ("Finance & Business", "Business Analyst"): {
        "description": (
            "Business analysts sit between business needs and solutions -- "
            "gathering requirements from stakeholders, analyzing processes or data, "
            "and recommending improvements to how an organization operates or the "
            "systems it uses. The work involves a lot of listening and documenting, "
            "followed by translating what people need into something concrete that "
            "both business and technical teams can act on."
        ),
        "typical_activities": [
            "Interviewing stakeholders to gather requirements",
            "Documenting current versus desired business processes",
            "Analyzing data to identify inefficiencies or opportunities",
            "Creating process diagrams and written reports",
            "Presenting findings and recommendations to stakeholders",
            "Supporting the rollout of approved changes",
        ],
        "useful_strengths": ["analytical_thinking", "communication", "problem_solving", "research", "organization"],
        "critical_skills": ["analytical_thinking", "communication", "problem_solving", "organization"],
        "skill_importance": {
            "analytical_thinking": 1.0,
            "communication": 0.85,
            "problem_solving": 0.75,
            "organization": 0.55,
        },
        "useful_academic_areas": ["Business/Economics", "Computer", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Corporate strategy or operations teams", "IT departments", "Consulting firms",
                           "Financial services companies"],
        "possible_directions": ["Process Improvement", "IT Business Analysis", "Data/Reporting Analysis",
                                 "Management Consulting"],
        "foundational_topics": ["Basics of business process mapping", "Requirements-gathering techniques",
                                 "Basic data analysis"],
        "field_methods": ["Stakeholder interviews", "Process mapping and flowcharting", "Gap analysis"],
        "tools_context": ["Spreadsheet tools", "Flowchart or diagramming tools", "Basic database or reporting tools (optional)"],
        "project_ideas": ["Map a process at a small business", "Requirements doc for a simple app idea",
                           "Data-driven improvement proposal"],
        "project": {
            "title": "Process Improvement Case Study",
            "steps": [
                "Pick a simple process you interact with (a campus service, a small shop, a club sign-up)",
                "Map out how it currently works, step by step",
                "Interview 2-3 people who use it about where it breaks down or frustrates them",
                "Identify the main bottleneck or pain point",
                "Propose one specific, realistic improvement",
                "Note how you'd measure whether the improvement actually helped",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in business, information systems, or a related field is common, but "
            "business analysts come from varied academic backgrounds -- strong analytical thinking and "
            "the ability to communicate clearly across both business and technical audiences matter more "
            "than a specific major."
        ),
        "experience_ideas": {
            "+2 / High School": ["Practice breaking down a familiar process (like a school registration system) into steps",
                                  "Take a free intro course on data analysis or business fundamentals"],
            "Bachelor": ["Seek a business analyst or operations internship",
                        "Volunteer to document or improve a process for a student organization"],
            "Master": ["Take on a project involving real stakeholder interviews and a documented recommendation",
                      "Build a small portfolio case study of a process you analyzed and improved"],
        },
    },

    ("Finance & Business", "Entrepreneur"): {
        "description": (
            "Entrepreneurs identify a problem worth solving and build a business "
            "around addressing it -- from the initial idea through launch, "
            "iteration, and eventually managing growth. It combines idea "
            "validation, resourcefulness with limited resources, and comfort with "
            "financial and operational uncertainty, since much of the work happens "
            "without a fixed process or guaranteed outcome."
        ),
        "typical_activities": [
            "Identifying and validating a problem or business idea",
            "Developing a product or service offering",
            "Managing budgets and cash flow with limited resources",
            "Building a customer base and handling early sales",
            "Adapting the plan or offering based on real feedback",
            "Managing a small team as the business grows",
        ],
        "useful_strengths": ["problem_solving", "creativity", "leadership", "communication", "organization"],
        "critical_skills": ["problem_solving", "creativity", "leadership", "communication"],
        "skill_importance": {
            "problem_solving": 1.0,
            "creativity": 0.85,
            "leadership": 0.75,
            "communication": 0.65,
        },
        "useful_academic_areas": ["Business/Economics", "Arts", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 4,
            "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 5,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Startups (own venture)", "Small businesses", "Co-working spaces",
                           "Home-based or remote operations"],
        "possible_directions": ["Product/Tech Startup", "Local Service Business", "E-commerce", "Social Enterprise"],
        "foundational_topics": ["Basics of validating a business idea", "Budgeting and cash-flow basics",
                                 "Basics of marketing and sales"],
        "field_methods": ["Customer discovery interviews", "Testing a small/minimal version of the idea before scaling it",
                           "Basic financial planning"],
        "tools_context": ["Spreadsheet tools for budgeting", "Simple website or e-commerce builders (optional)",
                           "Social media for early marketing"],
        "project_ideas": ["Validate a small business idea with real customers", "Build and sell a simple product or service",
                           "Write a one-page business plan"],
        "project": {
            "title": "Test a Small Business Idea",
            "steps": [
                "Identify a real problem or need you could plausibly address",
                "Talk to 5-10 potential customers about whether it's actually a problem for them",
                "Sketch a simple, low-cost version of the product or service",
                "Offer it on a small scale, even to just a handful of people",
                "Gather feedback and note honestly what you'd change",
            ],
        },
        "education_preparation": (
            "There's no fixed educational path -- entrepreneurs come from many backgrounds. A business "
            "or commerce degree can help with fundamentals, but small, low-stakes hands-on attempts at "
            "building something tend to teach more than coursework alone."
        ),
        "experience_ideas": {
            "+2 / High School": ["Try a small low-risk venture (selling something, offering a service locally)",
                                  "Follow a founder or small business owner's story to see what the day-to-day actually looks like"],
            "Bachelor": ["Join a student entrepreneurship club or startup competition",
                        "Attempt a real small-scale venture, even part-time"],
            "Master": ["Develop a more serious business plan and test it with real customers",
                      "Seek mentorship from an experienced founder or small business owner"],
        },
    },

    ("Finance & Business", "Human Resources Manager"): {
        "description": (
            "HR managers handle the people side of an organization -- hiring, "
            "employee relations, workplace policies, and culture. The work "
            "involves balancing what employees need, what the organization needs, "
            "and legal or policy requirements, often while handling sensitive or "
            "difficult conversations."
        ),
        "typical_activities": [
            "Managing recruitment and hiring processes",
            "Handling employee relations issues and workplace conflicts",
            "Developing and enforcing workplace policies",
            "Coordinating training programs and performance reviews",
            "Ensuring compliance with labor laws and regulations",
            "Supporting compensation and benefits decisions",
        ],
        "useful_strengths": ["communication", "organization", "problem_solving", "leadership", "teamwork"],
        "critical_skills": ["communication", "organization", "problem_solving", "leadership"],
        "skill_importance": {
            "communication": 1.0,
            "organization": 0.8,
            "problem_solving": 0.7,
            "leadership": 0.6,
        },
        "useful_academic_areas": ["Business/Economics", "English", "Arts"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Corporate HR departments", "Recruitment or staffing agencies", "Nonprofit organizations",
                           "Government agencies"],
        "possible_directions": ["Recruitment/Talent Acquisition", "Employee Relations", "Training & Development",
                                 "Compensation & Benefits"],
        "foundational_topics": ["Basics of labor law and workplace policy", "Recruitment and interviewing basics",
                                 "Conflict resolution basics"],
        "field_methods": ["Structured interviewing", "Policy documentation", "Conflict mediation"],
        "tools_context": ["Applicant tracking systems (used on the job)", "Spreadsheet tools for records",
                           "Basic HR information systems (optional)"],
        "project_ideas": ["Design a hiring process for a small team", "Draft a workplace policy document",
                           "Mock conflict-resolution scenario write-up"],
        "project": {
            "title": "Design a Hiring Process for a Small Role",
            "steps": [
                "Pick a simple job role (e.g. a campus club coordinator)",
                "Write a clear job description for it",
                "Design 5-6 interview questions that would genuinely reveal fit for the role",
                "Outline how you'd screen and fairly compare candidates",
                "Note what a basic onboarding plan for that role would look like",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in HR, business, or psychology is common; people skills and comfort "
            "with policy and documentation matter as much as the specific degree, and many HR "
            "professionals move into the field from other people-facing roles."
        ),
        "experience_ideas": {
            "+2 / High School": ["Practice writing a fair set of interview questions for a hypothetical role",
                                  "Read about basic workplace rights and policies in your region"],
            "Bachelor": ["Seek an HR internship or a role helping with recruitment/events for a student organization",
                        "Volunteer to help organize hiring or onboarding for a club"],
            "Master": ["Take on an HR generalist or specialist internship with real casework",
                      "Study a specific HR specialization (e.g. compensation, employee relations) in more depth"],
        },
    },

    ("Finance & Business", "Supply Chain Manager"): {
        "description": (
            "Supply chain managers coordinate the flow of goods -- from sourcing "
            "raw materials through production to final delivery -- to keep "
            "operations efficient and costs under control. The work involves "
            "logistics coordination, working with suppliers, and problem-solving "
            "quickly when shipments, materials, or timelines don't go as planned."
        ),
        "typical_activities": [
            "Coordinating with suppliers and vendors, including negotiating terms",
            "Planning and monitoring inventory levels",
            "Tracking shipments and logistics schedules",
            "Analyzing costs and identifying efficiency improvements",
            "Resolving disruptions such as delays or shortages",
            "Coordinating across procurement, production, and distribution teams",
        ],
        "useful_strengths": ["organization", "analytical_thinking", "problem_solving", "communication", "leadership"],
        "critical_skills": ["organization", "problem_solving", "analytical_thinking", "communication"],
        "skill_importance": {
            "organization": 1.0,
            "problem_solving": 0.85,
            "analytical_thinking": 0.75,
            "communication": 0.55,
        },
        "useful_academic_areas": ["Business/Economics", "Mathematics", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Manufacturing companies", "Retail and distribution centers", "Logistics and shipping firms",
                           "Import/export businesses"],
        "possible_directions": ["Procurement", "Logistics/Distribution", "Inventory Planning", "Vendor Management"],
        "foundational_topics": ["Basics of inventory management", "How supply chains are structured (sourcing to delivery)",
                                 "Basic cost and logistics analysis"],
        "field_methods": ["Inventory tracking methods", "Vendor evaluation and negotiation basics",
                           "Demand forecasting basics"],
        "tools_context": ["Spreadsheet tools for tracking inventory and costs", "Supply chain/ERP software (used on the job)",
                           "Basic scheduling tools"],
        "project_ideas": ["Map the supply chain of an everyday product", "Inventory tracking spreadsheet for a small shop",
                           "Compare two suppliers on cost and reliability"],
        "project": {
            "title": "Trace a Product's Supply Chain",
            "steps": [
                "Pick a common product you use regularly",
                "Research where its raw materials or components likely come from",
                "Map out the stages from sourcing to reaching a customer",
                "Identify points in that chain where delays or extra costs could arise",
                "Suggest one realistic improvement to that chain",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in supply chain management, business, or industrial engineering is "
            "common; strong organizational and analytical habits matter a great deal, and entry-level "
            "operations or logistics roles are a typical starting point."
        ),
        "experience_ideas": {
            "+2 / High School": ["Track and analyze a household or personal 'supply chain' (grocery shopping, budgeting for supplies)",
                                  "Read about how a familiar product gets made and delivered"],
            "Bachelor": ["Seek an internship in operations, logistics, or procurement",
                        "Take on inventory or event-logistics responsibility for a student organization"],
            "Master": ["Pursue an internship or project involving real vendor or logistics coordination",
                      "Study a specific area like procurement or demand planning in more depth"],
        },
    },

    ("Finance & Business", "Insurance Agent"): {
        "description": (
            "Insurance agents help individuals or businesses choose insurance "
            "policies that match their needs, explain coverage and terms clearly, "
            "and support clients through applications and claims. Much of the work "
            "is relationship-based and sales-driven, combined with a solid working "
            "knowledge of policy details and relevant regulations."
        ),
        "typical_activities": [
            "Meeting with clients to assess their insurance needs",
            "Explaining policy options, coverage, and costs",
            "Helping clients complete applications and paperwork",
            "Following up on claims and policy renewals",
            "Building and maintaining a client base",
            "Staying current on policy and regulation changes",
        ],
        "useful_strengths": ["communication", "presentation", "organization", "problem_solving"],
        "critical_skills": ["communication", "presentation", "organization"],
        "skill_importance": {
            "communication": 1.0,
            "presentation": 0.8,
            "organization": 0.65,
        },
        "useful_academic_areas": ["Business/Economics", "English", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Insurance companies and agencies", "Independent brokerage practices",
                           "Banks (bancassurance)", "Client-facing field visits"],
        "possible_directions": ["Life Insurance", "Health Insurance", "General/Property Insurance", "Insurance Brokerage"],
        "foundational_topics": ["Basics of how insurance and risk pooling work", "Common policy types and terms",
                                 "Basics of sales and client communication"],
        "field_methods": ["Client needs-assessment conversations", "Policy comparison and explanation",
                           "Claims follow-up process"],
        "tools_context": ["Spreadsheet or CRM tools for tracking clients (used on the job)",
                           "Insurer's own policy management systems"],
        "project_ideas": ["Compare insurance policy options for a scenario", "Mock client needs-assessment conversation",
                           "Explain a policy in plain language"],
        "project": {
            "title": "Compare Insurance Options for a Sample Client",
            "steps": [
                "Create a simple client profile (age, needs, rough budget)",
                "Research 2-3 publicly available policy types that could fit that profile",
                "Compare their coverage, costs, and key exclusions",
                "Write a plain-language explanation of your recommendation, as if presenting it to the client",
            ],
        },
        "education_preparation": (
            "A bachelor's degree is common but not always required; many regions require passing a "
            "licensing exam specific to the type of insurance sold, so checking local licensing "
            "requirements early is worthwhile."
        ),
        "experience_ideas": {
            "+2 / High School": ["Practice explaining a financial or insurance concept clearly to someone unfamiliar with it",
                                  "Research how basic insurance types (health, life, property) work"],
            "Bachelor": ["Look into entry-level or internship roles at an insurance agency",
                        "Research licensing requirements for insurance agents in your region"],
            "Master": ["Pursue a specialization (e.g. health, commercial) through formal study or certification",
                      "Seek a role with real client-facing sales responsibility"],
        },
    },

    # --- from group3_publicservice_education.py ---
    # ---------------------------------------------------------------
    # Public Service & Law
    # ---------------------------------------------------------------

    ("Public Service & Law", "Civil Servant (Loksewa)"): {
        "description": (
            "Civil servants work within government ministries and departments, "
            "implementing public policy, managing administrative processes, and "
            "delivering public services. In Nepal, entry is primarily through the "
            "Loksewa Aayog (Public Service Commission) competitive examination "
            "system rather than through a specific required degree or specialization."
        ),
        "typical_activities": [
            "Drafting official letters, reports, and administrative documents",
            "Processing applications, permits, or public records",
            "Coordinating work between government departments",
            "Implementing government programs and policies at a local level",
            "Meeting with members of the public to address requests or grievances",
            "Preparing budgets, files, and administrative records",
        ],
        "useful_strengths": ["organization", "communication", "analytical_thinking",
                              "problem_solving", "leadership"],
        "critical_skills": ["organization", "communication", "analytical_thinking",
                             "problem_solving", "leadership"],
        "skill_importance": {"organization": 0.9, "communication": 0.85,
                              "analytical_thinking": 0.75, "problem_solving": 0.65,
                              "leadership": 0.55},
        "useful_academic_areas": ["English", "Mathematics", "Business/Economics", "Arts"],
        "work_preferences": {
            "pref_people_vs_independent": 4, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 1,
            "pref_handson_vs_theoretical": 2, "pref_tech_vs_people": 4,
        },
        "work_settings": ["Government ministries and departments", "District administration offices",
                           "Public service delivery counters", "Government field offices"],
        "possible_directions": ["General Administration Service", "Revenue / Finance Service",
                                 "Education Service", "Local Governance"],
        "foundational_topics": [
            "Nepal's constitution and basic governance structure",
            "How public administration and government offices function",
            "Current affairs and general knowledge",
            "Basics of government budgeting and public resource use",
        ],
        "field_methods": [
            "Practicing past Loksewa exam papers under timed conditions",
            "Mock interview practice",
            "Reading government notices, gazettes, or policy documents",
            "Group discussion and debate practice on public-issue topics",
        ],
        "tools_context": ["Word processing and document-drafting tools",
                           "Government e-service portals (as a user, to understand public-facing systems)"],
        "project_ideas": ["Mock Loksewa exam study plan", "Local governance process case study",
                           "Public service process mapping exercise"],
        "project": {
            "title": "Local Public Service Process Map",
            "steps": [
                "Pick one common public service (e.g. citizenship certificate, land registration, a permit)",
                "Find out, step by step, what a person actually has to do to get it",
                "Note where the process is confusing, slow, or unclear",
                "Talk to someone who has been through the process, if possible",
                "Organize what you found into a simple step-by-step map",
                "Suggest 1-2 realistic ways the process could be clearer or faster",
            ],
        },
        "education_preparation": (
            "Entry is primarily through the Loksewa Aayog (Public Service Commission) competitive "
            "exam system rather than a specific required degree; a bachelor's degree in any subject "
            "is typically the minimum requirement to sit for officer-level exams, and sustained, "
            "disciplined exam preparation matters more than the specific subject you studied."
        ),
        "experience_ideas": {
            "+2 / High School": ["Follow current affairs and government policy news regularly",
                                  "Talk to a working civil servant about their day-to-day role"],
            "Bachelor": ["Start studying past Loksewa question patterns and the official syllabus",
                         "Join or form a peer study group for structured exam preparation"],
            "Master": ["Take full-length mock exams under timed conditions",
                       "Deepen subject knowledge in the specific service group you plan to target"],
        },
    },

    ("Public Service & Law", "Police Officer"): {
        "description": (
            "Police officers maintain public order, prevent and investigate crime, and respond "
            "to emergencies within an assigned community or jurisdiction. The work combines "
            "physical fieldwork, direct public interaction, and procedural record-keeping, and "
            "entry is typically through a structured recruitment and training process rather "
            "than a specific academic degree."
        ),
        "typical_activities": [
            "Patrolling an assigned area on foot, by vehicle, or otherwise",
            "Responding to incidents and emergency calls",
            "Investigating reported crimes and gathering evidence",
            "Writing incident and case reports",
            "Interacting with community members and coordinating with fellow officers",
            "Appearing in court or at hearings to give testimony when required",
        ],
        "useful_strengths": ["problem_solving", "communication", "teamwork",
                              "organization", "leadership"],
        "critical_skills": ["problem_solving", "communication", "teamwork",
                             "organization", "leadership"],
        "skill_importance": {"problem_solving": 0.85, "communication": 0.8,
                              "teamwork": 0.75, "organization": 0.6, "leadership": 0.55},
        "useful_academic_areas": ["English", "Science", "Arts"],
        "work_preferences": {
            "pref_people_vs_independent": 4, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 4, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 4,
        },
        "work_settings": ["Police stations", "Community patrol areas", "Traffic and field posts",
                           "Criminal investigation units", "Courts (for testimony)"],
        "possible_directions": ["Traffic Police", "Criminal Investigation", "Community Policing",
                                 "Specialized units (e.g. cyber, forensics)"],
        "foundational_topics": [
            "Basics of criminal law and how the justice system fits together",
            "Physical fitness and discipline standards expected of officers",
            "Conflict de-escalation and calm communication under pressure",
            "Awareness of the local community and geography an officer works in",
        ],
        "field_methods": [
            "Regular physical fitness training",
            "Patrol and observation practice",
            "Basic first-aid training",
            "Incident report writing practice",
            "Scenario-based / roleplay training exercises",
        ],
        "tools_context": ["Two-way radio and basic communication equipment",
                           "Incident-reporting and record-keeping systems"],
        "project_ideas": ["Neighborhood safety observation log", "Traffic safety pattern review",
                           "Community outreach mini-plan"],
        "project": {
            "title": "Community Safety Observation Project",
            "steps": [
                "Choose a small, familiar local area (a street, market, or neighborhood)",
                "Observe and note safety issues over a few days (lighting, traffic, crowding, etc.)",
                "Talk respectfully with a few community members about their safety concerns",
                "Organize what you found into a short list of issues",
                "Suggest 2-3 practical, realistic improvements",
                "Write a short summary report",
            ],
        },
        "education_preparation": (
            "Entry is typically through a national or local police recruitment process involving "
            "written exams, physical fitness tests, and academy training rather than a specific "
            "degree, though a bachelor's degree is required for officer-level entry in many systems; "
            "consistent physical fitness matters just as much as academic preparation."
        ),
        "experience_ideas": {
            "+2 / High School": ["Build and maintain physical fitness through regular training",
                                  "Learn about local police recruitment requirements and exam patterns"],
            "Bachelor": ["Prepare for physical fitness tests alongside written exam preparation",
                         "Volunteer in community safety or disaster-response programs if available"],
            "Master": ["Pursue specialized study relevant to investigation, forensics, or law if "
                       "targeting a specialized track"],
        },
    },

    ("Public Service & Law", "Army Officer"): {
        "description": (
            "Army officers lead and manage military personnel, plan and take part in operations "
            "and exercises, and are responsible for the training, discipline, and welfare of their "
            "unit. The role combines leadership, physical readiness, and decision-making under "
            "pressure, with entry through a formal military commissioning process rather than a "
            "typical civilian career path."
        ),
        "typical_activities": [
            "Leading and training a unit of soldiers",
            "Planning and taking part in drills and field exercises",
            "Maintaining equipment and unit readiness standards",
            "Managing logistics and resources for a unit",
            "Making decisions under time pressure during exercises or operations",
            "Mentoring and evaluating subordinate personnel",
        ],
        "useful_strengths": ["leadership", "problem_solving", "organization",
                              "teamwork", "communication"],
        "critical_skills": ["leadership", "problem_solving", "organization",
                             "teamwork", "communication"],
        "skill_importance": {"leadership": 0.9, "problem_solving": 0.75,
                              "organization": 0.7, "teamwork": 0.7, "communication": 0.6},
        "useful_academic_areas": ["Mathematics", "Science", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 4, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 5, "pref_structured_vs_flexible": 1,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 3,
        },
        "work_settings": ["Military bases and cantonments", "Field training areas",
                           "Border or deployment postings", "Command offices"],
        "possible_directions": ["Infantry / Combat Arms", "Engineering Corps",
                                 "Logistics / Administration", "Signals / Communications"],
        "foundational_topics": [
            "Basics of military organization, strategy, and history",
            "Physical fitness standards expected of officers",
            "Leadership fundamentals -- setting direction and taking responsibility for a team",
            "Discipline and chain-of-command structure",
        ],
        "field_methods": [
            "Physical endurance training",
            "Drill and formation practice",
            "Land navigation and map reading",
            "Basic tactical exercise participation",
        ],
        "tools_context": ["Map and navigation tools", "Basic field communication equipment"],
        "project_ideas": ["Personal fitness and discipline plan", "Small-team leadership exercise",
                           "Local map navigation practice"],
        "project": {
            "title": "Team Leadership Mini-Exercise",
            "steps": [
                "Organize a small group activity (a sports team, study group, or volunteer task)",
                "Take on a defined leadership role for that activity",
                "Set clear goals and assign tasks to the group",
                "Run the activity through to completion",
                "Reflect afterward on what worked and what didn't",
                "Write a short reflection on what you learned about leading others",
            ],
        },
        "education_preparation": (
            "Entry is through a formal military commissioning process -- entrance exam, physical "
            "and medical standards, and officer academy training -- rather than a specific civilian "
            "degree, though a bachelor's degree is typically required or completed as part of "
            "training; sustained physical fitness and discipline matter from an early stage."
        ),
        "experience_ideas": {
            "+2 / High School": ["Maintain a structured physical fitness routine",
                                  "Research the officer commissioning process and entry requirements"],
            "Bachelor": ["Take on leadership roles in clubs, sports teams, or student organizations",
                         "Prepare for the physical and written standards of officer entry exams"],
            "Master": ["If applicable, target specialized commissioning routes (engineering, "
                       "medical, etc.) that match your degree"],
        },
    },

    ("Public Service & Law", "Diplomat / Foreign Affairs"): {
        "description": (
            "Diplomats represent their country's interests abroad, take part in negotiations, "
            "manage international relations, and support citizens living or traveling overseas. "
            "The work relies on careful written and verbal communication, cross-cultural awareness, "
            "and analysis of political and economic developments, with entry typically through a "
            "competitive foreign service exam."
        ),
        "typical_activities": [
            "Drafting diplomatic correspondence, memos, and reports",
            "Attending and representing the country at official meetings or negotiations",
            "Assisting citizens abroad with visas, documentation, or emergencies",
            "Analyzing political and economic developments in a host country",
            "Building working relationships with foreign officials and organizations",
            "Organizing cultural events or bilateral programs",
        ],
        "useful_strengths": ["communication", "analytical_thinking", "research",
                              "presentation", "organization"],
        "critical_skills": ["communication", "analytical_thinking", "research",
                             "presentation", "organization"],
        "skill_importance": {"communication": 0.9, "analytical_thinking": 0.75,
                              "research": 0.7, "presentation": 0.65, "organization": 0.55},
        "useful_academic_areas": ["English", "Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 4, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 2, "pref_tech_vs_people": 5,
        },
        "work_settings": ["Embassies and consulates", "Ministry of Foreign Affairs offices",
                           "International conferences and summits", "Overseas postings"],
        "possible_directions": ["Political / Diplomatic Track", "Economic & Trade Affairs",
                                 "Consular Services", "Multilateral / International Organizations"],
        "foundational_topics": [
            "Basics of international relations and diplomacy",
            "Home country's foreign policy history and priorities",
            "A working level of at least one additional language",
            "Diplomatic protocol and formal communication etiquette",
        ],
        "field_methods": [
            "Model UN or debate participation",
            "Current-affairs analysis practice",
            "Formal memo and briefing-note writing practice",
            "Cross-cultural communication practice",
        ],
        "tools_context": ["Word processing and report-drafting tools",
                           "Translation resources", "Video conferencing for international meetings"],
        "project_ideas": ["Model UN or debate participation", "Bilateral relations case study",
                           "Foreign policy briefing memo"],
        "project": {
            "title": "Country Relations Briefing Memo",
            "steps": [
                "Choose two countries and one specific shared issue (trade, migration, etc.)",
                "Research each country's position and history on that issue",
                "Summarize the key facts in your own words",
                "Write a short briefing memo as if advising a diplomat on the topic",
                "Propose 2-3 possible talking points or next steps",
            ],
        },
        "education_preparation": (
            "Entry is usually through a competitive foreign service exam requiring a bachelor's "
            "degree, often in international relations, political science, law, or economics, "
            "though not strictly limited to these; strong written communication and a genuine "
            "habit of following current affairs are built up over years, not from a single course."
        ),
        "experience_ideas": {
            "+2 / High School": ["Participate in Model United Nations or debate clubs",
                                  "Follow international news and one specific country or region closely"],
            "Bachelor": ["Study or improve proficiency in an additional language",
                         "Seek internships with international organizations, NGOs, or government "
                         "foreign affairs offices"],
            "Master": ["Pursue a master's in international relations, diplomacy, or a related field "
                       "if targeting the foreign service track",
                       "Attend or help organize a Model UN / international affairs conference"],
        },
    },

    ("Public Service & Law", "Lawyer / Advocate"): {
        "description": (
            "Lawyers and advocates represent clients, provide legal advice, draft legal documents, "
            "and argue cases in court, usually within a specific area of law such as criminal, "
            "civil, corporate, or family law. Practicing law is a regulated profession requiring a "
            "formal law degree (e.g. an LLB) and registration with the bar council -- this roadmap "
            "is for exploring and preparing for the field, not a substitute for that formal "
            "qualification and licensing."
        ),
        "typical_activities": [
            "Meeting clients to understand their legal issue",
            "Researching relevant laws and precedent cases",
            "Drafting contracts, petitions, or other legal documents",
            "Representing clients in court hearings or negotiations",
            "Advising clients on their legal rights and obligations",
            "Keeping up with changes in law and regulation",
        ],
        "useful_strengths": ["analytical_thinking", "research", "communication",
                              "presentation", "problem_solving"],
        "critical_skills": ["analytical_thinking", "research", "communication",
                             "presentation", "problem_solving"],
        "skill_importance": {"analytical_thinking": 0.9, "research": 0.85,
                              "communication": 0.8, "presentation": 0.65, "problem_solving": 0.6},
        "useful_academic_areas": ["English", "Arts", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 2, "pref_tech_vs_people": 4,
        },
        "work_settings": ["Law firms", "Courts", "Government legal offices",
                           "Corporate legal departments", "Independent practice"],
        "possible_directions": ["Litigation", "Corporate / Business Law", "Criminal Law",
                                 "Family Law", "Human Rights Law"],
        "foundational_topics": [
            "Basics of legal reasoning and argumentation",
            "How to read and interpret case law",
            "Structure of the court system",
            "Basics of contract and constitutional law",
        ],
        "field_methods": [
            "Mock trial / debate participation",
            "Case-brief writing practice",
            "Observing real court proceedings as a visitor, where permitted",
            "Moot court exercises",
        ],
        "tools_context": ["Legal research resources and case-law databases",
                           "Word processing tools for drafting documents"],
        "project_ideas": ["Moot court or mock trial participation", "Case law summary writing",
                           "Legal debate club involvement"],
        "project": None,
        "education_preparation": (
            "Practicing as a lawyer or advocate requires a formal law degree (e.g. a Bachelor of "
            "Laws / LLB) followed by bar council registration and a licensing/bar exam process -- "
            "this is a strictly regulated profession, and no amount of independent exploration "
            "substitutes for that formal qualification. What you can do now is build the underlying "
            "skills -- reading comprehension, argumentation, and research -- through debate, moot "
            "court, and reading real legal cases."
        ),
        "experience_ideas": {
            "+2 / High School": ["Join a debate club or take part in public-speaking competitions",
                                  "Read about a real court case and try to summarize both sides' "
                                  "arguments"],
            "Bachelor": ["Participate in moot court competitions",
                                   "Seek an internship or shadowing opportunity at a law firm or "
                                   "with a practicing advocate"],
            "Master": ["Pursue an LLM in a specialized area of interest",
                       "Seek research-assistant roles with faculty or practicing lawyers in that "
                       "specialization"],
        },
    },

    ("Public Service & Law", "Legal Consultant"): {
        "description": (
            "Legal consultants advise businesses, organizations, or individuals on specific legal "
            "matters -- such as compliance, contracts, or regulatory requirements -- without "
            "necessarily representing clients in court. The role often draws on legal training but "
            "is applied in a more advisory, business-facing way than courtroom litigation."
        ),
        "typical_activities": [
            "Reviewing contracts and legal documents for clients",
            "Advising organizations on regulatory compliance",
            "Researching applicable laws for a specific business situation",
            "Drafting policies or legal guidance documents",
            "Liaising between a client and external lawyers when litigation is needed",
            "Staying current on relevant regulatory changes",
        ],
        "useful_strengths": ["analytical_thinking", "research", "communication",
                              "problem_solving", "organization"],
        "critical_skills": ["analytical_thinking", "research", "communication",
                             "problem_solving", "organization"],
        "skill_importance": {"analytical_thinking": 0.85, "research": 0.8,
                              "communication": 0.7, "problem_solving": 0.65, "organization": 0.55},
        "useful_academic_areas": ["Business/Economics", "English", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2, "pref_tech_vs_people": 3,
        },
        "work_settings": ["Corporate legal / compliance departments", "Consulting firms",
                           "NGOs / INGOs", "Independent advisory practice"],
        "possible_directions": ["Corporate Compliance", "Contract Advisory",
                                 "Regulatory Affairs", "NGO / Non-profit Legal Advisory"],
        "foundational_topics": [
            "Basics of contract law",
            "Regulatory and compliance frameworks relevant to a sector",
            "Basic business fundamentals",
        ],
        "field_methods": [
            "Contract review practice",
            "Compliance checklist development",
            "Case-study analysis of real regulatory issues",
        ],
        "tools_context": ["Legal research resources and databases",
                           "Document review and word processing tools",
                           "Spreadsheets for compliance tracking"],
        "project_ideas": ["Sample contract review exercise", "Compliance checklist for a small business",
                           "Regulatory change briefing note"],
        "project": {
            "title": "Small Business Compliance Checklist",
            "steps": [
                "Pick a small local business type (e.g. a shop, cafe, or startup)",
                "Research the basic legal and regulatory requirements that apply to it",
                "Organize your findings into a simple checklist",
                "Note which requirements seem most commonly overlooked",
                "Present it as a short advisory note, as if for that business owner",
            ],
        },
        "education_preparation": (
            "A law degree is the most common foundation for this role, though some legal "
            "consultants combine legal training with business or sector-specific expertise; unlike "
            "courtroom advocacy, this path leans more on applied advisory skills and often benefits "
            "from exposure to a specific industry."
        ),
        "experience_ideas": {
            "+2 / High School": ["Read about how businesses handle legal compliance in a field "
                                 "you're interested in",
                                 "Follow business and regulatory news"],
            "Bachelor": ["Seek internships in a corporate legal or compliance department",
                         "Take a business law or contracts elective if available"],
            "Master": ["Consider an LLM or specialized certification in a compliance-heavy area "
                       "(e.g. corporate, labor, or data law)",
                       "Build sector expertise (e.g. finance, healthcare) alongside legal knowledge"],
        },
    },

    # ---------------------------------------------------------------
    # Education
    # ---------------------------------------------------------------

    ("Education", "School Teacher"): {
        "description": (
            "School teachers plan and deliver lessons, assess student learning, and manage "
            "classroom dynamics for a specific subject and age group. The role involves daily "
            "direct interaction with students, ongoing lesson preparation, and regular "
            "communication with parents/guardians and school administration."
        ),
        "typical_activities": [
            "Planning lessons and preparing teaching materials",
            "Delivering classroom instruction",
            "Grading assignments and tests and giving feedback",
            "Managing classroom behavior and student engagement",
            "Communicating with parents about student progress",
            "Participating in school events and staff meetings",
        ],
        "useful_strengths": ["communication", "organization", "creativity",
                              "leadership", "teamwork"],
        "critical_skills": ["communication", "organization", "creativity",
                             "leadership", "teamwork"],
        "skill_importance": {"communication": 0.85, "organization": 0.75,
                              "creativity": 0.6, "leadership": 0.55, "teamwork": 0.5},
        "useful_academic_areas": ["English", "Mathematics", "Science", "Arts"],
        "work_preferences": {
            "pref_people_vs_independent": 5, "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 5,
        },
        "work_settings": ["Public or private schools", "Classrooms",
                           "After-school or tutoring programs"],
        "possible_directions": ["Primary Education", "Secondary Subject Teaching",
                                 "Special Education", "School Administration / Leadership track"],
        "foundational_topics": [
            "Basics of child and adolescent development",
            "Lesson planning fundamentals",
            "Classroom management approaches",
            "Subject-specific teaching methods",
        ],
        "field_methods": [
            "Observing experienced teachers' classrooms",
            "Practice lesson delivery / microteaching",
            "Creating and testing simple lesson plans",
        ],
        "tools_context": ["Presentation and slide tools for lessons",
                           "Printed worksheets and teaching materials"],
        "project_ideas": ["Design a lesson plan for one topic", "Peer microteaching session",
                           "Simple classroom activity kit"],
        "project": {
            "title": "Mini Lesson Plan and Microteaching",
            "steps": [
                "Choose one topic in a subject you know well",
                "Design a 20-30 minute lesson plan that includes an activity",
                "Practice teaching it to a few friends, family, or peers",
                "Ask for honest feedback on clarity and engagement",
                "Revise the lesson based on that feedback",
            ],
        },
        "education_preparation": (
            "Most school teaching positions require a bachelor's degree, often in education or "
            "the subject taught, plus, in many systems, a teaching license or completion of a "
            "teacher-training program; practical classroom experience through student teaching or "
            "tutoring is typically expected before independent teaching."
        ),
        "experience_ideas": {
            "+2 / High School": ["Tutor a younger student in a subject you're strong in",
                                  "Volunteer as a teaching assistant at a local school or coaching "
                                  "center"],
            "Bachelor": ["Complete a student-teaching or practicum placement",
                         "Take on regular tutoring to practice explaining concepts clearly"],
            "Master": ["Pursue a specialization (special education, subject-specific pedagogy, etc.)",
                       "Take on a mentoring or curriculum-development role at a school"],
        },
    },

    ("Education", "University Professor"): {
        "description": (
            "University professors teach courses at the tertiary level, conduct original research "
            "in their field, and publish academic work, while also supervising students and "
            "taking part in departmental or institutional service. The balance between teaching "
            "and research varies by institution and role type."
        ),
        "typical_activities": [
            "Preparing and delivering lectures or seminars",
            "Conducting original research and writing academic papers",
            "Supervising graduate students' thesis work",
            "Reviewing manuscripts or serving on academic committees",
            "Applying for research grants or funding",
            "Attending and presenting at academic conferences",
        ],
        "useful_strengths": ["research", "analytical_thinking", "communication",
                              "presentation", "organization"],
        "critical_skills": ["research", "analytical_thinking", "communication",
                             "presentation", "organization"],
        "skill_importance": {"research": 0.9, "analytical_thinking": 0.8,
                              "communication": 0.65, "presentation": 0.6, "organization": 0.5},
        "useful_academic_areas": ["Science", "Mathematics", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 1,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 1, "pref_tech_vs_people": 3,
        },
        "work_settings": ["Universities and colleges", "Research labs",
                           "Academic conferences", "Graduate supervision settings"],
        "possible_directions": ["Teaching-focused Faculty", "Research-focused Faculty",
                                 "Department / Program Leadership", "Applied / Industry-linked Research"],
        "foundational_topics": [
            "Deep subject-matter grounding in a chosen discipline",
            "Basics of academic research methodology",
            "Academic writing and publishing norms",
        ],
        "field_methods": [
            "Literature review practice",
            "Designing a small independent research study",
            "Exposure to how academic peer review works",
        ],
        "tools_context": ["Reference management software", "Statistical or analysis tools "
                           "relevant to the discipline", "Presentation tools for conferences"],
        "project_ideas": ["Small literature review on a topic", "Mini independent research study",
                           "Conference-style presentation practice"],
        "project": {
            "title": "Mini Literature Review",
            "steps": [
                "Choose a narrow topic within a subject you're interested in",
                "Find and read 5-8 relevant articles or sources",
                "Summarize the key findings and debates in your own words",
                "Identify a gap or open question in what you read",
                "Write a short structured review",
                "Optionally, present it to peers and take questions",
            ],
        },
        "education_preparation": (
            "University faculty positions typically require a master's degree at minimum and, for "
            "most research-track roles, a PhD in the relevant discipline, followed by years of "
            "research and publishing before a faculty position; the path is long and "
            "research-intensive, so genuine, sustained interest in a specific subject matters more "
            "than general academic strength alone."
        ),
        "experience_ideas": {
            "+2 / High School": ["Pursue independent projects or reading well beyond the school "
                                 "curriculum in a subject of interest",
                                 "Enter academic competitions or science/humanities fairs"],
            "Bachelor": ["Seek a research assistantship with a faculty member",
                         "Present a project at an undergraduate research symposium if available"],
            "Master": ["Begin publishing or presenting research at conferences",
                       "Pursue or apply for PhD programs in your specialization"],
        },
    },

    ("Education", "Education Counselor"): {
        "description": (
            "Education counselors help students navigate academic planning, course or college "
            "selection, and personal or social challenges that affect their learning. The role "
            "blends listening and advising with practical knowledge of academic pathways, "
            "application processes, and available support resources."
        ),
        "typical_activities": [
            "Meeting one-on-one with students to discuss academic or personal concerns",
            "Advising on subject, stream, or college/program selection",
            "Helping students and families understand application and admission processes",
            "Identifying students who need additional academic or emotional support",
            "Coordinating with teachers and parents",
            "Running workshops on study skills or career awareness",
        ],
        "useful_strengths": ["communication", "problem_solving", "organization",
                              "research", "teamwork"],
        "critical_skills": ["communication", "problem_solving", "organization",
                             "research", "teamwork"],
        "skill_importance": {"communication": 0.85, "problem_solving": 0.7,
                              "organization": 0.6, "research": 0.55, "teamwork": 0.5},
        "useful_academic_areas": ["English", "Arts", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 5, "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2, "pref_tech_vs_people": 5,
        },
        "work_settings": ["Schools", "Colleges and universities", "Private counseling practices",
                           "Education consultancies"],
        "possible_directions": ["School Academic Counseling", "College / Admissions Counseling",
                                 "Career Counseling", "Student Wellbeing Support"],
        "foundational_topics": [
            "Academic pathway and stream options and their requirements",
            "Basics of active listening and non-judgmental advising",
            "Awareness of college admission and application processes",
        ],
        "field_methods": [
            "Practicing active-listening conversations",
            "Mock advising sessions with peers",
            "Building and maintaining a resource list of programs or pathways",
        ],
        "tools_context": ["Information resources on academic programs",
                           "Simple record-keeping for student notes and appointments"],
        "project_ideas": ["Study pathway resource guide", "Mock advising session practice",
                           "Study-skills mini workshop"],
        "project": {
            "title": "Academic Pathway Resource Guide",
            "steps": [
                "Pick a specific decision point (e.g. choosing a stream after +2, or a major after "
                "bachelor's)",
                "Research the realistic options and requirements for that decision",
                "Talk to 2-3 people who made that choice about their experience",
                "Compile what you learned into a simple guide",
                "Share it with someone actually facing that decision",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in psychology, education, or a related field is a common starting "
            "point, with many counseling roles preferring or requiring further training or "
            "certification in counseling; being comfortable having honest, sometimes difficult "
            "conversations matters as much as subject knowledge."
        ),
        "experience_ideas": {
            "+2 / High School": ["Volunteer as a peer mentor for younger students",
                                  "Practice helping friends think through their own academic "
                                  "decisions"],
            "Bachelor": ["Seek an internship or volunteer role in a school counseling office",
                         "Take an introductory psychology or counseling course"],
            "Master": ["Pursue certification or a specialized degree in counseling if required in "
                       "your context",
                       "Seek a supervised counseling practicum placement"],
        },
    },

    ("Education", "Instructional Designer"): {
        "description": (
            "Instructional designers plan and create structured learning materials -- courses, "
            "training modules, or curricula -- often for schools, companies, or online learning "
            "platforms. The work combines understanding how people learn with organizing content "
            "into a clear, effective sequence, frequently using digital tools to build and deliver "
            "the material."
        ),
        "typical_activities": [
            "Analyzing what learners need to know and their current skill level",
            "Structuring content into a logical learning sequence or curriculum",
            "Writing and designing learning materials (text, activities, assessments)",
            "Building courses in learning-management or e-learning tools",
            "Testing materials with a small group and revising based on feedback",
            "Collaborating with subject-matter experts to gather accurate content",
        ],
        "useful_strengths": ["organization", "creativity", "communication",
                              "analytical_thinking", "technical_ability"],
        "critical_skills": ["organization", "creativity", "communication",
                             "analytical_thinking", "technical_ability"],
        "skill_importance": {"organization": 0.8, "creativity": 0.75,
                              "communication": 0.65, "analytical_thinking": 0.6,
                              "technical_ability": 0.55},
        "useful_academic_areas": ["Computer", "English", "Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 2, "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 2,
        },
        "work_settings": ["EdTech companies", "Corporate training / L&D departments",
                           "Online learning platforms", "Schools/universities (curriculum teams)"],
        "possible_directions": ["Corporate Training / L&D", "K-12 Curriculum Design",
                                 "Higher-Ed Online Course Design", "E-learning Content Development"],
        "foundational_topics": [
            "Basics of learning theory -- how people learn and retain information",
            "Curriculum and course-structuring principles",
            "Basics of assessment design",
        ],
        "field_methods": [
            "Piloting a lesson or module with a small test group and gathering feedback",
            "Storyboarding a course before building it",
        ],
        "tools_context": ["E-learning authoring tools", "Learning management systems (LMS)",
                           "Presentation and multimedia design tools"],
        "project_ideas": ["Build a mini online course module", "Storyboard a training session",
                           "Redesign an existing lesson for clarity"],
        "project": {
            "title": "Mini Learning Module",
            "steps": [
                "Pick a small skill or topic to teach (something you know well)",
                "Define clear learning objectives for it",
                "Structure the content into a short sequence with an activity and a quick check "
                "for understanding",
                "Build it using a simple tool (slides, a document, or a free e-learning tool)",
                "Test it with 2-3 people and gather feedback",
                "Revise it based on what you learned",
            ],
        },
        "education_preparation": (
            "There isn't one fixed entry path -- backgrounds in education, psychology, "
            "communications, or a specific subject area combined with self-taught or formal "
            "training in instructional design tools and methods are all common; building a "
            "portfolio of sample learning materials matters more than a specific degree title."
        ),
        "experience_ideas": {
            "+2 / High School": ["Create simple study guides or explainer materials for a subject "
                                 "and get feedback from classmates",
                                 "Explore free tutorials on basic instructional design or "
                                 "e-learning tools"],
            "Bachelor": ["Volunteer to create training or onboarding materials for a club, event, "
                        "or part-time job",
                        "Build a small sample e-learning module using a free tool to start a "
                        "portfolio"],
            "Master": ["Pursue a formal instructional design or educational technology course or "
                       "certification if targeting this professionally",
                       "Take on a learning-design project with real learners to test and refine "
                       "your approach"],
        },
    },

    # --- from group4_healthcare_engineering.py ---
    # -----------------------------------------------------------
    # Healthcare & Medicine
    # -----------------------------------------------------------

    ("Healthcare & Medicine", "Medical Doctor"): {
        "description": (
            "Medical doctors diagnose and treat illness and injury -- taking patient "
            "histories, examining patients, ordering and interpreting tests, and "
            "deciding on treatment. Medicine is a licensed clinical profession: this "
            "roadmap is about exploring and preparing for that path, not a substitute "
            "for the required formal education, licensing exam, and clinical training."
        ),
        "typical_activities": [
            "Taking patient histories and performing physical examinations",
            "Ordering and interpreting diagnostic tests",
            "Diagnosing conditions and deciding on a treatment plan",
            "Prescribing and monitoring medication or other treatment",
            "Referring patients to specialists when a case needs it",
            "Keeping accurate, legally required clinical records",
        ],
        "useful_strengths": ["analytical_thinking", "problem_solving", "communication",
                              "research", "organization"],
        "critical_skills": ["analytical_thinking", "problem_solving", "communication",
                             "research", "organization"],
        "skill_importance": {
            "analytical_thinking": 1.0, "problem_solving": 0.9, "communication": 0.8,
            "research": 0.6, "organization": 0.55,
        },
        "useful_academic_areas": ["Science", "Mathematics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 4, "pref_creative_vs_analytical": 1,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 4,
        },
        "work_settings": ["Hospitals", "Clinics", "Private practice", "Emergency/trauma centers",
                           "Public/rural health services"],
        "possible_directions": ["General practice / family medicine",
                                 "Specialization via residency (e.g. surgery, pediatrics)",
                                 "Public or rural health service", "Research & academic medicine"],
        "foundational_topics": [
            "What day-to-day medical practice actually involves across specialties",
            "The formal education path required (a recognized medical degree, a "
            "licensing exam, and registration with a medical council) -- this varies "
            "by country and must be confirmed locally",
            "Basic human biology, chemistry, and anatomy as background reading",
            "The distinction between general practice and specialist residency training",
        ],
        "field_methods": [
            "Shadowing or observing clinical settings only where formally arranged",
            "Studying structured clinical reasoning as a concept (history, exam, "
            "differential diagnosis), not practicing it on real patients",
            "Reading case studies and basic medical literature critically",
        ],
        "tools_context": [],
        "project_ideas": ["Human-body-systems study guide", "Interview a doctor about their specialty",
                           "Summary write-up of a public health case study"],
        "project": None,  # deliberately no "build a project" step for a clinical, licensed field
        "education_preparation": (
            "Practicing medicine requires completing a recognized medical degree "
            "(e.g. MBBS or equivalent), passing a licensing examination, and "
            "registering with the relevant national medical council -- exact "
            "pathways and durations vary by country. This roadmap supports "
            "exploration and academic preparation only; it does not substitute "
            "for that formal training."
        ),
        "experience_ideas": {
            "+2 / High School": ["Research accredited medical programs and their (often "
                                  "competitive) entry requirements", "Talk to a working doctor "
                                  "about their day-to-day work and career path",
                                  "Build strong foundations in biology, chemistry, and physics"],
            "Bachelor": ["Confirm you're enrolled in (or applying to) an accredited medical "
                        "program", "Focus on your program's supervised clinical rotations -- "
                        "that structured training is what actually builds clinical competence"],
            "Master": ["Consider a specialization via residency/postgraduate training",
                      "Look for structured research or clinical exposure in your area of interest"],
        },
    },

    ("Healthcare & Medicine", "Public Health Officer"): {
        "description": (
            "Public health officers work on population-level health rather than "
            "treating individual patients -- tracking disease trends, designing and "
            "evaluating health programs, coordinating outbreak response, and shaping "
            "health policy. The work sits across government, hospitals, and NGOs "
            "rather than in one clinic."
        ),
        "typical_activities": [
            "Monitoring disease trends and health data across a population",
            "Designing and evaluating public health programs or campaigns",
            "Coordinating outbreak investigation and response",
            "Working with government agencies and NGOs on health policy",
            "Communicating health guidance to communities and media",
            "Analyzing health statistics to guide decisions and funding",
        ],
        "useful_strengths": ["analytical_thinking", "research", "communication",
                              "organization", "leadership"],
        "critical_skills": ["analytical_thinking", "research", "communication",
                             "organization", "leadership"],
        "skill_importance": {
            "analytical_thinking": 0.9, "research": 0.85, "communication": 0.75,
            "organization": 0.6, "leadership": 0.55,
        },
        "useful_academic_areas": ["Science", "Mathematics", "Business/Economics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 4, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 2, "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2, "pref_tech_vs_people": 4,
        },
        "work_settings": ["Government health departments", "Public health agencies / NGOs",
                           "Hospitals & health systems (program roles)", "Research institutions",
                           "Field / outbreak response sites"],
        "possible_directions": ["Epidemiology & disease surveillance",
                                 "Health policy & program management",
                                 "Health promotion / community outreach",
                                 "Health systems research"],
        "foundational_topics": [
            "How population/public health differs from individual clinical care",
            "Basic epidemiology concepts (incidence, prevalence, outbreak investigation)",
            "How health data is collected and used to guide policy and funding",
            "Common education paths (a public health degree, sometimes alongside a "
            "clinical background) -- this varies by country",
        ],
        "field_methods": [
            "Reading and interpreting basic health statistics",
            "Program planning and evaluation frameworks",
            "Community needs assessment",
            "Health communication and risk messaging",
        ],
        "tools_context": ["Basic epidemiology software (e.g. Epi Info)",
                           "Excel or statistical software for health data",
                           "GIS mapping tools (for disease mapping)"],
        "project_ideas": ["Local health awareness campaign", "Simple disease-trend data summary",
                           "Community health needs survey"],
        "project": {
            "title": "Community Health Awareness Campaign",
            "steps": [
                "Pick a real, local public health issue (e.g. hygiene, nutrition, a "
                "common illness)",
                "Research basic facts and existing official guidance about it",
                "Design a simple awareness campaign (poster, talk, or social content)",
                "Share it with a real audience (school, community group) if possible",
                "Reflect on what worked and what you'd improve",
            ],
        },
        "education_preparation": (
            "Public health roles typically require a degree in public health, "
            "epidemiology, or a related field (sometimes building on a prior clinical "
            "or science background); requirements vary by country and by role."
        ),
        "experience_ideas": {
            "+2 / High School": ["Follow how a real public health campaign or outbreak "
                                  "response was communicated to the public", "Volunteer with "
                                  "a health-awareness or community organization"],
            "Bachelor": ["Look for an internship with a public health agency, NGO, or "
                        "hospital program team", "Take an intro epidemiology or biostatistics "
                        "course if available"],
            "Master": ["Seek a structured field placement in epidemiology or program "
                      "management", "Take on a small applied research or program-evaluation "
                      "project"],
        },
    },

    ("Healthcare & Medicine", "Pharmacist"): {
        "description": (
            "Pharmacists dispense medication safely, check for interactions and "
            "allergies, and counsel patients on correct use, working closely with "
            "doctors to make sure treatment is appropriate and safe. Pharmacy is a "
            "licensed clinical profession: this roadmap is about exploring and "
            "preparing for that path, not a substitute for the required formal "
            "education and licensing."
        ),
        "typical_activities": [
            "Reviewing prescriptions for accuracy, dosage, and safety",
            "Dispensing medication and checking for interactions or allergies",
            "Counseling patients on how to take medication correctly",
            "Managing pharmacy inventory and storage of controlled substances",
            "Collaborating with doctors on treatment plans",
            "Staying current on new drugs and clinical guidelines",
        ],
        "useful_strengths": ["analytical_thinking", "organization", "communication",
                              "problem_solving"],
        "critical_skills": ["analytical_thinking", "organization", "communication",
                             "problem_solving"],
        "skill_importance": {
            "analytical_thinking": 0.95, "organization": 0.85, "communication": 0.7,
            "problem_solving": 0.6,
        },
        "useful_academic_areas": ["Science", "Mathematics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 1,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 1,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 3,
        },
        "work_settings": ["Retail / community pharmacies", "Hospital pharmacies",
                           "Pharmaceutical companies", "Public health / regulatory agencies"],
        "possible_directions": ["Community/retail pharmacy", "Hospital/clinical pharmacy",
                                 "Pharmaceutical industry (research or regulatory)",
                                 "Pharmacy academia"],
        "foundational_topics": [
            "What day-to-day pharmacy work involves across different settings",
            "The formal education path required (an accredited pharmacy degree and "
            "licensing exam/registration) -- this varies by country and must be "
            "confirmed locally",
            "Basic chemistry and human biology as background reading",
        ],
        "field_methods": [
            "Careful, methodical checking (dosage, interactions, allergies)",
            "Clear patient-counseling communication",
            "Accurate inventory and record-keeping practices",
        ],
        "tools_context": [],
        "project_ideas": ["Drug-interaction reference summary", "Medication-safety awareness leaflet",
                           "Interview a pharmacist about daily practice"],
        "project": None,  # deliberately no "build a project" step for a clinical, licensed field
        "education_preparation": (
            "Practicing as a pharmacist requires completing an accredited pharmacy "
            "degree, followed by a licensing exam and registration with the relevant "
            "pharmacy council -- exact pathways vary by country. This roadmap supports "
            "exploration and academic preparation only; it does not substitute for "
            "that formal training."
        ),
        "experience_ideas": {
            "+2 / High School": ["Research accredited pharmacy programs and their entry "
                                  "requirements", "Talk to a working pharmacist about their "
                                  "day-to-day work"],
            "Bachelor": ["Confirm you're enrolled in (or applying to) an accredited pharmacy "
                        "program", "Focus on your program's supervised practical placements -- "
                        "that structured training is what actually builds competence"],
            "Master": ["Consider a specialization (e.g. clinical or hospital pharmacy) through "
                      "formal advanced study", "Look for structured research or clinical "
                      "exposure in your area of interest"],
        },
    },

    ("Healthcare & Medicine", "Dentist"): {
        "description": (
            "Dentists diagnose and treat problems with teeth, gums, and the mouth -- "
            "from routine cleanings and fillings to more complex procedures -- and "
            "educate patients on oral health. Dentistry is a licensed clinical "
            "profession: this roadmap is about exploring and preparing for that path, "
            "not a substitute for the required formal education and clinical training."
        ),
        "typical_activities": [
            "Examining teeth, gums, and the mouth for problems",
            "Performing procedures such as fillings, extractions, and cleanings",
            "Taking and reading dental X-rays",
            "Educating patients on oral hygiene and prevention",
            "Managing patient anxiety and comfort during procedures",
            "Maintaining clinical records and sterilization protocols",
        ],
        "useful_strengths": ["technical_ability", "analytical_thinking", "communication",
                              "problem_solving"],
        "critical_skills": ["technical_ability", "analytical_thinking", "communication",
                             "problem_solving"],
        "skill_importance": {
            "technical_ability": 0.95, "analytical_thinking": 0.8, "communication": 0.65,
            "problem_solving": 0.6,
        },
        "useful_academic_areas": ["Science", "Mathematics", "Arts"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 5, "pref_tech_vs_people": 3,
        },
        "work_settings": ["Private dental clinics", "Hospitals (dental/maxillofacial units)",
                           "Community dental health programs", "Dental schools / academia"],
        "possible_directions": ["General/family dentistry",
                                 "Orthodontics (with further specialization)",
                                 "Oral surgery (with further specialization)",
                                 "Public dental health"],
        "foundational_topics": [
            "What day-to-day dental practice involves",
            "The formal education path required (an accredited dental degree and "
            "licensing/registration) -- this varies by country and must be confirmed "
            "locally",
            "Basic human biology and oral anatomy as background reading",
            "Fine motor precision as a core, learnable requirement of the field",
        ],
        "field_methods": [
            "Studying clinical observation and record-keeping as a concept, not practice",
            "Patient communication and comfort-management approaches",
            "Understanding strict hygiene and sterilization protocols",
        ],
        "tools_context": [],
        "project_ideas": ["Oral hygiene awareness guide", "Interview a dentist about daily practice",
                           "Dental anatomy study guide"],
        "project": None,  # deliberately no "build a project" step for a clinical, licensed field
        "education_preparation": (
            "Practicing as a dentist requires completing an accredited dental degree, "
            "followed by a licensing exam and registration with the relevant dental "
            "council -- exact pathways vary by country. This roadmap supports "
            "exploration and academic preparation only; it does not substitute for "
            "that formal training."
        ),
        "experience_ideas": {
            "+2 / High School": ["Research accredited dental programs and their entry "
                                  "requirements", "Talk to a working dentist about their "
                                  "day-to-day work"],
            "Bachelor": ["Confirm you're enrolled in (or applying to) an accredited dental "
                        "program", "Focus on your program's supervised clinical placements -- "
                        "that structured training is what actually builds clinical competence"],
            "Master": ["Consider a specialization track (e.g. orthodontics, oral surgery) "
                      "through formal advanced study", "Look for structured clinical or "
                      "research exposure in your area of interest"],
        },
    },

    # -----------------------------------------------------------
    # Engineering
    # -----------------------------------------------------------

    ("Engineering", "Civil Engineer"): {
        "description": (
            "Civil engineers design, plan, and oversee construction of infrastructure "
            "-- roads, bridges, buildings, water systems -- balancing safety, cost, "
            "and regulation across a project's life from design through construction."
        ),
        "typical_activities": [
            "Designing structural elements (foundations, beams, load paths)",
            "Conducting site surveys and soil/material testing",
            "Preparing technical drawings and specifications",
            "Supervising construction sites and quality checks",
            "Ensuring designs meet safety codes and regulations",
            "Estimating project costs and timelines",
        ],
        "useful_strengths": ["analytical_thinking", "technical_ability", "problem_solving",
                              "organization"],
        "critical_skills": ["analytical_thinking", "technical_ability", "problem_solving",
                             "organization"],
        "skill_importance": {
            "analytical_thinking": 0.9, "technical_ability": 0.85, "problem_solving": 0.75,
            "organization": 0.6,
        },
        "useful_academic_areas": ["Mathematics", "Science", "Computer", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 4, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 2,
        },
        "work_settings": ["Construction sites", "Engineering design offices",
                           "Government infrastructure departments", "Consulting firms"],
        "possible_directions": ["Structural engineering", "Transportation/highway engineering",
                                 "Water resources engineering", "Construction management"],
        "foundational_topics": [
            "Statics and basic structural principles (loads, forces, materials)",
            "How a construction project moves from design to completion",
            "Reading technical/engineering drawings",
        ],
        "field_methods": [
            "Basic site surveying",
            "Material testing concepts (concrete, soil)",
            "Structural load calculations",
            "Reading and producing technical drawings",
        ],
        "tools_context": ["AutoCAD", "Basic structural analysis software", "Surveying tools / GPS"],
        "project_ideas": ["Small structure design exercise", "Local infrastructure survey",
                           "Basic bridge-load calculation"],
        "project": {
            "title": "Small Structure Design Exercise",
            "steps": [
                "Pick a simple structure to model (a footbridge, small shed, or ramp)",
                "Sketch the design and identify the main loads it needs to handle",
                "Do basic hand calculations or use free structural software to check it",
                "Draw it up cleanly using a CAD tool (even a free one)",
                "Write a short explanation of your design choices and trade-offs",
            ],
        },
        "education_preparation": (
            "A career as a civil engineer typically requires an accredited "
            "engineering degree; professional practice in many countries also "
            "involves further licensing (e.g. a professional engineer exam) after "
            "some years of supervised experience."
        ),
        "experience_ideas": {
            "+2 / High School": ["Take an intro physics/mechanics course seriously -- it's "
                                  "the foundation of this field", "Look at how a local "
                                  "construction project is built and sequenced"],
            "Bachelor": ["Look for a site-engineering or design-office internship",
                        "Join a student engineering or design competition"],
            "Master": ["Specialize in one area (structural, water resources, transportation) "
                      "through advanced coursework", "Seek a research or design role with "
                      "real project exposure"],
        },
    },

    ("Engineering", "Electrical Engineer"): {
        "description": (
            "Electrical engineers design and work with systems that use electricity -- "
            "from power distribution and machinery to electronics and control systems "
            "-- covering both large-scale power infrastructure and smaller circuit-"
            "level design depending on specialization."
        ),
        "typical_activities": [
            "Designing and testing circuits and electrical systems",
            "Working with power distribution, wiring, and safety standards",
            "Troubleshooting electrical faults and equipment issues",
            "Using simulation software to model circuit behavior",
            "Reading and producing electrical schematics",
            "Coordinating with other engineering disciplines on shared projects",
        ],
        "useful_strengths": ["technical_ability", "analytical_thinking", "problem_solving",
                              "research"],
        "critical_skills": ["technical_ability", "analytical_thinking", "problem_solving",
                             "research"],
        "skill_importance": {
            "technical_ability": 0.9, "analytical_thinking": 0.85, "problem_solving": 0.75,
            "research": 0.5,
        },
        "useful_academic_areas": ["Mathematics", "Science", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 2, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 2, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 1,
        },
        "work_settings": ["Power/utility companies", "Electronics & manufacturing firms",
                           "Engineering design offices", "Construction & building services",
                           "Research labs"],
        "possible_directions": ["Power systems engineering", "Electronics/circuit design",
                                 "Control & automation systems", "Telecommunications engineering"],
        "foundational_topics": [
            "Basic circuit theory (voltage, current, resistance, Ohm's law)",
            "The difference between power-systems work and electronics/signal work",
            "Reading electrical schematics and safety symbols",
        ],
        "field_methods": [
            "Breadboarding and basic circuit testing",
            "Using a multimeter and basic test equipment",
            "Simulating a circuit before building it physically",
            "Following electrical safety standards",
        ],
        "tools_context": ["MATLAB/Simulink", "Circuit simulation software (e.g. LTspice)",
                           "Basic electronics kit (breadboard, multimeter)"],
        "project_ideas": ["Simple circuit build and test", "Sensor-based alarm project",
                           "Home wiring safety review (observation only)"],
        "project": {
            "title": "Simple Circuit Build & Test",
            "steps": [
                "Pick a small, safe circuit idea (an LED sequencer, sensor-based alarm)",
                "Design the circuit and simulate it in free software first",
                "Build it on a breadboard with basic components",
                "Test and troubleshoot until it works as intended",
                "Document the design with a schematic and short write-up",
            ],
        },
        "education_preparation": (
            "A career as an electrical engineer typically requires an accredited "
            "engineering degree; professional practice in many countries also "
            "involves further licensing after some years of supervised experience, "
            "particularly for power-systems and infrastructure work."
        ),
        "experience_ideas": {
            "+2 / High School": ["Try a beginner electronics kit and build a few simple "
                                  "circuits", "Take physics seriously, especially electricity "
                                  "and magnetism topics"],
            "Bachelor": ["Look for an electronics, power, or automation internship",
                        "Join a student robotics or electronics club/competition"],
            "Master": ["Specialize in one area (power, electronics, control systems) through "
                      "advanced coursework", "Seek a research or design role with real "
                      "hardware exposure"],
        },
    },

    ("Engineering", "Mechanical Engineer"): {
        "description": (
            "Mechanical engineers design, analyze, and build physical systems and "
            "machines -- engines, tools, manufacturing equipment, mechanical "
            "components -- applying principles of motion, force, and energy across "
            "design and manufacturing."
        ),
        "typical_activities": [
            "Designing mechanical parts and assemblies using CAD software",
            "Analyzing forces, stresses, and material behavior in a design",
            "Prototyping and testing physical components",
            "Working within manufacturing processes and tolerances",
            "Troubleshooting mechanical failures",
            "Collaborating with manufacturing and quality teams",
        ],
        "useful_strengths": ["technical_ability", "analytical_thinking", "problem_solving",
                              "creativity"],
        "critical_skills": ["technical_ability", "analytical_thinking", "problem_solving",
                             "creativity"],
        "skill_importance": {
            "technical_ability": 0.9, "analytical_thinking": 0.8, "problem_solving": 0.75,
            "creativity": 0.55,
        },
        "useful_academic_areas": ["Mathematics", "Science", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 2, "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 2, "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 4, "pref_tech_vs_people": 1,
        },
        "work_settings": ["Manufacturing plants", "Engineering design offices",
                           "Automotive/aerospace companies", "Product design & prototyping labs",
                           "Maintenance & operations"],
        "possible_directions": ["Design & product engineering", "Manufacturing/production engineering",
                                 "Automotive/aerospace engineering", "HVAC & thermal systems"],
        "foundational_topics": [
            "Basic mechanics (forces, motion, energy)",
            "How a CAD model translates into a manufactured part",
            "Material properties and how they shape design choices",
        ],
        "field_methods": [
            "Hand sketching before CAD modeling",
            "Basic prototyping (3D printing, simple fabrication)",
            "Tolerance and fit considerations in design",
            "Basic failure analysis",
        ],
        "tools_context": ["SolidWorks or Fusion 360", "A basic 3D printer (for prototyping)",
                           "Simulation software (stress/thermal analysis)"],
        "project_ideas": ["Simple mechanical device prototype", "3D-printed tool or part",
                           "Basic machine-failure case study"],
        "project": {
            "title": "Simple Mechanical Device Prototype",
            "steps": [
                "Pick a small mechanical problem to solve (a simple tool, holder, or "
                "mechanism)",
                "Sketch a few design concepts by hand",
                "Model your chosen design in free CAD software",
                "3D print or build a rough physical prototype if possible",
                "Test it, note what fails or works, and refine the design",
            ],
        },
        "education_preparation": (
            "A career as a mechanical engineer typically requires an accredited "
            "engineering degree; professional practice in many countries also "
            "involves further licensing after some years of supervised experience, "
            "particularly for safety-critical design work."
        ),
        "experience_ideas": {
            "+2 / High School": ["Take things apart (safely) to see how mechanisms work",
                                  "Try a free intro CAD tutorial (Fusion 360, Tinkercad)"],
            "Bachelor": ["Look for a design or manufacturing internship",
                        "Join a student design-build competition (e.g. a robotics or "
                        "formula-style team)"],
            "Master": ["Specialize in one area (design, manufacturing, thermal/fluids) "
                      "through advanced coursework", "Seek a research or product-development "
                      "role with real prototyping exposure"],
        },
    },

    ("Engineering", "Environmental Engineer"): {
        "description": (
            "Environmental engineers apply engineering principles to protect the "
            "environment and public health -- designing water and wastewater "
            "treatment systems, managing pollution control, and working on "
            "sustainability and regulatory-compliance projects."
        ),
        "typical_activities": [
            "Designing water and wastewater treatment processes",
            "Assessing pollution sources and environmental impact",
            "Ensuring projects comply with environmental regulations",
            "Sampling and testing air, water, or soil quality",
            "Working on waste management and recycling systems",
            "Preparing environmental impact reports",
        ],
        "useful_strengths": ["analytical_thinking", "research", "technical_ability",
                              "problem_solving"],
        "critical_skills": ["analytical_thinking", "research", "technical_ability",
                             "problem_solving"],
        "skill_importance": {
            "analytical_thinking": 0.85, "research": 0.75, "technical_ability": 0.7,
            "problem_solving": 0.65,
        },
        "useful_academic_areas": ["Mathematics", "Science", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 2, "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 4, "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 2,
        },
        "work_settings": ["Government environmental agencies", "Consulting firms",
                           "Water/utility companies", "Industrial compliance teams",
                           "Field sampling sites"],
        "possible_directions": ["Water & wastewater engineering", "Pollution control & remediation",
                                 "Environmental compliance/consulting",
                                 "Sustainability & waste management"],
        "foundational_topics": [
            "Basic environmental science (water cycles, pollution sources, ecosystems)",
            "How environmental regulations shape engineering projects",
            "Water/wastewater treatment fundamentals",
        ],
        "field_methods": [
            "Basic water/soil/air sampling",
            "Reading and interpreting environmental test results",
            "Environmental impact assessment basics",
        ],
        "tools_context": ["GIS mapping software", "Basic water-quality testing kits",
                           "Spreadsheet/statistical tools for environmental data"],
        "project_ideas": ["Local water quality study", "Waste management improvement proposal",
                           "Simple pollution-source mapping"],
        "project": {
            "title": "Local Water Quality Study",
            "steps": [
                "Identify a local water source you can safely observe (pond, stream, tap)",
                "Research which basic indicators matter for water quality",
                "Use a simple test kit or published data to check a few indicators",
                "Compare your findings to recommended safety standards",
                "Write a short report with your findings and recommendations",
            ],
        },
        "education_preparation": (
            "A career as an environmental engineer typically requires an accredited "
            "engineering degree, often with coursework in environmental science; some "
            "roles also involve professional licensing after supervised experience."
        ),
        "experience_ideas": {
            "+2 / High School": ["Follow local news on a real environmental issue (water, "
                                  "waste, air quality) in your area", "Take environmental "
                                  "science seriously alongside physics and chemistry"],
            "Bachelor": ["Look for an internship with an environmental agency or consulting "
                        "firm", "Join a campus sustainability or environmental project"],
            "Master": ["Specialize in one area (water treatment, pollution control, "
                      "sustainability) through advanced coursework", "Seek a research or "
                      "fieldwork role with real sampling/data exposure"],
        },
    },

    ("Engineering", "Architect"): {
        "description": (
            "Architects design buildings and spaces, balancing aesthetics, function, "
            "safety, and cost -- from initial concept sketches through detailed "
            "technical drawings used for construction. In most countries, architecture "
            "is a licensed profession: this roadmap is about exploring and preparing "
            "for that path, not a substitute for the required formal education and "
            "licensing."
        ),
        "typical_activities": [
            "Sketching and developing initial design concepts with clients",
            "Producing detailed technical drawings and building plans",
            "Balancing aesthetic vision with structural and budget constraints",
            "Ensuring designs comply with building codes and regulations",
            "Coordinating with engineers and contractors during construction",
            "Using 3D modeling software to visualize and refine designs",
        ],
        "useful_strengths": ["creativity", "technical_ability", "communication",
                              "analytical_thinking"],
        "critical_skills": ["creativity", "technical_ability", "communication",
                             "analytical_thinking"],
        "skill_importance": {
            "creativity": 0.9, "technical_ability": 0.8, "communication": 0.65,
            "analytical_thinking": 0.6,
        },
        "useful_academic_areas": ["Mathematics", "Science", "Arts", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 3, "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 2, "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3, "pref_tech_vs_people": 3,
        },
        "work_settings": ["Architecture firms", "Construction sites (for design oversight)",
                           "Government planning departments", "Freelance/independent practice"],
        "possible_directions": ["Residential architecture", "Commercial/institutional architecture",
                                 "Urban planning & design", "Interior architecture"],
        "foundational_topics": [
            "What day-to-day architectural practice involves, from concept to construction",
            "The formal education path required (an accredited architecture degree, "
            "commonly around five years, plus supervised training and professional "
            "licensing/registration) -- this varies by country and must be confirmed "
            "locally",
            "Basic design principles (space, light, proportion, materials)",
        ],
        "field_methods": [
            "Concept sketching and design iteration, as a study/hobby practice",
            "Reading architectural drawings and plans",
            "Understanding how building codes shape design decisions",
        ],
        "tools_context": ["SketchUp (free 3D design tool)", "Basic sketching/drafting practice"],
        "project_ideas": ["Concept sketch for a small building", "Study of a favorite building's design",
                           "Interview an architect about their process"],
        "project": None,  # deliberately no "build a project" step for a licensed design profession
        "education_preparation": (
            "Practicing as an architect requires completing an accredited "
            "architecture degree (commonly around five years), followed by a period "
            "of supervised practical training and professional licensing/registration "
            "-- requirements vary by country. This roadmap supports exploration and "
            "design-fundamentals preparation only; it is not a substitute for that "
            "formal training and licensing."
        ),
        "experience_ideas": {
            "+2 / High School": ["Sketch buildings or spaces you find interesting, just to "
                                  "practice observation", "Research accredited architecture "
                                  "programs and their entry requirements (often a portfolio "
                                  "or design aptitude test)"],
            "Bachelor": ["Confirm you're enrolled in (or applying to) an accredited "
                        "architecture program", "Focus on your program's studio work and "
                        "any supervised practical training -- that's what actually builds "
                        "professional competence"],
            "Master": ["Consider a specialization (e.g. urban design, sustainable "
                      "architecture) through formal advanced study", "Look for a structured "
                      "internship at a licensed architecture firm"],
        },
    },

    # --- from group5_media_research_agriculture.py ---
    ("Media & Communication", "Journalist"): {
        "description": (
            "Journalists research, verify, and report news and current events for print, "
            "broadcast, or online audiences. The work involves finding stories, interviewing "
            "sources, checking facts carefully, and writing under deadline pressure."
        ),
        "typical_activities": [
            "Researching and pitching story ideas",
            "Interviewing sources and eyewitnesses",
            "Verifying facts and cross-checking claims",
            "Writing and editing articles or news scripts",
            "Attending press conferences, events, or court hearings",
            "Meeting publication deadlines under time pressure",
        ],
        "useful_strengths": ["communication", "research", "analytical_thinking", "organization", "presentation"],
        "critical_skills": ["communication", "research", "analytical_thinking", "organization", "presentation"],
        "skill_importance": {
            "communication": 1.0,
            "research": 0.9,
            "analytical_thinking": 0.7,
            "organization": 0.6,
            "presentation": 0.5,
        },
        "useful_academic_areas": ["English", "Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 4,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 3,
            "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["Newsrooms", "Media houses", "Online publications",
                           "Freelance / remote reporting", "Press and event venues"],
        "possible_directions": ["Print / Digital News", "Broadcast Journalism",
                                 "Investigative Journalism", "Feature Writing"],
        "foundational_topics": ["Media ethics and law", "Interviewing techniques",
                                 "News writing style (inverted pyramid)"],
        "field_methods": ["Fact-checking and source verification", "Beat reporting",
                           "On-the-record vs. off-the-record source handling"],
        "tools_context": ["Word processors or newsroom CMS platforms", "Audio recorders for interviews",
                           "Basic photo or video editing (optional)"],
        "project_ideas": [
            "Cover a Local Event Story",
            "Start a Niche Newsletter",
            "Write an Investigative Mini-Report",
        ],
        "project": {
            "title": "Write and Publish a Local News Story",
            "steps": [
                "Pick a local issue or event worth covering",
                "Interview 2-3 people connected to it",
                "Research background facts and context",
                "Draft the article following a clear news-writing style",
                "Fact-check every claim and quote",
                "Edit for clarity, accuracy, and length",
                "Publish on a blog, student paper, or local outlet",
            ],
        },
        "education_preparation": (
            "A degree in journalism or mass communication can help, but it is not mandatory -- "
            "many journalists build credibility through a portfolio of published, well-researched "
            "pieces rather than credentials alone."
        ),
        "experience_ideas": {
            "+2 / High School": ["Write for a school newsletter or magazine",
                                  "Start a personal blog covering topics you care about"],
            "Bachelor": ["Intern at a local newspaper or media house",
                         "Contribute regularly to a student publication"],
            "Master": ["Pursue a specialized reporting focus (e.g. data or investigative journalism)",
                       "Work as a stringer or freelancer for an established outlet"],
        },
    },

    ("Media & Communication", "Content Creator"): {
        "description": (
            "Content creators produce video, written, or social media content for an online "
            "audience, often on a specific platform or niche. The work blends creative "
            "production with understanding what an audience wants and how platforms distribute it."
        ),
        "typical_activities": [
            "Planning and scripting content ideas",
            "Filming, recording, or writing content",
            "Editing video, audio, or images",
            "Reviewing engagement metrics to see what resonates",
            "Collaborating with brands or sponsors on partnerships",
            "Keeping up with platform trends and audience preferences",
        ],
        "useful_strengths": ["creativity", "communication", "organization", "technical_ability", "presentation"],
        "critical_skills": ["creativity", "communication", "technical_ability", "organization", "presentation"],
        "skill_importance": {
            "creativity": 1.0,
            "communication": 0.85,
            "technical_ability": 0.7,
            "organization": 0.6,
            "presentation": 0.55,
        },
        "useful_academic_areas": ["Arts", "Computer", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 5,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 5,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Home studio / self-employed", "Media or marketing agencies",
                           "Brand partnership projects", "Online platforms"],
        "possible_directions": ["Video / YouTube Content", "Short-form Social Content",
                                 "Podcasting", "Niche Blogging or Writing"],
        "foundational_topics": ["Storytelling basics", "Platform algorithms and audience building",
                                 "Basic video or photo editing"],
        "field_methods": ["Content calendar planning", "Analytics review and iteration",
                           "Trend and competitor research"],
        "tools_context": ["Smartphone camera or basic camera", "Video editing app (CapCut, Premiere)",
                           "Canva for graphics", "Platform-native analytics dashboards"],
        "project_ideas": [
            "Run a 30-Day Content Series",
            "Launch a Niche Topic Channel",
        ],
        "project": {
            "title": "30-Day Niche Content Challenge",
            "steps": [
                "Choose a specific niche or topic",
                "Plan a content calendar covering 30 days",
                "Create and post content consistently",
                "Track basic engagement metrics as you go",
                "Review what worked and what didn't",
                "Summarize the lessons learned",
            ],
        },
        "education_preparation": (
            "No formal degree is required -- consistency, a clear niche, and a genuine following "
            "matter most, though courses in media, marketing, or design can sharpen specific skills."
        ),
        "experience_ideas": {
            "+2 / High School": ["Start a personal social media account around a hobby",
                                  "Learn a free video or photo editing tool"],
            "Bachelor": ["Grow a niche account with consistent posting",
                         "Collaborate with peers on a joint content project"],
            "Master": ["Explore monetization or brand-partnership strategies",
                       "Study audience analytics to refine content decisions"],
        },
    },

    ("Media & Communication", "Radio/TV Presenter"): {
        "description": (
            "Radio and TV presenters host live or recorded broadcast segments -- news, "
            "entertainment, interviews, or talk shows -- delivering content clearly and "
            "engagingly to an audience, often while adapting to changes in real time."
        ),
        "typical_activities": [
            "Reading scripts or working from an autocue",
            "Hosting live shows, interviews, or call-in segments",
            "Interacting with guests, co-hosts, or callers",
            "Rehearsing segments before airing",
            "Adapting smoothly to live, on-air changes",
            "Coordinating with producers and directors on show flow",
        ],
        "useful_strengths": ["communication", "presentation", "creativity", "teamwork"],
        "critical_skills": ["communication", "presentation", "creativity", "teamwork"],
        "skill_importance": {
            "communication": 1.0,
            "presentation": 0.9,
            "creativity": 0.6,
            "teamwork": 0.55,
        },
        "useful_academic_areas": ["English", "Arts", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Radio studios", "TV studios", "Live event venues",
                           "Broadcast networks", "Online streaming platforms"],
        "possible_directions": ["News Anchoring", "Entertainment / Talk Shows",
                                 "Sports Commentary", "Radio Jockeying"],
        "foundational_topics": ["Voice and diction training", "On-air etiquette and timing",
                                 "Script reading and ad-libbing"],
        "field_methods": ["Rehearsal and voice warm-ups", "Live audience engagement techniques"],
        "tools_context": ["Teleprompter / autocue", "Basic audio or video setup for practice reels"],
        "project_ideas": [
            "Record a Mock Radio Show",
            "Host a Practice Interview Segment",
        ],
        "project": {
            "title": "Record a Mock Broadcast Segment",
            "steps": [
                "Choose a format (news update, talk segment, interview)",
                "Write or outline a script",
                "Practice voice modulation and pacing",
                "Record a 5-10 minute segment",
                "Review the recording for clarity and pace",
                "Get feedback from others and revise",
                "Re-record an improved version",
            ],
        },
        "education_preparation": (
            "Mass communication or broadcasting courses can help, but many presenters build a "
            "career through demo reels, hosting practice, and a strong, clear on-air presence "
            "rather than a specific degree."
        ),
        "experience_ideas": {
            "+2 / High School": ["Host school events or announcements",
                                  "Practice recording yourself and reviewing playback"],
            "Bachelor": ["Join a college radio or TV club",
                         "Build a short demo reel of hosting practice"],
            "Master": ["Seek an internship at a local radio or TV station",
                       "Take on freelance voiceover or hosting gigs"],
        },
    },

    ("Media & Communication", "Social Media Strategist"): {
        "description": (
            "Social media strategists plan and manage an organization's presence across "
            "platforms -- setting content direction, coordinating campaigns, and analyzing "
            "what is and isn't working to grow an audience or brand."
        ),
        "typical_activities": [
            "Planning content calendars across multiple platforms",
            "Analyzing engagement and performance data",
            "Coordinating with designers, writers, or videographers",
            "Running or overseeing paid social ad campaigns",
            "Monitoring brand mentions and industry trends",
            "Reporting performance results to stakeholders",
        ],
        "useful_strengths": ["analytical_thinking", "organization", "communication", "creativity", "technical_ability"],
        "critical_skills": ["analytical_thinking", "organization", "communication", "creativity", "technical_ability"],
        "skill_importance": {
            "analytical_thinking": 0.9,
            "organization": 0.85,
            "communication": 0.8,
            "creativity": 0.6,
            "technical_ability": 0.5,
        },
        "useful_academic_areas": ["Business/Economics", "Computer", "Arts"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 3,
        },
        "work_settings": ["Marketing / advertising agencies", "In-house brand teams",
                           "Startups", "Remote / freelance work"],
        "possible_directions": ["Brand Strategy", "Paid Social / Ads",
                                 "Community Management", "Analytics & Growth"],
        "foundational_topics": ["Social media analytics basics", "Campaign planning",
                                 "Target audience and persona research"],
        "field_methods": ["A/B testing content variations", "Competitor analysis",
                           "Engagement tracking over time"],
        "tools_context": ["Native platform analytics (Instagram/X Insights)", "Scheduling tools (Buffer, Hootsuite)",
                           "Spreadsheet software for reporting", "Canva for quick assets"],
        "project_ideas": [
            "Grow a Small Brand's Social Page",
            "Write a Social Media Audit Report",
        ],
        "project": {
            "title": "Social Media Growth Plan for a Small Business",
            "steps": [
                "Pick a real or fictional small business",
                "Audit its current (or a competitor's) social presence",
                "Define a target audience and clear goals",
                "Build a 4-week content calendar",
                "Create a few sample posts",
                "Define 3-4 metrics to track success",
                "Write a short strategy report summarizing the plan",
            ],
        },
        "education_preparation": (
            "A marketing or mass communication background helps, but demonstrated results growing "
            "or managing real accounts -- even small or personal ones -- often matter more than a "
            "specific degree."
        ),
        "experience_ideas": {
            "+2 / High School": ["Manage a club's or personal interest social media account",
                                  "Study how a few brands you like run their social pages"],
            "Bachelor": ["Intern with a marketing team", "Manage social media for a student organization"],
            "Master": ["Lead a small campaign or client account",
                       "Study paid advertising platforms in depth"],
        },
    },

    ("Research & Science", "Research Scientist"): {
        "description": (
            "Research scientists design and carry out studies to answer specific questions "
            "and expand knowledge in a field, whether in academia, industry, or government. "
            "The work centers on careful experimental design, data analysis, and communicating "
            "findings through papers or reports."
        ),
        "typical_activities": [
            "Designing experiments or research studies",
            "Conducting lab or field research",
            "Analyzing data and applying statistical methods",
            "Writing research papers or technical reports",
            "Presenting findings at conferences or seminars",
            "Applying for research funding or grants",
        ],
        "useful_strengths": ["research", "analytical_thinking", "problem_solving", "technical_ability", "organization"],
        "critical_skills": ["research", "analytical_thinking", "problem_solving", "technical_ability", "organization"],
        "skill_importance": {
            "research": 1.0,
            "analytical_thinking": 0.9,
            "problem_solving": 0.8,
            "technical_ability": 0.6,
            "organization": 0.5,
        },
        "useful_academic_areas": ["Science", "Mathematics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 1,
        },
        "work_settings": ["University labs", "Government research institutes",
                           "Private R&D labs", "Research nonprofits"],
        "possible_directions": ["Academic Research", "Industry R&D",
                                 "Government Research Labs", "Applied Research Consulting"],
        "foundational_topics": ["Scientific method and experimental design", "Statistics for research",
                                 "Literature review skills"],
        "field_methods": ["Hypothesis testing", "Peer review process",
                           "Structured data collection protocols"],
        "tools_context": ["Statistical software (R, SPSS, or Excel for basics)", "Reference management tools (Zotero, Mendeley)",
                           "Field-specific lab instruments as relevant"],
        "project_ideas": [
            "Run a Small Original Study",
            "Write a Literature Review on a Topic",
        ],
        "project": {
            "title": "Small-Scale Original Research Study",
            "steps": [
                "Pick a specific, narrow research question",
                "Review 5-10 existing sources on the topic",
                "Design a simple study or experiment to test it",
                "Collect data through a survey, experiment, or observation",
                "Analyze the results",
                "Write up findings in a short report",
                "Note limitations and what you would study next",
            ],
        },
        "education_preparation": (
            "Typically requires a bachelor's degree in the relevant science field, often followed "
            "by a master's or PhD for independent research roles; the specific field of study "
            "should match your emerging research interest."
        ),
        "experience_ideas": {
            "+2 / High School": ["Enter a science fair project",
                                  "Read introductory papers in a field of interest"],
            "Bachelor": ["Assist a professor with their research as an RA",
                         "Present at an undergraduate research symposium"],
            "Master": ["Pursue a thesis-based program",
                       "Submit a paper to a conference or journal"],
        },
    },

    ("Research & Science", "Geologist"): {
        "description": (
            "Geologists study the earth's physical structure, materials, and processes -- "
            "rocks, minerals, soil, and groundwater -- often to understand natural resources, "
            "hazards, or geological history. The work mixes outdoor fieldwork with lab and "
            "office-based analysis."
        ),
        "typical_activities": [
            "Conducting field surveys and collecting samples",
            "Analyzing rock, soil, or mineral samples",
            "Mapping geological formations",
            "Interpreting seismic or satellite data",
            "Writing geological reports",
            "Assessing sites for construction, mining, or hazard risk",
        ],
        "useful_strengths": ["analytical_thinking", "research", "technical_ability", "problem_solving"],
        "critical_skills": ["analytical_thinking", "research", "technical_ability", "problem_solving"],
        "skill_importance": {
            "analytical_thinking": 0.9,
            "research": 0.8,
            "technical_ability": 0.75,
            "problem_solving": 0.7,
        },
        "useful_academic_areas": ["Science", "Mathematics", "Computer"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 4,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 1,
        },
        "work_settings": ["Mining and energy companies", "Government geological surveys",
                           "Environmental consulting firms", "Construction / engineering firms",
                           "Field sites and labs"],
        "possible_directions": ["Mining / Resource Geology", "Environmental / Engineering Geology",
                                 "Seismology", "Hydrogeology"],
        "foundational_topics": ["Rock and mineral identification", "Basic geological mapping",
                                 "Plate tectonics and earth processes"],
        "field_methods": ["Field sampling and rock/soil logging", "Compass and clinometer structural readings",
                           "Basic GPS-based site mapping"],
        "tools_context": ["GIS software (QGIS or ArcGIS) for mapping", "Rock/mineral identification kits",
                           "Basic field survey instruments"],
        "project_ideas": [
            "Local Rock and Soil Survey",
            "Map a Small Area's Geology",
        ],
        "project": {
            "title": "Local Area Geological Survey",
            "steps": [
                "Choose a small, accessible area (park, quarry, riverbank)",
                "Collect and identify a handful of rock or soil samples",
                "Note visible geological features (layers, erosion, formations)",
                "Sketch or map the area's basic geology",
                "Research the likely geological history of the area",
                "Compile findings into a short illustrated report",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in geology or earth science is the standard entry point; "
            "fieldwork experience and comfort with outdoor physical work matter alongside "
            "classroom knowledge."
        ),
        "experience_ideas": {
            "+2 / High School": ["Join a science club field trip",
                                  "Collect and identify local rocks or minerals as a hobby"],
            "Bachelor": ["Attend a field camp or mapping course",
                         "Volunteer or assist on a professor's fieldwork"],
            "Master": ["Specialize (e.g. hydrogeology, seismology) through a research thesis",
                       "Seek an internship with a survey or mining company"],
        },
    },

    ("Research & Science", "Lab Technician"): {
        "description": (
            "Lab technicians perform hands-on bench work -- preparing samples, running "
            "standard tests, and maintaining equipment -- supporting scientists, doctors, or "
            "engineers with accurate, repeatable lab processes. The role focuses more on "
            "precise execution than independent research design."
        ),
        "typical_activities": [
            "Preparing and labeling samples",
            "Running standard lab tests and procedures",
            "Calibrating and maintaining lab equipment",
            "Recording and logging results accurately",
            "Following safety and quality-control protocols",
            "Restocking lab supplies and reagents",
        ],
        "useful_strengths": ["technical_ability", "organization", "analytical_thinking", "teamwork"],
        "critical_skills": ["technical_ability", "organization", "analytical_thinking", "teamwork"],
        "skill_importance": {
            "technical_ability": 0.9,
            "organization": 0.85,
            "analytical_thinking": 0.6,
            "teamwork": 0.5,
        },
        "useful_academic_areas": ["Science", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 1,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 1,
            "pref_handson_vs_theoretical": 5,
            "pref_tech_vs_people": 1,
        },
        "work_settings": ["Hospital / clinical labs", "University research labs",
                           "Pharmaceutical / biotech companies", "Industrial quality-control labs"],
        "possible_directions": ["Clinical / Medical Lab Work", "Research Lab Support",
                                 "Quality Control Labs", "Industrial / Pharma Labs"],
        "foundational_topics": ["Lab safety and hygiene practices", "Basic measurement and instrument use",
                                 "Sample handling and record-keeping"],
        "field_methods": ["Standard operating procedures (SOPs)", "Equipment calibration checks",
                           "Chain-of-custody sample tracking"],
        "tools_context": ["Standard lab equipment (pipettes, centrifuges, microscopes)", "Lab information management systems (LIMS)",
                           "Basic spreadsheet software for records"],
        "project_ideas": [
            "Practice Sample Testing Routine",
            "Simple Home-Safe Lab Procedure Log",
        ],
        "project": {
            "title": "Practice Lab Procedure and Log",
            "steps": [
                "Pick a simple, safe hands-on procedure (e.g. water pH testing, plant sample prep)",
                "Write a clear step-by-step protocol for it",
                "Carry out the procedure carefully, following safety practices",
                "Record measurements and results in a structured log",
                "Repeat the procedure 2-3 times to check consistency",
                "Note any errors or inconsistencies and possible causes",
            ],
        },
        "education_preparation": (
            "Often requires a diploma or bachelor's degree in a lab-related science (biology, "
            "chemistry, or medical lab science); attention to detail and following procedure "
            "precisely matter as much as theoretical depth."
        ),
        "experience_ideas": {
            "+2 / High School": ["Do careful, methodical work in school science labs",
                                  "Practice taking detailed, structured lab notes"],
            "Bachelor": ["Seek a lab assistant role or internship in a university or hospital lab"],
            "Master": ["Aim for specialized lab work (e.g. diagnostics, research support)",
                       "Pursue further certification in a specific lab technique"],
        },
    },

    ("Agriculture & Environment", "Agricultural Scientist"): {
        "description": (
            "Agricultural scientists apply science to improve crop yields, soil health, and "
            "farming practices, working between research and practical field application. "
            "The role often involves advising farmers or agribusinesses on evidence-based "
            "techniques."
        ),
        "typical_activities": [
            "Conducting field trials on crops or soil",
            "Testing new farming techniques or seed varieties",
            "Analyzing soil, plant, or yield data",
            "Advising farmers on best practices",
            "Researching pest and disease management",
            "Writing reports for agricultural agencies or companies",
        ],
        "useful_strengths": ["research", "analytical_thinking", "problem_solving", "communication"],
        "critical_skills": ["research", "analytical_thinking", "problem_solving", "communication"],
        "skill_importance": {
            "research": 0.85,
            "analytical_thinking": 0.8,
            "problem_solving": 0.75,
            "communication": 0.55,
        },
        "useful_academic_areas": ["Science", "Mathematics", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 4,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 2,
        },
        "work_settings": ["Agricultural research institutes", "Government agriculture departments",
                           "Agribusiness companies", "Farms and field stations"],
        "possible_directions": ["Crop Science", "Soil Science",
                                 "Agricultural Extension / Advisory", "Agribusiness Research"],
        "foundational_topics": ["Plant and soil science basics", "Experimental field trial design",
                                 "Sustainable farming practices"],
        "field_methods": ["Field trial setup and monitoring", "Soil and plant sampling",
                           "Yield measurement and comparison"],
        "tools_context": ["Soil testing kits", "Basic statistical or spreadsheet software for yield data",
                           "Farm management apps (optional)"],
        "project_ideas": [
            "Small Crop Trial Comparison",
            "Soil Health Test on a Local Plot",
        ],
        "project": {
            "title": "Small-Scale Crop Growth Trial",
            "steps": [
                "Choose one crop or plant and one variable to test (e.g. fertilizer type, watering schedule)",
                "Set up 2-3 small comparison plots or containers",
                "Maintain and monitor them over several weeks",
                "Record growth measurements regularly",
                "Compare results across conditions",
                "Write up findings and practical recommendations",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in agricultural science, agronomy, or a related field is the "
            "typical starting point; hands-on farming or field-trial experience strengthens "
            "practical understanding alongside coursework."
        ),
        "experience_ideas": {
            "+2 / High School": ["Help with a family or community garden or farm",
                                  "Join an agriculture-related school club"],
            "Bachelor": ["Participate in a field trial or research project with a professor",
                         "Intern with an agricultural extension office"],
            "Master": ["Pursue a specialization (crop science, soil science)",
                       "Collaborate with a research institute or agribusiness"],
        },
    },

    ("Agriculture & Environment", "Veterinary Doctor"): {
        "description": (
            "Veterinary doctors diagnose and treat health issues in animals, from pets and "
            "livestock to wildlife, and advise owners or farmers on care and disease "
            "prevention. In practice this is a licensed medical profession requiring formal "
            "veterinary training."
        ),
        "typical_activities": [
            "Examining and diagnosing sick or injured animals",
            "Administering treatments and vaccinations",
            "Advising animal owners on care and nutrition",
            "Assisting with animal births or minor procedures",
            "Maintaining animal health records",
            "Working with farmers or shelters on preventive care",
        ],
        "useful_strengths": ["problem_solving", "technical_ability", "communication", "analytical_thinking"],
        "critical_skills": ["problem_solving", "technical_ability", "communication", "analytical_thinking"],
        "skill_importance": {
            "problem_solving": 0.85,
            "technical_ability": 0.8,
            "communication": 0.7,
            "analytical_thinking": 0.6,
        },
        "useful_academic_areas": ["Science", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 3,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["Veterinary clinics", "Farms and rural practices",
                           "Animal shelters / NGOs", "Zoos or wildlife centers"],
        "possible_directions": ["Companion Animal Practice", "Livestock / Farm Veterinary Work",
                                 "Wildlife / Zoo Veterinary Care", "Animal Public Health"],
        "foundational_topics": ["Basic animal anatomy and physiology", "Animal handling and welfare basics",
                                 "Common disease recognition"],
        "field_methods": ["Animal health observation and assessment", "Basic vitals monitoring",
                           "Record-keeping for animal health history"],
        "tools_context": ["Veterinary reference guides", "Basic animal handling equipment",
                           "Clinic management / record-keeping software"],
        "project_ideas": [
            "Animal Care Case Study",
            "Shadow a Vet or Shelter Visit Write-Up",
        ],
        "project": {
            "title": "Animal Care Observation Case Study",
            "steps": [
                "Arrange to observe at a vet clinic, shelter, or farm (with permission)",
                "Choose one animal case to follow (even a pet's routine checkup)",
                "Note the animal's condition, symptoms, and how it is assessed",
                "Research the underlying health topic afterward",
                "Write up the case as a short observational report",
                "Reflect on what care or prevention steps were involved",
            ],
        },
        "education_preparation": (
            "Veterinary practice requires a professional veterinary degree (BVSc or equivalent) "
            "and licensing to treat animals; before that, building comfort with animals and "
            "strengthening biology fundamentals is a practical first step for someone exploring "
            "the field."
        ),
        "experience_ideas": {
            "+2 / High School": ["Volunteer at an animal shelter",
                                  "Care for pets or farm animals responsibly"],
            "Bachelor": ["Shadow a practicing veterinarian",
                         "Volunteer at a clinic or wildlife rescue"],
            "Master": ["Complete required clinical rotations during veterinary studies",
                       "Seek mentorship with an experienced vet in your area of interest"],
        },
    },

    ("Agriculture & Environment", "Environmental Scientist"): {
        "description": (
            "Environmental scientists study natural systems -- air, water, soil, and "
            "ecosystems -- to assess environmental problems, monitor pollution, and support "
            "conservation or policy decisions. The work combines field data collection with "
            "analysis and reporting."
        ),
        "typical_activities": [
            "Collecting environmental samples (water, soil, air)",
            "Monitoring pollution or ecosystem health",
            "Analyzing environmental data",
            "Writing environmental impact assessments",
            "Advising organizations or governments on regulations",
            "Conducting site visits and field surveys",
        ],
        "useful_strengths": ["research", "analytical_thinking", "problem_solving", "communication"],
        "critical_skills": ["research", "analytical_thinking", "problem_solving", "communication"],
        "skill_importance": {
            "research": 0.85,
            "analytical_thinking": 0.8,
            "problem_solving": 0.65,
            "communication": 0.55,
        },
        "useful_academic_areas": ["Science", "Mathematics", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 4,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 2,
        },
        "work_settings": ["Environmental consulting firms", "Government environmental agencies",
                           "NGOs / conservation organizations", "Research institutes"],
        "possible_directions": ["Environmental Consulting", "Conservation & Ecology",
                                 "Environmental Policy", "Pollution Monitoring"],
        "foundational_topics": ["Ecosystem and environmental science basics", "Environmental regulations and impact assessment",
                                 "Data collection and sampling methods"],
        "field_methods": ["Water, soil, and air sampling techniques", "Field surveys and biodiversity counts",
                           "Environmental monitoring protocols"],
        "tools_context": ["GIS software for environmental mapping", "Basic field testing kits (water quality, soil)",
                           "Spreadsheet or statistical software for analysis"],
        "project_ideas": [
            "Local Water Quality Check",
            "Community Environmental Audit",
        ],
        "project": {
            "title": "Local Environmental Quality Assessment",
            "steps": [
                "Choose one local environmental aspect to study (a water body, green space, or air quality concern)",
                "Research appropriate simple assessment methods",
                "Collect observations or basic measurements (e.g. water clarity, litter counts, plant diversity)",
                "Compare findings to general environmental standards where possible",
                "Identify likely causes of any problems found",
                "Write a short report with practical recommendations",
            ],
        },
        "education_preparation": (
            "A bachelor's degree in environmental science or a related science field is the "
            "typical entry point; fieldwork experience and familiarity with environmental "
            "regulations add practical value."
        ),
        "experience_ideas": {
            "+2 / High School": ["Participate in a local clean-up or conservation volunteer effort",
                                  "Join an environmental club"],
            "Bachelor": ["Assist with a professor's environmental research or fieldwork",
                         "Intern with an environmental NGO or agency"],
            "Master": ["Specialize in a focus area (water resources, conservation, policy)",
                       "Contribute to an applied research or consulting project"],
        },
    },

    # --- from group6_hospitality_socialwork_sports.py ---
    ("Hospitality & Tourism", "Hotel Manager"): {
        "description": (
            "Hotel managers oversee the day-to-day running of a hotel or resort, making sure "
            "guests have a good stay while the business stays profitable. The work involves "
            "coordinating staff across departments like front desk, housekeeping, and food "
            "service, and stepping in personally when something goes wrong for a guest."
        ),
        "typical_activities": [
            "Scheduling and supervising staff across departments",
            "Resolving guest complaints and service issues",
            "Monitoring budgets, occupancy, and revenue",
            "Coordinating housekeeping, front desk, and food & beverage teams",
            "Negotiating with vendors and suppliers",
            "Monitoring guest reviews and service quality",
        ],
        "useful_strengths": ["leadership", "organization", "communication", "problem_solving"],
        "critical_skills": ["leadership", "organization", "communication", "problem_solving"],
        "skill_importance": {
            "leadership": 0.9,
            "organization": 0.85,
            "communication": 0.8,
            "problem_solving": 0.7,
        },
        "useful_academic_areas": ["Business/Economics", "English", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Hotels & resorts", "Hospitality chains", "Boutique guesthouses",
                           "Convention & conference centers"],
        "possible_directions": ["Front Office Management", "Food & Beverage Management",
                                 "Revenue Management", "Hospitality Consulting"],
        "foundational_topics": ["Hospitality operations basics", "Customer service principles",
                                 "Budgeting & revenue basics"],
        "field_methods": ["Guest feedback analysis", "Staff shift scheduling",
                           "Service quality audits"],
        "tools_context": ["Property management systems (e.g. Opera)", "Spreadsheet software",
                           "Booking & reservation platforms"],
        "project_ideas": ["Mock Hotel Operations Plan", "Guest Experience Audit"],
        "project": {
            "title": "Local Guesthouse Service Audit",
            "steps": [
                "Pick a small local hotel or guesthouse you can observe or visit",
                "Walk through the guest journey from booking to check-out",
                "Talk to staff or the manager about how their workflow runs",
                "Note 3-4 gaps or friction points in the guest experience",
                "Propose specific, realistic improvements for each gap",
                "Write a short report summarizing your findings",
            ],
        },
        "education_preparation": (
            "A hospitality management diploma or degree is common and helpful, but many hotel "
            "managers build their career by working up through hotel departments. Internships "
            "and hands-on experience in an actual hotel matter a great deal."
        ),
        "experience_ideas": {
            "+2 / High School": ["Take a part-time or holiday job at a local hotel's front desk",
                                  "Shadow a hotel manager for a day to see the range of their work"],
            "Bachelor": ["Do an internship rotating across hotel departments",
                         "Take on a leadership role in a hospitality or hosting club/event"],
            "Master": ["Join a hotel chain's management trainee program",
                       "Take a specialization in revenue or operations management"],
        },
    },

    ("Hospitality & Tourism", "Tour Guide"): {
        "description": (
            "Tour guides lead visitors through places of interest, sharing history, culture, "
            "or nature knowledge while keeping the group safe, on schedule, and engaged. The "
            "work depends heavily on storytelling and thinking on your feet when plans change."
        ),
        "typical_activities": [
            "Researching the history and background of destinations",
            "Leading walking, bus, or site tours for groups",
            "Answering visitor questions on the spot",
            "Managing group logistics, pacing, and safety",
            "Coordinating with drivers, vendors, or site staff",
            "Handling unexpected issues like delays or emergencies",
        ],
        "useful_strengths": ["communication", "presentation", "organization", "problem_solving"],
        "critical_skills": ["communication", "presentation", "organization", "problem_solving"],
        "skill_importance": {
            "communication": 0.95,
            "presentation": 0.85,
            "organization": 0.65,
            "problem_solving": 0.6,
        },
        "useful_academic_areas": ["English", "Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 4,
            "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Travel & tour agencies", "Museums & heritage sites", "National parks",
                           "Freelance / self-employed"],
        "possible_directions": ["Heritage & Cultural Tours", "Adventure / Eco Tourism",
                                 "Museum & Site Interpretation", "Travel Planning"],
        "foundational_topics": ["Local history and geography", "Tourism safety basics",
                                 "Public speaking"],
        "field_methods": ["Route & itinerary planning", "Storytelling techniques",
                           "Group management"],
        "tools_context": ["Audio guide equipment", "Translation apps", "Mapping apps"],
        "project_ideas": ["Neighborhood Heritage Walk", "Local Legends Tour Script"],
        "project": {
            "title": "Design a Local Walking Tour",
            "steps": [
                "Pick a neighborhood or site near you with some history or character",
                "Research its background from a few different sources",
                "Draft a 45-60 minute route with 4-6 stops",
                "Write narration and talking points for each stop",
                "Test-run the tour with friends or family",
                "Gather their feedback and revise the script",
            ],
        },
        "education_preparation": (
            "There's no fixed degree required; strong research, language, and public-speaking "
            "skills matter more than formal schooling. Many regions require a local tourism "
            "board certification or guide license to operate professionally."
        ),
        "experience_ideas": {
            "+2 / High School": ["Volunteer at a local museum or heritage site",
                                  "Practice giving informal tours to visiting family or friends"],
            "Bachelor": ["Intern with a tour operator or travel agency",
                         "Get certified as a licensed local tour guide"],
            "Master": ["Pursue a language or specialization certification",
                       "Work with an international tour agency on specialized tours"],
        },
    },

    ("Hospitality & Tourism", "Chef / Culinary Artist"): {
        "description": (
            "Chefs plan menus and prepare food professionally, balancing creativity with "
            "technique, hygiene, and consistency under time pressure. The work ranges from "
            "hands-on cooking to managing a kitchen team and controlling food costs."
        ),
        "typical_activities": [
            "Developing recipes and planning menus",
            "Preparing and cooking food to a consistent standard",
            "Managing kitchen workflow during service",
            "Sourcing ingredients and managing inventory",
            "Maintaining food hygiene and safety standards",
            "Plating and presenting finished dishes",
        ],
        "useful_strengths": ["technical_ability", "creativity", "organization", "teamwork"],
        "critical_skills": ["technical_ability", "creativity", "organization", "teamwork"],
        "skill_importance": {
            "technical_ability": 0.9,
            "creativity": 0.85,
            "organization": 0.7,
            "teamwork": 0.65,
        },
        "useful_academic_areas": ["Science", "Arts", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 5,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 5,
            "pref_tech_vs_people": 2,
        },
        "work_settings": ["Restaurants", "Hotels", "Catering companies",
                           "Private / personal chef work", "Culinary studios"],
        "possible_directions": ["Pastry & Baking", "Restaurant Head Chef",
                                 "Catering & Events Cooking", "Food Styling / Content Creation"],
        "foundational_topics": ["Food safety & hygiene", "Basic culinary techniques",
                                 "Ingredient and flavor knowledge"],
        "field_methods": ["Recipe testing and tasting", "Plating and presentation practice",
                           "Kitchen workflow (mise en place)"],
        "tools_context": ["Kitchen equipment", "Recipe costing spreadsheets",
                           "Food photography basics (optional)"],
        "project_ideas": ["Original Recipe Collection", "Pop-up Dinner Menu"],
        "project": {
            "title": "Create and Test an Original Recipe Menu",
            "steps": [
                "Pick a cuisine or theme you want to explore",
                "Develop 3-4 original recipes around it",
                "Test and refine each recipe through repeated cooking",
                "Cost out the ingredients for each dish",
                "Plate and photograph the final dishes",
                "Cook the menu for family or friends and collect feedback",
            ],
        },
        "education_preparation": (
            "Culinary school or a diploma helps build technique and hygiene discipline quickly, "
            "but many chefs learn through apprenticeships and years of real kitchen experience "
            "instead of a formal degree."
        ),
        "experience_ideas": {
            "+2 / High School": ["Cook regularly at home and experiment with recipes",
                                  "Take a part-time job as a kitchen helper"],
            "Bachelor": ["Attend a culinary school or diploma program",
                         "Do an internship (stage) in a restaurant kitchen"],
            "Master": ["Pursue specialized training (pastry, a specific cuisine)",
                       "Complete an apprenticeship in a professional kitchen"],
        },
    },

    ("Hospitality & Tourism", "Event Planner"): {
        "description": (
            "Event planners turn a client's vision for an event into a real, working plan, "
            "managing budgets, vendors, and timelines so everything comes together on the "
            "day. The work mixes creative planning with a lot of logistics and troubleshooting."
        ),
        "typical_activities": [
            "Meeting clients to understand their vision and budget",
            "Sourcing and negotiating with vendors",
            "Building event timelines and logistics plans",
            "Coordinating on-site during the event itself",
            "Tracking and managing event budgets",
            "Troubleshooting problems as they come up",
        ],
        "useful_strengths": ["organization", "problem_solving", "communication", "creativity"],
        "critical_skills": ["organization", "problem_solving", "communication", "creativity"],
        "skill_importance": {
            "organization": 0.9,
            "problem_solving": 0.8,
            "communication": 0.8,
            "creativity": 0.65,
        },
        "useful_academic_areas": ["Business/Economics", "Arts", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 4,
            "pref_indoor_vs_outdoor": 2,
            "pref_structured_vs_flexible": 4,
            "pref_handson_vs_theoretical": 4,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["Event management companies", "Hotels & venues",
                           "Corporate events teams", "Freelance / self-employed",
                           "Wedding planning agencies"],
        "possible_directions": ["Corporate Event Management", "Wedding Planning",
                                 "Conference & Exhibition Management", "Venue Management"],
        "foundational_topics": ["Budgeting & vendor negotiation basics",
                                 "Event logistics & timeline planning", "Basic contract awareness"],
        "field_methods": ["Run-of-show / timeline creation", "Vendor coordination",
                           "On-site problem solving"],
        "tools_context": ["Spreadsheet / budget tools", "Event planning apps (e.g. Trello)",
                           "Design tools for invitations or mood boards (optional)"],
        "project_ideas": ["Plan a Small Community Event", "Mock Wedding Budget & Timeline"],
        "project": {
            "title": "Plan and Run a Small Real Event",
            "steps": [
                "Choose a small real event (birthday, club event, fundraiser)",
                "Define a budget and vision together with the 'client'",
                "Create a vendor/task list and a full timeline",
                "Coordinate logistics in the lead-up to the event",
                "Run the event on the day and handle issues as they arise",
                "Write a short post-event review of what worked and what didn't",
            ],
        },
        "education_preparation": (
            "There's no strict degree requirement; an event management certificate or a "
            "hospitality/business background helps, but hands-on experience assisting with "
            "real events is often more valuable than classroom study alone."
        ),
        "experience_ideas": {
            "+2 / High School": ["Help organize a school or college event",
                                  "Volunteer on a local event's setup crew"],
            "Bachelor": ["Intern with an event management company",
                         "Take charge of planning a club or college fest"],
            "Master": ["Pursue an event management certification",
                       "Independently manage a larger-scale event"],
        },
    },

    ("Social Work & Community", "NGO Program Officer"): {
        "description": (
            "NGO program officers design, run, and monitor community or development programs, "
            "working between funders, field teams, and the communities being served. The work "
            "mixes hands-on coordination with writing proposals and reports for donors."
        ),
        "typical_activities": [
            "Designing and monitoring program activities",
            "Writing grant proposals and donor reports",
            "Coordinating with beneficiaries and communities",
            "Managing field teams and program budgets",
            "Liaising with donors and partner organizations",
            "Monitoring and evaluating program outcomes",
        ],
        "useful_strengths": ["organization", "communication", "research", "problem_solving"],
        "critical_skills": ["organization", "communication", "research", "problem_solving"],
        "skill_importance": {
            "organization": 0.85,
            "communication": 0.8,
            "research": 0.7,
            "problem_solving": 0.65,
        },
        "useful_academic_areas": ["Business/Economics", "English", "Science"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 3,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["NGOs / INGOs", "UN or development agencies", "Government programs",
                           "CSR units of companies", "Community-based organizations"],
        "possible_directions": ["Program Management", "Monitoring & Evaluation",
                                 "Grants & Fundraising", "Policy & Advocacy"],
        "foundational_topics": ["Project cycle basics (design-implement-monitor-evaluate)",
                                 "Grant writing basics", "Community engagement principles"],
        "field_methods": ["Needs assessments", "Monitoring & evaluation (M&E) frameworks",
                           "Stakeholder coordination"],
        "tools_context": ["Spreadsheet / reporting tools", "Basic data-collection apps (e.g. KoboToolbox)",
                           "Proposal writing templates"],
        "project_ideas": ["Mini Program Design & Proposal", "Community Needs-to-Action Plan"],
        "project": {
            "title": "Design a Small Program Proposal",
            "steps": [
                "Identify one specific local social issue",
                "Do a small needs assessment (a few interviews or observations)",
                "Design a simple program with clear goals and activities",
                "Draft a basic budget outline",
                "Write a 2-3 page proposal document",
                "Define 2-3 indicators to measure whether it's working",
            ],
        },
        "education_preparation": (
            "A degree in social sciences, development studies, or a related field is common, "
            "but practical field or volunteer experience with an NGO is often what matters most "
            "for entry-level roles."
        ),
        "experience_ideas": {
            "+2 / High School": ["Volunteer with a local NGO or community drive",
                                  "Help organize a school social-impact initiative"],
            "Bachelor": ["Intern at an NGO or INGO",
                         "Participate in a student-led social-impact project"],
            "Master": ["Take on a program coordination role or M&E assistantship",
                       "Pursue a development studies specialization"],
        },
    },

    ("Social Work & Community", "Psychologist"): {
        "description": (
            "Psychologists study how people think, feel, and behave, and apply that "
            "understanding through research, education, or (for licensed practitioners) "
            "assessment and therapy. The exploratory and research side of psychology is open "
            "to anyone curious to learn, but clinical practice is a formally regulated field."
        ),
        "typical_activities": [
            "Researching human behavior and mental processes",
            "Designing and running surveys or small studies",
            "Analyzing data from psychological research",
            "Educating people about mental health and wellbeing",
            "Documenting case notes or research findings",
            "For licensed practitioners: conducting assessments and therapy sessions",
        ],
        "useful_strengths": ["research", "analytical_thinking", "communication", "problem_solving"],
        "critical_skills": ["research", "analytical_thinking", "communication", "problem_solving"],
        "skill_importance": {
            "research": 0.85,
            "analytical_thinking": 0.85,
            "communication": 0.8,
            "problem_solving": 0.6,
        },
        "useful_academic_areas": ["Science", "English", "Mathematics"],
        "work_preferences": {
            "pref_people_vs_independent": 4,
            "pref_creative_vs_analytical": 2,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 2,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["Hospitals & clinics (licensed roles)", "Schools & universities",
                           "Research institutions", "NGOs (mental health programs)",
                           "Private practice (licensed roles)", "Corporate HR / wellness teams"],
        "possible_directions": ["Clinical / Counseling Psychology (requires licensure)",
                                 "Research Psychology", "School / Educational Psychology",
                                 "Organizational Psychology"],
        "foundational_topics": ["Basic psychology theories and terminology",
                                 "Research methods and statistics", "Ethics of working with people"],
        "field_methods": ["Surveys and structured interviews", "Behavioral observation",
                           "Basic statistical analysis of survey data"],
        "tools_context": ["Survey tools (e.g. Google Forms)", "Statistical software (e.g. SPSS, Excel)",
                           "Psychology reference literature / journals"],
        "project_ideas": ["Small Survey on a Behavior Topic", "Interview Study on Wellbeing"],
        "project": {
            "title": "Small Exploratory Survey Study",
            "steps": [
                "Choose a specific, appropriate psychology topic (e.g. study habits, stress, social media use)",
                "Design a short survey or interview questionnaire (8-12 questions)",
                "Collect responses from a small, willing sample",
                "Organize and analyze the responses for patterns",
                "Write a short summary of your findings and possible interpretations",
            ],
        },
        "education_preparation": (
            "General exploration and research-based work, like the project above, can start "
            "with self-study and coursework in psychology. Practicing clinically or offering "
            "counseling and therapy, however, legally requires a relevant formal degree "
            "(typically a Master's or higher), supervised training, and licensing — this is not "
            "something to attempt without proper qualification."
        ),
        "experience_ideas": {
            "+2 / High School": ["Read introductory psychology books",
                                  "Run a small, informal, non-clinical survey among peers"],
            "Bachelor": ["Assist a professor with a research project",
                         "Volunteer with a mental-health awareness campaign (non-clinical)"],
            "Master": ["Pursue supervised clinical training/practicum if going the counseling route",
                       "Take a research assistantship if going the research route"],
        },
    },

    ("Sports & Fitness", "Sports Coach"): {
        "description": (
            "Sports coaches train individuals or teams to improve their skills, fitness, and "
            "game strategy, and guide them through competition. The work is as much about "
            "motivating and managing people as it is about technical sport knowledge."
        ),
        "typical_activities": [
            "Planning and running training sessions",
            "Teaching techniques and rules of the sport",
            "Developing game strategy and tactics",
            "Motivating athletes and giving performance feedback",
            "Managing team dynamics and discipline",
            "Communicating with players' families or institutions about progress",
        ],
        "useful_strengths": ["leadership", "communication", "teamwork", "problem_solving"],
        "critical_skills": ["leadership", "communication", "teamwork", "problem_solving"],
        "skill_importance": {
            "leadership": 0.9,
            "communication": 0.8,
            "teamwork": 0.65,
            "problem_solving": 0.6,
        },
        "useful_academic_areas": ["Science", "Business/Economics", "English"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 4,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 5,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Schools & colleges", "Sports academies / clubs",
                           "Community sports programs", "National / state sports teams"],
        "possible_directions": ["Youth / School Coaching", "Competitive / Elite Team Coaching",
                                 "Strength & Conditioning Coaching", "Sports Program Administration"],
        "foundational_topics": ["Rules and techniques of the sport",
                                 "Basic training and practice-session planning",
                                 "Sports safety and injury awareness"],
        "field_methods": ["Drill and practice-session design",
                           "Performance feedback and correction techniques",
                           "Team and tournament planning"],
        "tools_context": ["Video recording for technique review",
                           "Basic scheduling / planning tools", "Sport-specific training equipment"],
        "project_ideas": ["Coach a Beginner Group Session", "6-Week Training Plan for a Team"],
        "project": {
            "title": "Design and Run a Beginner Training Program",
            "steps": [
                "Pick a sport you know well",
                "Gather a small group of beginners (friends or juniors) to coach",
                "Design a 4-6 week session plan with clear skill goals",
                "Run weekly sessions and track each person's progress",
                "Adjust drills based on what's working and what isn't",
                "Run a final session reviewing everyone's improvement",
            ],
        },
        "education_preparation": (
            "A sports science or physical education degree helps, but certified coaching "
            "courses run by sport federations are often the more direct path in. Real playing "
            "experience in the sport is also very valuable."
        ),
        "experience_ideas": {
            "+2 / High School": ["Help coach a junior team or younger siblings/peers informally",
                                  "Take a basic coaching certification course"],
            "Bachelor": ["Serve as assistant coach for a school or college team",
                         "Pursue a sport-specific coaching certification"],
            "Master": ["Pursue an advanced coaching license or diploma",
                       "Coach at a higher competitive level (state / academy)"],
        },
    },

    ("Sports & Fitness", "Fitness Trainer"): {
        "description": (
            "Fitness trainers design and guide exercise programs for individuals or groups "
            "aiming to improve their health, strength, or fitness. The work is hands-on and "
            "people-focused, requiring both correct exercise technique and the ability to keep "
            "clients motivated and safe."
        ),
        "typical_activities": [
            "Designing individualized workout or exercise plans",
            "Demonstrating and correcting exercise form",
            "Tracking client progress (strength, endurance, body metrics)",
            "Advising on general fitness and lifestyle habits",
            "Running group fitness classes",
            "Ensuring safe use of gym equipment",
        ],
        "useful_strengths": ["technical_ability", "communication", "problem_solving", "organization"],
        "critical_skills": ["technical_ability", "communication", "problem_solving", "organization"],
        "skill_importance": {
            "technical_ability": 0.85,
            "communication": 0.75,
            "problem_solving": 0.6,
            "organization": 0.55,
        },
        "useful_academic_areas": ["Science", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 5,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 3,
            "pref_structured_vs_flexible": 3,
            "pref_handson_vs_theoretical": 5,
            "pref_tech_vs_people": 5,
        },
        "work_settings": ["Gyms & fitness centers", "Wellness / health clubs",
                           "Freelance / personal training", "Corporate wellness programs"],
        "possible_directions": ["Personal Training", "Group Fitness Instruction",
                                 "Strength & Conditioning", "Specialized Training (rehab, sport-specific)"],
        "foundational_topics": ["Basic exercise physiology and anatomy", "Safe exercise technique",
                                 "Nutrition fundamentals"],
        "field_methods": ["Fitness assessments (strength, endurance, flexibility tests)",
                           "Progress tracking and program adjustment", "Exercise form correction"],
        "tools_context": ["Fitness tracking apps", "Basic gym / training equipment",
                           "Workout planning spreadsheets or apps"],
        "project_ideas": ["Personal 8-Week Fitness Plan", "Train a Friend Toward a Goal"],
        "project": {
            "title": "Design and Run an 8-Week Training Program",
            "steps": [
                "Pick a willing friend or family member and their fitness goal",
                "Assess their current fitness level safely",
                "Design a progressive 8-week workout plan",
                "Guide and supervise sessions with proper form",
                "Track measurable progress weekly",
                "Adjust the plan based on results and feedback",
            ],
        },
        "education_preparation": (
            "A recognized personal training or fitness certification is the common entry path. "
            "A formal sports science degree helps for advanced or clinical work, but isn't "
            "always required to start out."
        ),
        "experience_ideas": {
            "+2 / High School": ["Get certified in basic first aid / CPR",
                                  "Build and log your own consistent workout routine"],
            "Bachelor": ["Pursue a personal training certification",
                         "Train friends or family informally to build experience"],
            "Master": ["Pursue specialized certifications (strength & conditioning, rehab)",
                       "Work under an experienced trainer at a gym"],
        },
    },

    ("Sports & Fitness", "Sports Analyst"): {
        "description": (
            "Sports analysts collect and study performance data and game footage to help "
            "coaches and teams make better decisions. The work is far more data- and "
            "video-driven than coaching or playing, closer to research than to being on the field."
        ),
        "typical_activities": [
            "Collecting and organizing match and player performance data",
            "Analyzing statistics to identify patterns and trends",
            "Preparing scouting or opposition reports",
            "Presenting findings to coaches or team management",
            "Watching and breaking down game footage",
            "Building performance dashboards or visualizations",
        ],
        "useful_strengths": ["analytical_thinking", "research", "technical_ability", "presentation"],
        "critical_skills": ["analytical_thinking", "research", "technical_ability", "presentation"],
        "skill_importance": {
            "analytical_thinking": 0.9,
            "research": 0.7,
            "technical_ability": 0.65,
            "presentation": 0.6,
        },
        "useful_academic_areas": ["Mathematics", "Computer", "Science"],
        "work_preferences": {
            "pref_people_vs_independent": 2,
            "pref_creative_vs_analytical": 1,
            "pref_indoor_vs_outdoor": 1,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 3,
            "pref_tech_vs_people": 2,
        },
        "work_settings": ["Professional sports teams / clubs", "Sports media / broadcasting",
                           "Sports analytics companies", "Research / academic sports science units"],
        "possible_directions": ["Performance Analysis", "Scouting & Recruitment Analysis",
                                 "Sports Data Science", "Sports Broadcasting Analysis"],
        "foundational_topics": ["Basic statistics", "Deep knowledge of the sport's rules and tactics",
                                 "Data organization (spreadsheets / databases)"],
        "field_methods": ["Video / footage breakdown", "Statistical trend analysis",
                           "Report writing for coaching staff"],
        "tools_context": ["Spreadsheet software", "Sports analytics platforms",
                           "Video analysis software", "Basic data visualization tools"],
        "project_ideas": ["Match Performance Report", "Season Stats Dashboard"],
        "project": {
            "title": "Analyze a Team's Recent Performance",
            "steps": [
                "Pick a sport or team you follow closely",
                "Gather match statistics from public sources for several recent games",
                "Organize the data in a spreadsheet",
                "Identify 3-4 meaningful patterns or trends",
                "Create simple charts to illustrate the findings",
                "Write a short scouting-style report with recommendations",
            ],
        },
        "education_preparation": (
            "A background in sports science, statistics, or data analysis is useful. This "
            "field increasingly values demonstrated analytical and data skills, such as a "
            "strong self-made analysis project, as much as a specific degree."
        ),
        "experience_ideas": {
            "+2 / High School": ["Track and analyze stats for a favorite team or player as a hobby",
                                  "Learn basic spreadsheet and data skills"],
            "Bachelor": ["Intern with a sports media outlet or a college team's analytics effort",
                         "Build a public portfolio of analysis write-ups"],
            "Master": ["Pursue a sports analytics or data science specialization",
                       "Seek an analyst assistantship with a team or sports organization"],
        },
    },

    ("Sports & Fitness", "Athlete"): {
        "description": (
            "Being an athlete means pursuing competitive or professional performance in a "
            "sport through structured training and competition, not a typical job with a fixed "
            "roadmap. It usually requires starting young, sustained access to coaching and "
            "competition, and a lot of disciplined practice, and most people who train "
            "seriously do not end up going professional — which is why many build a parallel "
            "path (study, coaching, analysis) alongside training."
        ),
        "typical_activities": [
            "Following structured physical training and skill practice",
            "Competing in matches, tournaments, or competitions",
            "Reviewing personal performance, including video analysis",
            "Following nutrition, recovery, and injury-prevention routines",
            "Working closely with coaches and trainers",
            "Balancing training with school, work, or other commitments",
        ],
        "useful_strengths": ["technical_ability", "problem_solving", "organization", "teamwork"],
        "critical_skills": ["technical_ability", "organization", "problem_solving", "teamwork"],
        "skill_importance": {
            "technical_ability": 0.9,
            "organization": 0.75,
            "problem_solving": 0.6,
            "teamwork": 0.5,
        },
        "useful_academic_areas": ["Science", "Business/Economics"],
        "work_preferences": {
            "pref_people_vs_independent": 3,
            "pref_creative_vs_analytical": 3,
            "pref_indoor_vs_outdoor": 4,
            "pref_structured_vs_flexible": 2,
            "pref_handson_vs_theoretical": 5,
            "pref_tech_vs_people": 4,
        },
        "work_settings": ["Sports clubs / academies", "School & college sports teams",
                           "National / state training centers", "Competitive tournaments / circuits"],
        "possible_directions": ["Continuing to compete at higher levels", "Moving into Coaching",
                                 "Moving into Sports Analysis / Commentary", "Sports Administration / Management"],
        "foundational_topics": ["Fundamentals and rules of the chosen sport",
                                 "Basic training, recovery, and nutrition principles",
                                 "Understanding of competition structures (leagues, qualification)"],
        "field_methods": ["Structured practice and drilling", "Performance and video self-review",
                           "Recovery and injury-prevention routines"],
        "tools_context": ["Training log or app for tracking sessions",
                           "Video recording for technique review (optional)"],
        "project_ideas": ["8-Week Personal Training Log", "Pre-Competition Prep Plan"],
        "project": {
            "title": "Structured Training & Performance Tracking Plan",
            "steps": [
                "Choose the sport or event to focus on",
                "Set 2-3 specific, measurable performance goals",
                "Build a structured weekly training schedule",
                "Log every session: what was practiced, effort, and results",
                "Review progress every 2 weeks and adjust the plan",
                "Compete or test yourself in a low-stakes match or time-trial to benchmark",
            ],
        },
        "education_preparation": (
            "There is no fixed academic path to becoming a professional athlete — it depends "
            "heavily on starting to train early, consistent access to good coaching and "
            "competition, and natural aptitude, and most people who train seriously do not end "
            "up as professionals. It's worth building a fallback academic or career path (e.g. "
            "sports science, coaching, or another field) alongside training."
        ),
        "experience_ideas": {
            "+2 / High School": ["Join school or local club teams and competitions",
                                  "Get access to a good coach if possible"],
            "Bachelor": ["Compete at college or university level tournaments",
                         "Consider a sports science or related degree as a fallback/complement"],
            "Master": ["Pursue high-performance training programs if still actively competing",
                       "Transition into coaching or sports management studies"],
        },
    },

}


def get_career_knowledge(domain: str, role: str, specialization: str = None) -> dict:
    """
    Look up curated guidance for a role, merging in specialization-level
    overrides where they exist. Returns {} if this role hasn't been
    authored yet -- callers (roadmap.py) must handle that gracefully,
    not assume every role is covered.
    """
    base = CAREER_KNOWLEDGE.get((domain, role))
    if not base:
        return {}

    result = {k: v for k, v in base.items() if k != "specializations"}

    if specialization and "specializations" in base:
        # specialization may be "Parent — Sub" (sub-specialization) -- match
        # on the parent spec name, which is what carries the override
        parent_spec = specialization.split(" — ")[0]
        override = base["specializations"].get(parent_spec, {})
        result.update(override)

    return result


def is_regulated(domain: str, role: str) -> bool:
    return (domain, role) in REGULATED_ROLES
