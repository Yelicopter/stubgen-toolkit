from _typeshed import Incomplete
from pydantic import BaseModel
from typing import Literal

health_router: Incomplete

class HealthResponse(BaseModel):
    status: Literal['ok']

def health() -> HealthResponse: ...
