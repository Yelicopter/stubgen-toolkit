from fastapi.security.base import SecurityBase
from starlette.exceptions import HTTPException as HTTPException
from starlette.requests import Request as Request
from starlette.status import HTTP_403_FORBIDDEN as HTTP_403_FORBIDDEN
from typing import Optional

class OpenIdConnect(SecurityBase):
    def __init__(self, *, openIdConnectUrl: str, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...
