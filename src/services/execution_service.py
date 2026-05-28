from src.models.execution import (
    AIExecutionRequest,
    AIExecutionResponse,
)
from src.services.adapter_registry import AdapterRegistry
from src.services.provider_service import ProviderService


class ExecutionService:
    @staticmethod
    async def execute(
        request: AIExecutionRequest,
    ) -> AIExecutionResponse:
        active_provider = (
            request.provider
            if request.provider
            else ProviderService.get_active_provider().provider
        )

        adapter = AdapterRegistry.get_adapter(active_provider)

        return await adapter.execute(request)
