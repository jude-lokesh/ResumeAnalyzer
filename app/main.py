from fastapi import FastAPI, UploadFile
from app.parsepdf import parse_pdf
from app.agents.resume_extractor import extract_resume_data
from app.agents.jd_extractor import analyze_Job_Desc
from app.agents.candidate_evaluation import evaluate_candidate


app = FastAPI()

# @app.post('/screening/')
# async def screening(resume: UploadFile):
    
#     resume_data = parse_pdf(resume.file)
#     resume_details_extracted = extract_resume_data(resume_data)
    
#     jd_text = ''
#     with open('app/resources/job_description.pdf', 'rb') as file:
#         jd_text = parse_pdf(file)
#     jd_extracted = analyze_Job_Desc(jd_text)

#     evaluation_result = evaluate_candidate(resume_details_extracted, jd_extracted)

#     return resume_details_extracted
@app.post('/screening/')
async def screening(resume: UploadFile):

    resume_data = parse_pdf(resume.file)

    resume_details_extracted = extract_resume_data(resume_data)
    
    print(type(resume_details_extracted))
    print(resume_details_extracted)

    with open('app/resources/job_description.pdf', 'rb') as file:
        jd_text = parse_pdf(file)

    jd_extracted = analyze_Job_Desc(jd_text)

    evaluation_result = evaluate_candidate(
        resume_details_extracted,
        jd_extracted
    )

    return {
        "candidate": resume_details_extracted,
        "evaluation": evaluation_result
    }