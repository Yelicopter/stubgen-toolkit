from fastapi.exceptions import HTTPException as HTTPException
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param as get_authorization_scheme_param
from starlette.requests import Request as Request
from starlette.status import HTTP_401_UNAUTHORIZED as HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN as HTTP_403_FORBIDDEN
from typing import Any, Dict, List, Optional, Union

class OAuth2PasswordRequestForm:
    def __init__(self, *, grant_type: Any = ..., username: Any = ..., password: Any = ..., scope: Any = ..., client_id: Any = ..., client_secret: Any = ...) -> None: ...

class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
    def __init__(self, grant_type: Any = ..., username: Any = ..., password: Any = ..., scope: Any = ..., client_id: Any = ..., client_secret: Any = ...) -> None: ...

class OAuth2(SecurityBase):
    def __init__(self, *, flows: Union[OAuthFlowsModel, Dict[str, Dict[str, Any]]] = ..., scheme_name: Optional[str] = ..., description: Optional[str] = ..., auto_error: bool = ...) -> None: ...
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
