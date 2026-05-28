from abc import ABC, abstractmethod

from src.models.execution import (
    AIExecutionRequest,
    AIExecutionResponse,
)


class BaseProviderAdapter(ABC):
    @abstractmethod
    def execute(
        self,
        request: AIExecutionRequest,
    ) -> AIExecutionResponse:
        pass
