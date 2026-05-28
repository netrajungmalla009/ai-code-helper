from fastapi import APIRouter

from src.models.execution import (
    AIExecutionRequest,
    AIExecutionResponse,
)
from src.services.execution_service import ExecutionService

router = APIRouter()


@router.post(
    "/execute",
    response_model=AIExecutionResponse,
    tags=["Execution"],
    summary="Execute AI request",
)
async def execute_ai_request(
    request: AIExecutionRequest,
):
    return await ExecutionService.execute(request)
