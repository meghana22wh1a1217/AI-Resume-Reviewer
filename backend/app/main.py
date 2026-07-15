from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.analyze import router as analyze_router
from app.api.payment import router as payment_router
from app.api.webhook import router as webhook_router
app = FastAPI(title="AI Resume Reviewer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    analyze_router,
    prefix="/analyze",
    tags=["Analyze"],
)

app.include_router(
    payment_router,
    prefix="/payment",
    tags=["Payment"],
)
app.include_router(
    webhook_router,
    prefix="/webhook",
    tags=["Webhook"],
)
@app.get("/")
def root():
    return {"message": "AI Resume Reviewer Backend is running!"}