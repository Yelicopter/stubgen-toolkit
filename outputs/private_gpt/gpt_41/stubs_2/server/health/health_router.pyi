from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

health_router: APIRouter

class HealthResponse(BaseModel):
    status: str

def health() -> HealthResponse: ...