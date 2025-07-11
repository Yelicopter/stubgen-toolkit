from fastapi import APIRouter as APIRouter
from pydantic import BaseModel
from typing import Literal

health_router: APIRouter

class HealthResponse(BaseModel):
    status: Literal['ok']

def health() -> HealthResponse: ...
