import streamlit as st
from config import Config

def render_header():
    """Render the application header"""
    st.title("💼 Career Recommendation System")
    st.markdown("""
    Get personalized career recommendations based on your skills, education, and interests.
    Fill out your profile below to get started!
    """)

def render_profile_form():
    """Render the user profile form"""
    with st.form("profile_form"):
        # Personal Information
        st.subheader("Personal Information")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        
        # Education
        st.subheader("Education")
        education_level = st.selectbox(
            "Highest Education Level",
            options=Config.EDUCATION_LEVELS
        )
        field_of_study = st.text_input("Field of Study")
        
        # Experience
        st.subheader("Experience")
        experience_level = st.selectbox(
            "Experience Level",
            options=Config.EXPERIENCE_LEVELS
        )
        current_role = st.text_input("Current/Most Recent Role")
        
        # Skills
        st.subheader("Skills")
        skills = []
        for category in Config.SKILL_CATEGORIES:
            skills_input = st.text_area(
                f"{category} (One per line)",
                height=100
            )
            if skills_input:
                skills.extend([skill.strip() for skill in skills_input.split('\n')])
        
        # Career Goals
        st.subheader("Career Goals")
        career_goals = st.text_area(
            "What are your career goals and interests?",
            height=150
        )
        
        submitted = st.form_submit_button("Get Recommendations")
        
        if submitted:
            return {
                "name": name,
                "email": email,
                "education_level": education_level,
                "field_of_study": field_of_study,
                "experience_level": experience_level,
                "current_role": current_role,
                "skills": skills,
                "career_goals": career_goals
            }
        return None

def render_recommendations(recommendations):
    """Render career recommendations"""
    if not recommendations:
        return
    
    st.header("🎯 Career Recommendations")
    
    # Recommended Roles
    st.subheader("Recommended Roles")
    for role in recommendations["recommended_roles"]:
        st.write(f"• {role}")
    
    # Skill Gaps
    st.subheader("Skills to Develop")
    for skill in recommendations["skill_gaps"]:
        st.write(f"• {skill}")
    
    # Recommended Courses
    st.subheader("Recommended Courses")
    for course in recommendations["recommended_courses"]:
        st.write(f"• {course}")
    
    # Market Insights
    st.subheader("Market Insights")
    st.write(recommendations["market_insights"])