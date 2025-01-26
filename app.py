import streamlit as st
from config import Config
from utils import analyze_profile, generate_career_path_visualization, generate_skill_gap_radar
from components import render_header, render_profile_form, render_recommendations

# Configure page settings
st.set_page_config(
    page_title=Config.PAGE_TITLE,
    page_icon=Config.PAGE_ICON,
    layout=Config.LAYOUT
)

def main():
    render_header()
    
    # Profile Form
    profile_data = render_profile_form()
    
    if profile_data:
        with st.spinner("Analyzing your profile..."):
            recommendations = analyze_profile(profile_data)
            
            if recommendations:
                # Display recommendations
                render_recommendations(recommendations)
                
                # Career Path Visualization
                st.header("📈 Career Path Visualization")
                fig = generate_career_path_visualization(recommendations["career_path"])
                st.plotly_chart(fig)
                
                # Skill Gap Analysis
                st.header("🎯 Skill Gap Analysis")
                fig = generate_skill_gap_radar(
                    profile_data["skills"],
                    recommendations["skill_gaps"]
                )
                st.plotly_chart(fig)
                
                # Download Report
                st.download_button(
                    label="Download Career Report",
                    data=str(recommendations),
                    file_name="career_report.json",
                    mime="application/json"
                )

if __name__ == "__main__":
    main()