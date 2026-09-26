from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

app = FastAPI(
    title="HealthInfo AI",
    description="An LLM-powered healthcare information API that provides general health information using Gemini.",
    version="1.0.0"
)

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "HealthInfo AI API is running"
    }

@app.post(
    "/ask",
    summary="Ask a healthcare information question",
    description="Submit a general healthcare question and receive an AI-generated informational response."
)
def ask_question(data: Question):
    prompt = f"""
You are HealthInfo AI, a healthcare information assistant.

Your role is to provide clear, general health information for educational purposes.

Guidelines:
- Do not diagnose the user or claim certainty about a medical condition.
- Do not present yourself as a doctor or healthcare professional.
- Explain medical information clearly and accurately.
- If symptoms could indicate a serious or emergency condition, advise the user to seek appropriate medical care.
- Do not recommend specific prescription medicines or dosages as a substitute for professional medical advice.
- Encourage users to consult a qualified healthcare professional when personalized medical advice is needed.

User question:
{data.question}
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return {
    "question": data.question,
    "answer": response.text,
    "disclaimer": "This information is for general educational purposes and is not a substitute for professional medical advice, diagnosis, or treatment."
}