from _typeshed import Incomplete
from fastapi.exceptions import HTTPException as HTTPException
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.param_functions import Form as Form
from fastapi.security.base import SecurityBase as SecurityBase
from fastapi.security.utils import get_authorization_scheme_param as get_authorization_scheme_param
from starlette.requests import Request as Request
from typing import Any, Dict, List, Optional, Union
from typing_extensions import Annotated

class OAuth2PasswordRequestForm:
    grant_type: Incomplete
    username: Incomplete
    password: Incomplete
    scopes: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    def __init__(self, *, grant_type: Annotated[Union[str, None], None, None] = ..., username: Annotated[str, None, None], password: Annotated[str, None, None], scope: Annotated[str, None, None] = ..., client_id: Annotated[Union[str, None], None, None] = ..., client_secret: Annotated[Union[str, None], None, None] = ...) -> None: ...

class OAuth2PasswordRequestFormStrict(OAuth2PasswordRequestForm):
    def __init__(self, grant_type: Annotated[str, None, None], username: Annotated[str, None, None], password: Annotated[str, None, None], scope: Annotated[str, None, None] = ..., client_id: Annotated[Union[str, None], None, None] = ..., client_secret: Annotated[Union[str, None], None, None] = ...) -> None: ...

class OAuth2(SecurityBase):
    model: Incomplete
    scheme_name: Incomplete
    auto_error: Incomplete
    def __init__(self, *, flows: Annotated[Union[OAuthFlowsModel, Dict[str, Dict[str, Any]]], None] = ..., scheme_name: Annotated[Optional[str], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2PasswordBearer(OAuth2):
    def __init__(self, tokenUrl: Annotated[str, None], scheme_name: Annotated[Optional[str], None] = ..., scopes: Annotated[Optional[Dict[str, str]], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class OAuth2AuthorizationCodeBearer(OAuth2):
    def __init__(self, authorizationUrl: str, tokenUrl: Annotated[str, None], refreshUrl: Annotated[Optional[str], None] = ..., scheme_name: Annotated[Optional[str], None] = ..., scopes: Annotated[Optional[Dict[str, str]], None] = ..., description: Annotated[Optional[str], None] = ..., auto_error: Annotated[bool, None] = ...) -> None: ...
    async def __call__(self, request: Request) -> Optional[str]: ...

class SecurityScopes:
    scopes: Incomplete
    scope_str: Incomplete
    def __init__(self, scopes: Annotated[Optional[List[str]], None] = ...) -> None: ...
