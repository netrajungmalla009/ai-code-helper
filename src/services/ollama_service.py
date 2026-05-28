from src.core.config import settings
from src.models.provider import LLMProvider
from src.models.provider_status import (
    ProviderStatusResponse,
)


class OllamaService:
    @staticmethod
    def get_status() -> ProviderStatusResponse:
        return ProviderStatusResponse(
            provider=LLMProvider.OLLAMA,
            available=settings.enable_ollama,
            base_url=settings.ollama_base_url,
            message="Ollama runtime configuration loaded",
        )
