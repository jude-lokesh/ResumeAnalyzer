import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Resume Screening",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Enter Job Description",
    placeholder="Paste the Job Description here...",
    height=250
)

if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("🚀 Process Resume"):

        with st.spinner("Analyzing Resume..."):

            response = requests.post(
                "http://localhost:8000/screening/",
                files={"resume": uploaded_file},
                data={"job_description": job_description}
            )

        if response.status_code == 200:

            data = response.json()
            
            response_data = response.json()
        
            
            
            candidate = response_data["candidate"]
            evaluation = response_data["evaluation"]
            
            st.subheader("👤 Candidate")

            st.divider()

            # Status Banner
            if evaluation["candidate_status"] == "Selected":
                st.success("✅ Candidate Selected")
            else:
                st.error("❌ Candidate Rejected")

            st.metric(
                "Skill Match",
                f"{evaluation['skill_match_percentage']}%"
            )

            # Metrics
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Experience",
                    f"{evaluation['experience']} Years"
                )

            with col2:
                st.metric(
                    "Skill Match",
                    f"{evaluation['skill_match_percentage']}%"
                )

            with col3:
                st.metric(
                    "Matched Skills",
                    len(evaluation["matched_skills"])
                )

            st.divider()

            # Skills
            st.subheader("🎯 Matched Skills")

            for skill in evaluation["matched_skills"]:
                st.badge(skill)

            st.divider()

            # Reason
            st.subheader("📝 Evaluation Summary")
            st.info(evaluation["reason"])

            # Raw JSON
            with st.expander("View Full Response"):
                st.json(evaluation)

        else:
            st.error("Failed to process resume")