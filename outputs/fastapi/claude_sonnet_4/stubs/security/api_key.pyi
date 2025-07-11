from typing import Optional

from fastapi.openapi.models import APIKey, APIKeyIn
from fastapi.security.base import SecurityBase
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN
from typing_extensions import Annotated, Doc

class APIKeyBase(SecurityBase):
    @staticmethod
    def check_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]:
        ...

class APIKeyQuery(APIKeyBase):
    def __init__(
        self,
        *,
        name: str,
        scheme_name: Optional[str] = ...,
        description: Optional[str] = ...,
        auto_error: bool = ...,
    ) -> None:
        ...

    async def __call__(self, request: Request) -> Optional[str]:
        ...

class APIKeyHeader(APIKeyBase):
    def __init__(
        self,
        *,
        name: str,
        scheme_name: Optional[str] = ...,
        description: Optional[str] = ...,
        auto_error: bool = ...,
    ) -> None:
        ...

    async def __call__(self, request: Request) -> Optional[str]:
        ...

class APIKeyCookie(APIKeyBase):
    def __init__(
        self,
        *,
        name: str,
        scheme_name: Optional[str] = ...,
        description: Optional[str] = ...,
        auto_error: bool = ...,
    ) -> None:
        ...

    async def __call__(self, request: Request) -> Optional[str]:
        ...