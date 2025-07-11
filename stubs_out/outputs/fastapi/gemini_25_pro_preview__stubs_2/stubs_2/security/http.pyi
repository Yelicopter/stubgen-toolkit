from fastapi.exceptions import HTTPException as HTTPException
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param as get_authorization_scheme_param
from pydantic import BaseModel
from starlette.requests import Request as Request
from starlette.status import HTTP_401_UNAUTHORIZED as HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN as HTTP_403_FORBIDDEN
from typing import Any, Optional

class HTTPBasicCredentials(BaseModel):
    username: str
    password: str

class HTTPAuthorizationCredentials(BaseModel):
    scheme: str
    credentials: str

class HTTPBase(SecurityBase):
    def __init__(self, *, scheme: str, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[Any]: ...

class HTTPBasic(HTTPBase):
    def __init__(self, *, scheme_name: Optional[str] = ..., realm: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPBasicCredentials]: ...

class HTTPBearer(HTTPBase):
    def __init__(self, *, bearerFormat: Optional[str] = ..., scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...

class HTTPDigest(HTTPBase):
    def __init__(self, *, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...
