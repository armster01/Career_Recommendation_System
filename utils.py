import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def analyze_profile(profile_data):
    """Analyze user profile using Gemini API"""
    try:
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""
        Analyze this career profile and provide recommendations:
        {json.dumps(profile_data, indent=2)}
        
        Return a JSON object with this structure:
        {{
            "recommended_roles": ["role1", "role2", "role3"],
            "skill_gaps": ["skill1", "skill2", "skill3"],
            "recommended_courses": ["course1", "course2", "course3"],
            "career_path": ["step1", "step2", "step3"],
            "market_insights": "brief market analysis"
        }}
        """
        
        response = model.generate_content(prompt)
        return json.loads(response.text)
        
    except Exception as e:
        st.error(f"Profile analysis error: {str(e)}")
        return None

def generate_career_path_visualization(career_path):
    """Generate a visualization of the career path"""
    fig = go.Figure(data=[go.Scatter(
        x=list(range(len(career_path))),
        y=[1] * len(career_path),
        mode='markers+text',
        text=career_path,
        textposition='top center'
    )])
    
    fig.update_layout(
        title="Your Career Path",
        showlegend=False,
        height=300
    )
    
    return fig

def generate_skill_gap_radar(current_skills, required_skills):
    """Generate a radar chart showing skill gaps"""
    categories = list(set(current_skills + required_skills))
    current_values = [1 if skill in current_skills else 0 for skill in categories]
    required_values = [1 if skill in required_skills else 0 for skill in categories]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=current_values,
        theta=categories,
        fill='toself',
        name='Current Skills'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=required_values,
        theta=categories,
        fill='toself',
        name='Required Skills'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True
    )
    
    return fig