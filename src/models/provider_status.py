from src.models.base import TimestampedModel
from src.models.provider import LLMProvider


class ProviderStatusResponse(TimestampedModel):
    provider: LLMProvider
    available: bool
    base_url: str | None = None
    message: str
