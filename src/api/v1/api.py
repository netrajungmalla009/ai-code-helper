from fastapi import APIRouter

from src.api.v1.routes.execution import router as execution_router
from src.api.v1.routes.health import router as health_router
from src.api.v1.routes.providers import router as providers_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(execution_router)
api_router.include_router(providers_router)
