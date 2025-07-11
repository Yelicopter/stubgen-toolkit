from _typeshed import Incomplete
from pydantic import BaseModel

health_router: Incomplete

class HealthResponse(BaseModel):
    status: str

def health() -> HealthResponse: ...
