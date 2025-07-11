from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

health_router: APIRouter

class HealthResponse(BaseModel):
    status: Literal["ok"] = Field(default="ok")

def health() -> HealthResponse: ...