from src.models.base import BaseResponse


class ErrorDetail(BaseResponse):
    code: str
    message: str


class ErrorResponse(BaseResponse):
    error: ErrorDetail
