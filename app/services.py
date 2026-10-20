
from fastapi import HTTPException

from openai import APIConnectionError, APIStatusError, APITimeoutError

from app.llm import generate_answer
from app.schemas import QuestionRequest, QuestionResponse


async def answer_question(
    request: QuestionRequest,
) -> QuestionResponse:
    try:
        answer = await generate_answer(request.question)

    except APITimeoutError:
        raise HTTPException(
            status_code=504,
            detail="The AI provider took too long to respond.",
        )

    except APIConnectionError:
        raise HTTPException(
            status_code=502,
            detail="Could not connect to the AI provider.",
        )

    except APIStatusError:
        raise HTTPException(
            status_code=502,
            detail="The AI provider returned an error.",
        )
    return QuestionResponse(
        question=request.question,
        answer=answer,
        status="completed",
    )
