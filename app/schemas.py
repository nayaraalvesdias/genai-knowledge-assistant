from typing_extensions import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class QuestionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    question: str = Field(min_length=3, max_length=500)
    
    @field_validator("question")
    @classmethod
    def normalize_question(cls, value: str) -> str:
        value = value.strip()

        if len(value) < 3:
            raise ValueError("Question must contain at least 3 characters")

        return value


class QuestionResponse(BaseModel):
    question: str
    answer: str
    status: Literal['completed']