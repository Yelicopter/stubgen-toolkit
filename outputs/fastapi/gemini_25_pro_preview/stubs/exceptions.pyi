from typing import Any, Dict, Optional, Sequence, Type, Union

from pydantic import BaseModel
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
    def __init__(self, code: int, reason: Optional[str] = None) -> None: ...

RequestErrorModel: Type[BaseModel]
WebSocketErrorModel: Type[BaseModel]

class FastAPIError(RuntimeError): ...

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Any]) -> None: ...
    def errors(self) -> Sequence[Any]: ...

class RequestValidationError(ValidationException):
    body: Any
    def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None: ...

class WebSocketRequestValidationError(ValidationException): ...

class ResponseValidationError(ValidationException):
    body: Any
    def __init__(self, errors: Sequence[Any], *, body: Any = None) -> None: ...
    def __str__(self) -> str: ...