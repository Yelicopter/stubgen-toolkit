from typing import Any, Optional

from fastapi.exceptions import HTTPException
from fastapi.openapi.models import HTTPBase as HTTPBaseModel
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import BaseModel
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

class HTTPBasicCredentials(BaseModel):
    username: str
    password: str

class HTTPAuthorizationCredentials(BaseModel):
    scheme: str
    credentials: str

class HTTPBase(SecurityBase):
    def __init__(
        self,
        *,
        scheme: str,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ) -> None: ...
    async def __call__(
        self, request: Request
    ) -> Optional[Any]: ...

class HTTPBasic(HTTPBase):
    def __init__(
        self,
        *,
        scheme_name: Optional[str] = None,
        realm: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPBasicCredentials]: ...

class HTTPBearer(HTTPBase):
    def __init__(
        self,
        *,
        bearerFormat: Optional[str] = None,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ) -> None: ...
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]: ...

class HTTPDigest(HTTPBase):
    def __init__(
        self,
        *,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ) -> None: ...
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]: ...