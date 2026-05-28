from src.adapters.base import BaseProviderAdapter
from src.models.execution import (
    AIExecutionRequest,
    AIExecutionResponse,
)
from src.models.provider import LLMProvider


class OpenAIAdapter(BaseProviderAdapter):
    def execute(
        self,
        request: AIExecutionRequest,
    ) -> AIExecutionResponse:
        simulated_response = f"OpenAI simulated response for: '{request.prompt}'"

        return AIExecutionResponse(
            provider=LLMProvider.OPENAI,
            model="gpt-5",
            prompt=request.prompt,
            response=simulated_response,
            success=True,
        )
