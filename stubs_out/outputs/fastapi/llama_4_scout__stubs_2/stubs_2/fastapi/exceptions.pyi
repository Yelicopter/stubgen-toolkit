from _typeshed import Incomplete
from pydantic import BaseModel as BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException, WebSocketException as StarletteWebSocketException
from typing import Any, Dict, Optional, Sequence

class HTTPException(StarletteHTTPException):
    def __init__(self, status_code: int, detail: Optional[Any] = ..., headers: Optional[Dict[str, Any]] = ...) -> None: ...

class WebSocketException(StarletteWebSocketException):
    def __init__(self, code: int, reason: Optional[Any] = ...) -> None: ...

RequestErrorModel: Incomplete
WebSocketErrorModel: Incomplete

class FastAPIError(RuntimeError): ...

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Any]) -> None: ...
    def errors(self) -> Sequence[Any]: ...

class RequestValidationError(ValidationException):
    def __init__(self, errors: Sequence[Any], *, body: Optional[Any] = ...) -> None: ...

class WebSocketRequestValidationError(ValidationException): ...

class ResponseValidationError(ValidationException):
    def __init__(self, errors: Sequence[Any], *, body: Optional[Any] = ...) -> None: ...
