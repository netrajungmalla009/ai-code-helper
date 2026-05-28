from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.models.error import ErrorDetail


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    error = ErrorDetail(
        success=False,
        code="VALIDATION_ERROR",
        message="Request validation failed",
    )

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=error.model_dump(mode="json"),
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    error = ErrorDetail(
        success=False,
        code="INTERNAL_SERVER_ERROR",
        message="An unexpected error occurred",
    )

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=error.model_dump(mode="json"),
    )
