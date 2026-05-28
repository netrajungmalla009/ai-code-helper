from datetime import UTC, datetime

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    success: bool = True


class TimestampedModel(BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
