from starlette.requests import Request as Request
from typing import Any, Optional

class OpenIdConnect:
    model: Any
    scheme_name: str
    auto_error: bool
    def __init__(self, *, openIdConnectUrl: str, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...
