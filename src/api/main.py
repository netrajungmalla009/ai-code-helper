from fastapi import FastAPI

from src.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Production-grade AI engineering assistant platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": f"{settings.app_name} API is running"}


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }
