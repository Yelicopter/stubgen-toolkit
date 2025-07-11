from typing import Any, Dict, Optional, Sequence, Type, Union

from pydantic import BaseModel, create_model
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.exceptions import WebSocketException as StarletteWebSocketException
from typing_extensions import Annotated, Doc

class HTTPException(StarletteHTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> None: ...

class WebSocketException(StarletteWebSocketException):
    def __init__(
        self,
        code: int,
        reason: Optional[str] = None,
    ) -> None: ...

RequestErrorModel: Type[BaseModel]
WebSocketErrorModel: Type[BaseModel]

class FastAPIError(RuntimeError):
    pass

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Dict[str, Any]]) -> None: ...
    def errors(self) -> Sequence[Dict[str, Any]]: ...

class RequestValidationError(ValidationException):
    def __init__(self, errors: Sequence[Dict[str, Any]], *, body: Any = None) -> None: ...

class WebSocketRequestValidationError(ValidationException):
    pass

class ResponseValidationError(ValidationException):
    def __init__(self, errors: Sequence[Dict[str, Any]], *, body: Any = None) -> None: ...
    def __str__(self) -> str: ...