from pydantic import BaseModel


class ReviewRequest(BaseModel):
    resume_url: str
    job_description: str = ""