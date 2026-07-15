import google.generativeai as genai
from app.config import settings

print("Loaded Gemini Key:", settings.GEMINI_API_KEY[:10])

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text: str, job_description: str = ""):
    prompt = f"""
You are an ATS Resume Reviewer.

Resume:
{resume_text}

Job Description:
{job_description}
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("========== GEMINI ERROR ==========")
        print(type(e))
        print(e)
        raise