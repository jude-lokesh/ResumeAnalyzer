from openai import OpenAI
import os
from dotenv import load_dotenv
from app.prompts import CANDIDATE_EVALUATION
import json

# load_dotenv()
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI()

def evaluate_candidate(Candidate_details: str, jd_text: str) -> dict:
    prompt = CANDIDATE_EVALUATION.format(
        resume_json=Candidate_details,
        jd_json=jd_text
    )
    try:
        response = client.chat.completions.create(
            model = 'gpt-4o-mini',
            response_format={"type": "json_object"},
            messages=[
                {'role': 'system', 'content':prompt}
            ]
        )
        print('Responce from OpenAI:', response.choices[0].message.content)
        return json.loads(
            response.choices[0].message.content
        )
    except Exception as e:
        return {'error' : str(e)}