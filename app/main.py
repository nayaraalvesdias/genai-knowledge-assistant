
from fastapi import FastAPI
from typing import Annotated
from fastapi import Depends

from app.schemas import QuestionRequest, QuestionResponse
from app.services import answer_question

app = FastAPI(
    title="GenAI Knowledge Assistant",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Knowledge Assistant API is running"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/ask", response_model=QuestionResponse)
async def ask_question(request: QuestionRequest) -> QuestionResponse:
    return await answer_question(request)


def get_app_info() -> dict:
    return {"service": "knowledge-assistant"}


@app.get("/info")
async def get_info(
    info: Annotated[dict, Depends(get_app_info)],
):
    return info