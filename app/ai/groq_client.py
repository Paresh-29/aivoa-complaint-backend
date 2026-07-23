import json
import os

from dotenv import load_dotenv
from groq import Groq

from app.ai.prompts import EXTRACT_COMPLAINT_PROMPT, UPDATE_COMPLAINT_PROMPT

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def create_complaint(text: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": EXTRACT_COMPLAINT_PROMPT,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
    )

    return json.loads(response.choices[0].message.content)

def update_complaint(complaint: dict, message: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": UPDATE_COMPLAINT_PROMPT,
            },
            {
                "role": "user",
                "content": f"""
Current Complaint:

{complaint}

User Instruction:

{message}
""",
            },
        ],
    )

    return json.loads(response.choices[0].message.content)
