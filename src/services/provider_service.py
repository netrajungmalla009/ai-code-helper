from src.core.config import settings
from src.models.provider import (
    LLMProvider,
    ProviderInfo,
    ProviderListResponse,
    ProviderStatus,
)


class ProviderService:
    @staticmethod
    def get_available_providers() -> ProviderListResponse:
        providers = [
            ProviderInfo(
                provider=LLMProvider.OPENAI,
                default_model=settings.default_llm_model,
                status=(
                    ProviderStatus.ENABLED
                    if settings.enable_openai
                    else ProviderStatus.DISABLED
                ),
            ),
            ProviderInfo(
                provider=LLMProvider.ANTHROPIC,
                default_model="claude-3-7-sonnet",
                status=(
                    ProviderStatus.ENABLED
                    if settings.enable_anthropic
                    else ProviderStatus.DISABLED
                ),
            ),
            ProviderInfo(
                provider=LLMProvider.OLLAMA,
                default_model="llama3",
                status=(
                    ProviderStatus.ENABLED
                    if settings.enable_ollama
                    else ProviderStatus.DISABLED
                ),
            ),
        ]

        return ProviderListResponse(providers=providers)

    @staticmethod
    def get_active_provider() -> ProviderInfo:
        provider_mapping = {
            "openai": ProviderInfo(
                provider=LLMProvider.OPENAI,
                default_model=settings.default_llm_model,
                status=ProviderStatus.ENABLED,
            ),
            "anthropic": ProviderInfo(
                provider=LLMProvider.ANTHROPIC,
                default_model="claude-3-7-sonnet",
                status=ProviderStatus.ENABLED,
            ),
            "ollama": ProviderInfo(
                provider=LLMProvider.OLLAMA,
                default_model="llama3",
                status=ProviderStatus.ENABLED,
            ),
        }

        return provider_mapping[settings.default_llm_provider]

    @staticmethod
    def is_provider_enabled(provider: LLMProvider) -> bool:
        provider_flags = {
            LLMProvider.OPENAI: settings.enable_openai,
            LLMProvider.ANTHROPIC: settings.enable_anthropic,
            LLMProvider.OLLAMA: settings.enable_ollama,
        }

        return provider_flags.get(provider, False)
