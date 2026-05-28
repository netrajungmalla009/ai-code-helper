from fastapi import FastAPI

from src.api.v1.api import api_router
from src.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Production-grade AI engineering assistant platform",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(
    api_router,
    prefix=settings.api_v1_str,
)
