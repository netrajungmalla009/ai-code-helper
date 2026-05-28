from fastapi import APIRouter

from src.models.provider_status import (
    ProviderStatusResponse,
)
from src.services.ollama_service import OllamaService

router = APIRouter(
    prefix="/providers",
    tags=["Providers"],
)


@router.get(
    "/ollama/status",
    response_model=ProviderStatusResponse,
    summary="Get Ollama runtime status",
)
async def get_ollama_status():
    return OllamaService.get_status()
