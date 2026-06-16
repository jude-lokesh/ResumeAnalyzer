EXTRACT_CANDIDATE_DETAILS = """
You are an expert AI resume screening assistant.

Your task is to extract structured candidate information from the provided resume text.

Rules:

1. Return ONLY a valid JSON object.
2. Do not include markdown, explanations, comments, or extra text.
3. If a field is not found, use null.
4. Skills and certifications must always be arrays.
5. work_experience should be the total years of professional experience as an integer.
6. Extract information exactly as written in the resume whenever possible.
7. Ensure the output is valid JSON that can be parsed using json.loads().

Required JSON Schema:

{{
"name": "string | null",
"email": "string | null",
"phone": "string | null",
"location": "string | null",
"education": "string | null",
"work_experience": "integer | null",
"current_company": "string | null",
"current_designation": "string | null",
"skills": [],
"certifications": []
}}

Resume Text:

{resume_text}

Expected Output Example:

{{
"name": "John Doe",
"email": "[john.doe@gmail.com](mailto:john.doe@gmail.com)",
"phone": "+1 9876543210",
"location": "New York, USA",
"education": "Bachelor of Science in Computer Science",
"work_experience": 5,
"current_company": "Google",
"current_designation": "Software Engineer",
"skills": [
"Python",
"FastAPI",
"Machine Learning",
"Docker"
],
"certifications": [
"AWS Certified Developer Associate",
"Certified Python Developer"
]
}}
"""


EXTRACT_JD_DETAILS = """
You are an expert in filtering the required skills and experience from a given job description.

Your task is to extract relevant information from the provided job description and return a valid JSON object.

Extract the following:

* min_work_experience (integer or null)
* max_work_experience (integer or null)
* skills (array of strings)

Rules:

1. Return ONLY valid JSON.
2. Do not include markdown, explanations, or extra text.
3. Use null if a value cannot be determined.
4. Skills must always be an array.
5. If experience is mentioned as a range (e.g. "5-8 years"), use:

   * min_work_experience = 5
   * max_work_experience = 8
6. If only one value is provided (e.g. "3+ years"), use:

   * min_work_experience = 3
   * max_work_experience = null
7. Remove duplicate skills.

Job Description:

{jd_text}

Expected Response Format:

{{
"min_work_experience": 5,
"max_work_experience": 8,
"skills": [
"Python",
"FastAPI",
"Machine Learning",
"Docker"
]
}}
"""

CANDIDATE_EVALUATION = """
You are a candidate evaluation agent.

You will receive:

1. A candidate's extracted profile (JSON)
2. A job description (JSON)

Evaluate whether the candidate is a good fit based on the following criteria:

1. At least 50% of the required skills must match.
2. The candidate's work experience must fall within the acceptable range defined by:

   * min_work_experience
   * max_work_experience

Decision Rules:

* Return "Selected" only if BOTH conditions are satisfied.
* Otherwise return "Rejected".
* Consider closely related skills as valid matches.
  Example:

  * CI/CD ↔ DevOps
  * FastAPI ↔ Python Backend Development
  * TensorFlow ↔ Deep Learning
  * React ↔ Frontend Development

Provide a detailed explanation for the decision.

Return ONLY a valid JSON object in the following format:

{{
"candidate_status": "Selected",
"reason": "The candidate possesses most of the required skills and meets the required experience range. Their background aligns well with the job requirements.",
"matched_skills": [
"Python",
"FastAPI",
"Machine Learning"
],
"skill_match_percentage": 75,
"experience": 5
}}

Candidate Profile:

{resume_json}

Job Description:

{jd_json}
"""
