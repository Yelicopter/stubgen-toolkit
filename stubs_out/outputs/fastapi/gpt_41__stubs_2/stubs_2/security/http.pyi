from pydantic import BaseModel
from starlette.requests import Request as Request
from typing import Any, Optional

class HTTPBasicCredentials(BaseModel):
    username: str
    password: str

class HTTPAuthorizationCredentials(BaseModel):
    scheme: str
    credentials: str

class HTTPBase:
    model: Any
    scheme_name: str
    auto_error: bool
    def __init__(self, *, scheme: str, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...

class HTTPBasic(HTTPBase):
    realm: Optional[str]
    def __init__(self, *, scheme_name: Optional[str] = ..., realm: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPBasicCredentials]: ...

class HTTPBearer(HTTPBase):
    def __init__(self, *, bearerFormat: Optional[str] = ..., scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...

class HTTPDigest(HTTPBase):
    def __init__(self, *, scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]: ...
