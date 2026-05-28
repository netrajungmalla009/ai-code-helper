from datetime import UTC, datetime

import httpx

from src.adapters.base import BaseProviderAdapter
from src.core.config import settings
from src.models.execution import (
    AIExecutionRequest,
    AIExecutionResponse,
)
from src.models.provider import LLMProvider


class OllamaAdapter(BaseProviderAdapter):
    async def execute(
        self,
        request: AIExecutionRequest,
    ) -> AIExecutionResponse:
        ollama_payload = {
            "model": request.model,
            "prompt": request.prompt,
            "stream": False,
        }

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{settings.ollama_base_url}/api/generate",
                json=ollama_payload,
            )

        response.raise_for_status()

        response_data = response.json()

        generated_text = response_data.get(
            "response",
            "No response generated.",
        )

        return AIExecutionResponse(
            created_at=datetime.now(UTC),
            provider=LLMProvider.OLLAMA,
            model=request.model,
            prompt=request.prompt,
            response=generated_text,
            success=True,
        )
