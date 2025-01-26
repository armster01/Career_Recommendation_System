class Config:
    # Streamlit configs
    PAGE_TITLE = "Career Recommendation System"
    PAGE_ICON = "💼"
    LAYOUT = "wide"
    
    # Gemini API settings
    MAX_TOKENS = 1000
    TEMPERATURE = 0.7
    MODEL_NAME = "gemini-pro"
    
    # Skill categories
    SKILL_CATEGORIES = [
        "Technical Skills",
        "Soft Skills",
        "Industry Knowledge",
        "Tools & Technologies",
        "Certifications"
    ]
    
    # Education levels
    EDUCATION_LEVELS = [
        "High School",
        "Bachelor's Degree",
        "Master's Degree",
        "Ph.D.",
        "Professional Certification"
    ]
    
    # Experience levels
    EXPERIENCE_LEVELS = [
        "Entry Level (0-2 years)",
        "Mid Level (3-5 years)",
        "Senior Level (6-10 years)",
        "Expert Level (10+ years)"
    ]