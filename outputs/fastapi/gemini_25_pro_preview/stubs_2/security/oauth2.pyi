from typing import Any, Dict, List, Optional, Union, cast

from fastapi.exceptions import HTTPException
from fastapi.openapi.models import OAuth2 as OAuth2Model
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.param_functions import Form
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

class OAuth2PasswordRequestForm:
    def __init__(
        self,
        *,
        grant_type: Any = Form(default=None, regex="password"),
        username: Any = Form(),
        password: Any = Form(),
        scope: Any = Form(default=""),
        client_id: Any = Form(default=None),
        client_secret: Any = Form(default=None),
    ) -> None: ...

class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
    def __init__(
        self,
        grant_type: Any = Form(regex="password"),
        username: Any = Form(),
        password: Any = Form(),
        scope: Any = Form(default=""),
        client_id: Any = Form(default=None),
        client_secret: Any = Form(default=None),
    ) -> None: ...

class OAuth2(SecurityBase):
    def __init__(
        self,
        *,
        flows: Union[OAuthFlowsModel, Dict[str, Dict[str, Any]]] = ...,
        scheme_name: Optional[str] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2PasswordBearer(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        auto_error: bool = True,
    ) -> None: ...
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
    ) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class SecurityScopes:
    scopes: List[str]
    scope_str: str
    def __init__(self, scopes: Optional[List[str]] = None) -> None: ...