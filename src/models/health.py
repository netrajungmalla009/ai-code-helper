from src.models.base import BaseResponse


class RootResponse(BaseResponse):
    message: str


class HealthResponse(BaseResponse):
    status: str
    environment: str
