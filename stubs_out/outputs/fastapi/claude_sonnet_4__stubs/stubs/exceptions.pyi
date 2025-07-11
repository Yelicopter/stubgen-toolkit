from pydantic import BaseModel as BaseModel, create_model as create_model
from starlette.exceptions import HTTPException as StarletteHTTPException, WebSocketException as StarletteWebSocketException
from typing import Any, Dict, Optional, Sequence, Type

class HTTPException(StarletteHTTPException):
    def __init__(self, status_code: int, detail: Any = ..., headers: Optional[Dict[str, Any]] = ...) -> None: ...

class WebSocketException(StarletteWebSocketException):
    def __init__(self, code: int, reason: Optional[str] = ...) -> None: ...

RequestErrorModel: Type[BaseModel]
WebSocketErrorModel: Type[BaseModel]

class FastAPIError(RuntimeError): ...

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Any]) -> None: ...
    def errors(self) -> Sequence[Any]: ...

class RequestValidationError(ValidationException):
    body: Any
    def __init__(self, errors: Sequence[Any], *, body: Any = ...) -> None: ...

class WebSocketRequestValidationError(ValidationException): ...

class ResponseValidationError(ValidationException):
    body: Any
    def __init__(self, errors: Sequence[Any], *, body: Any = ...) -> None: ...
