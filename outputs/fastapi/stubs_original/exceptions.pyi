from _typeshed import Incomplete
from pydantic import BaseModel as BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException, WebSocketException as StarletteWebSocketException
from typing import Any, Dict, Optional, Sequence, Type, Union
from typing_extensions import Annotated

class HTTPException(StarletteHTTPException):
    def __init__(self, status_code: Annotated[int, None], detail: Annotated[Any, None] = ..., headers: Annotated[Optional[Dict[str, str]], None] = ...) -> None: ...

class WebSocketException(StarletteWebSocketException):
    def __init__(self, code: Annotated[int, None], reason: Annotated[Union[str, None], None] = ...) -> None: ...

RequestErrorModel: Type[BaseModel]
WebSocketErrorModel: Type[BaseModel]

class FastAPIError(RuntimeError): ...

class ValidationException(Exception):
    def __init__(self, errors: Sequence[Any]) -> None: ...
    def errors(self) -> Sequence[Any]: ...

class RequestValidationError(ValidationException):
    body: Incomplete
    def __init__(self, errors: Sequence[Any], *, body: Any = ...) -> None: ...

class WebSocketRequestValidationError(ValidationException): ...

class ResponseValidationError(ValidationException):
    body: Incomplete
    def __init__(self, errors: Sequence[Any], *, body: Any = ...) -> None: ...
