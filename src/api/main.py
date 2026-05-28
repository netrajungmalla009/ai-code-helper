from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.config import settings
from src.core.logging import configure_logging, get_logger

configure_logging()

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting AI Code Helper API")
    logger.info(f"Environment: {settings.environment}")

    yield

    logger.info("Shutting down AI Code Helper API")


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)


@app.get(f"{settings.api_v1_str}/")
async def root():
    return {
        "message": "AI Code Helper API",
        "environment": settings.environment,
    }


@app.get(f"{settings.api_v1_str}/health")
async def health_check():
    return {
        "status": "healthy",
    }
