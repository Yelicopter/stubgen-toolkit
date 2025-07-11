from _typeshed import Incomplete
from fastapi.security.base import SecurityBase as SecurityBase
from starlette.requests import Request as Request
from typing import Optional
from typing_extensions import Annotated

class OpenIdConnect(SecurityBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, openIdConnectUrl: Annotated[str, None], scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...
