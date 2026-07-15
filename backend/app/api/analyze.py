from fastapi import APIRouter

from app.schemas.review import ReviewRequest
from app.services.pdf_service import extract_text_from_url
from app.services.ai_service import analyze_resume

router = APIRouter()


@router.post("/")
def analyze(request: ReviewRequest):

    resume_text = extract_text_from_url(request.resume_url)

    result = analyze_resume(
        resume_text,
        request.job_description,
    )

    return {
        "analysis": result
    }