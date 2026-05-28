from fastapi import FastAPI

from src.core.config import settings
from src.models.health import HealthResponse, RootResponse

app = FastAPI(
    title=settings.app_name,
    description="Production-grade AI engineering assistant platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get(
    "/",
    response_model=RootResponse,
    tags=["System"],
    summary="Root endpoint",
)
async def root():
    return RootResponse(message=f"{settings.app_name} API is running")


@app.get(
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
