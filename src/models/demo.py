from pydantic import BaseModel, Field


class DemoRequest(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0)
