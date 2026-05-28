import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.logging import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        logger.info(f"Incoming request: {request.method} {request.url.path}")

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            f"Completed request: "
            f"{request.method} "
            f"{request.url.path} "
            f"Status: {response.status_code} "
            f"Duration: {process_time:.4f}s"
        )

        return response
