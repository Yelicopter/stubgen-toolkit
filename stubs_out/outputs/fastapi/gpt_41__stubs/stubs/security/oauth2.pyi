from starlette.requests import Request as Request
from typing import Any, Dict, List, Optional

class OAuth2PasswordRequestForm:
    grant_type: Optional[str]
    username: str
    password: str
    scopes: List[str]
    client_id: Optional[str]
    client_secret: Optional[str]
    def __init__(self, *, grant_type: Optional[str] = ..., username: str, password: str, scope: str = ..., client_id: Optional[str] = ..., client_secret: Optional[str] = ...) -> None: ...

class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
    def __init__(self, grant_type: str, username: str, password: str, scope: str = ..., client_id: Optional[str] = ..., client_secret: Optional[str] = ...) -> None: ...

class OAuth2:
    model: Any
    scheme_name: str
    auto_error: bool
    def __init__(self, *, flows: Any = ..., scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2PasswordBearer(OAuth2):
    def __init__(self, tokenUrl: str, scheme_name: Optional[str] = ..., scopes: Optional[Dict[str, str]] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2AuthorizationCodeBearer(OAuth2):
    def __init__(self, authorizationUrl: str, tokenUrl: str, refreshUrl: Optional[str] = ..., scheme_name: Optional[str] = ..., scopes: Optional[Dict[str, str]] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class SecurityScopes:
    scopes: List[str]
    scope_str: str
    def __init__(self, scopes: Optional[List[str]] = ...) -> None: ...
