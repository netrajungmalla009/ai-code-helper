from pydantic import BaseModel, Field

from src.models.base import TimestampedModel
from src.models.provider import LLMProvider


class AIExecutionRequest(BaseModel):
    prompt: str = Field(..., min_length=1)

    provider: LLMProvider | None = None

    model: str | None = None

    temperature: float = Field(default=0.7, ge=0.0, le=2.0)

    max_tokens: int = Field(default=512, ge=1, le=8192)


class AIExecutionResponse(TimestampedModel):
    provider: LLMProvider

    model: str

    prompt: str

    response: str

    success: bool = True
