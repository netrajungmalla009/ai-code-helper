from src.adapters.base import BaseProviderAdapter
from src.adapters.ollama_adapter import OllamaAdapter
from src.adapters.openai_adapter import OpenAIAdapter
from src.models.provider import LLMProvider


class AdapterRegistry:
    _registry: dict[
        LLMProvider,
        BaseProviderAdapter,
    ] = {
        LLMProvider.OPENAI: OpenAIAdapter(),
        LLMProvider.OLLAMA: OllamaAdapter(),
    }

    @classmethod
    def get_adapter(
        cls,
        provider: LLMProvider,
    ) -> BaseProviderAdapter:
        adapter = cls._registry.get(provider)

        if not adapter:
            raise ValueError(f"No adapter registered for provider: {provider}")

        return adapter
