from _typeshed import Incomplete
from fastapi.exceptions import HTTPException as HTTPException
from fastapi.security.base import SecurityBase as SecurityBase
from fastapi.security.utils import get_authorization_scheme_param as get_authorization_scheme_param
from pydantic import BaseModel
from starlette.requests import Request as Request
from typing import Optional
from typing_extensions import Annotated

class HTTPBasicCredentials(BaseModel):
    username: Annotated[str, None]
    password: Annotated[str, None]

class HTTPAuthorizationCredentials(BaseModel):
    scheme: Annotated[str, None]
    credentials: Annotated[str, None]

class HTTPBase(SecurityBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, scheme: str, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...

class HTTPBasic(HTTPBase):
    model: Incomplete
    scheme_name: Incomplete
    realm: Incomplete
    auto_error: Incomplete
    def __init__(self, *, scheme_name: Annotated[Optional[str], None] = ..., realm: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPBasicCredentials]: ...

class HTTPBearer(HTTPBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, bearerFormat: Annotated[Optional[str], None] = ..., scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...

class HTTPDigest(HTTPBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...
