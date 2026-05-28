from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from src.api.exceptions.handlers import (
    generic_exception_handler,
    validation_exception_handler,
)
from src.api.middleware.logging import RequestLoggingMiddleware
from src.api.v1.api import api_router
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
app.add_middleware(RequestLoggingMiddleware)
app.include_router(
    api_router,
    prefix=settings.api_v1_str,
)
app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)

app.add_exception_handler(
    Exception,
    generic_exception_handler,
)
