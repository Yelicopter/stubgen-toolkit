from _typeshed import Incomplete
from fastapi.openapi.models import APIKey as APIKey, APIKeyIn as APIKeyIn
from fastapi.security.base import SecurityBase as SecurityBase
from starlette.requests import Request as Request
from typing import Optional
from typing_extensions import Annotated

class APIKeyBase(SecurityBase):
    @staticmethod
    def check_api_key(api_key: Optional[str], auto_error: bool) -> Optional[str]: ...

class APIKeyQuery(APIKeyBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, name: Annotated[str, None], scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class APIKeyHeader(APIKeyBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, name: Annotated[str, None], scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class APIKeyCookie(APIKeyBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, name: Annotated[str, None], scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...
