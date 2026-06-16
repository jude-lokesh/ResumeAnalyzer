from openai import OpenAI
import os
from dotenv import load_dotenv
from app.prompts import EXTRACT_CANDIDATE_DETAILS
import json

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_resume_data(resume_data):
    prompt = EXTRACT_CANDIDATE_DETAILS.format(resume_text = resume_data)
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        response_format={"type": "json_object"},
        messages=[
            {'role': 'system', 'content':prompt}
        ]
    )
    
    print('Responce from OpenAI:', response.choices[0].message.content)
    # return response.choices[0].message.content
    
    return json.loads(
        response.choices[0].message.content
    )