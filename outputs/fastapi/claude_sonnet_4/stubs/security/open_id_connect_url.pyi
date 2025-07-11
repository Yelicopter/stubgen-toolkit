from typing import Optional

from fastapi.openapi.models import OpenIdConnect as OpenIdConnectModel
from fastapi.security.base import SecurityBase
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN
from typing_extensions import Annotated, Doc

class OpenIdConnect(SecurityBase):
    def __init__(
        self,
        *,
        openIdConnectUrl: str,
        scheme_name: Optional[str] = ...,
        description: Optional[str] = ...,
        auto_error: bool = ...,
    ) -> None:
        ...

    async def __call__(self, request: Request) -> Optional[str]:
        ...