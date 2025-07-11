from fastapi import APIRouter as APIRouter
from pydantic import BaseModel, Field as Field

health_router: APIRouter

class HealthResponse(BaseModel):
    status: str

def health() -> HealthResponse: ...
