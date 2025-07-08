from pydantic import BaseModel
from typing import Optional
from enum import Enum


class NewsInputType(str, Enum):
    text = "text"
    url = "url"


class NewsInput(BaseModel):
    input_type: NewsInputType
    content: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "input_type": "text",
                "content": "Vacinas mudam o DNA humano."
            }
        }


class ClassificationResult(BaseModel):
    text: str
    type: NewsInputType
    label: str
    score: float

    class Config:
        frozen = True


class StatusResponse(BaseModel):
    status: str
