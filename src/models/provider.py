from enum import Enum

from pydantic import BaseModel


class LLMProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"


class ProviderStatus(str, Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"


class ProviderInfo(BaseModel):
    provider: LLMProvider

    default_model: str

    status: ProviderStatus


class ProviderListResponse(BaseModel):
    providers: list[ProviderInfo]
