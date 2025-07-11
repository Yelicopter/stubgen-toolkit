from typing import Any, Dict, List, Optional, Union, cast

from fastapi.exceptions import HTTPException
from fastapi.openapi.models import OAuth2 as OAuth2Model
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.param_functions import Form
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN
from typing_extensions import Annotated, Doc

class OAuth2PasswordRequestForm:
    def __init__(
        self,
        *,
        grant_type: Optional[str] = None,
        username: str,
        password: str,
        scope: str = "",
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ): ...

class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
    def __init__(
        self,
        grant_type: str,
        username: str,
        password: str,
        scope: str = "",
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ): ...

class OAuth2(SecurityBase):
    def __init__(
        self,
        *,
        flows: OAuthFlowsModel = OAuthFlowsModel(),
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ): ...

    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2PasswordBearer(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ): ...

    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2AuthorizationCodeBearer(OAuth2):
    def __init__(
        self,
        authorizationUrl: str,
        tokenUrl: str,
        refreshUrl: Optional[str] = None,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ): ...

    async def __call__(self, request: Request) -> Optional[str]: ...

class SecurityScopes:
    def __init__(
        self,
        scopes: Optional[List[str]] = None,
    ): ...
    scopes: List[str]
    scope_str: str