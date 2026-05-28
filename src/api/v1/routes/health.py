from fastapi import APIRouter

from src.core.config import settings
from src.models.demo import DemoRequest
from src.models.health import HealthResponse, RootResponse

router = APIRouter()


@router.get(
    "/",
    response_model=RootResponse,
    tags=["System"],
    summary="Root endpoint",
)
async def root():
    return RootResponse(message=f"{settings.app_name} API is running")


@router.get(
    "/health",
    response_model=HealthResponse,
    tags=["System"],
    summary="Health check endpoint",
)
async def health_check():
    return HealthResponse(
        status="healthy",
        environment=settings.environment,
    )


@router.post(
    "/demo-validation",
    tags=["System"],
    summary="Validation testing endpoint",
)
async def demo_validation(payload: DemoRequest):
    return {
        "success": True,
        "message": "Validation passed",
        "payload": payload.model_dump(),
    }
