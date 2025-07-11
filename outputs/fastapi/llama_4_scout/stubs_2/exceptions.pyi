from typing import Any, Dict, Optional, Sequence, Type, Union

from pydantic import BaseModel, create_model
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.exceptions import WebSocketException as StarletteWebSocketException

class HTTPException(StarletteHTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Optional[Any] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> None:
        ...

class WebSocketException(StarletteWebSocketException):
    def __init__(
        self,
        code: int,
        reason: Optional[Any] = None,
    ) -> None:
        ...

RequestErrorModel = create_model("Request")
WebSocketErrorModel = create_model("WebSocket")

class FastAPIError(RuntimeError):
    ...

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Any]) -> None:
        ...

    def errors(self) -> Sequence[Any]:
        ...

class RequestValidationError(ValidationException):
    def __init__(self, errors: Sequence[Any], *, body: Optional[Any] = None) -> None:
        ...

class WebSocketRequestValidationError(ValidationException):
    ...

class ResponseValidationError(ValidationException):
    def __init__(self, errors: Sequence[Any], *, body: Optional[Any] = None) -> None:
        ...

    def __str__(self) -> str:
        ...