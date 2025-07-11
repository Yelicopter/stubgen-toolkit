from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from fastapi.websockets import WebSocket
from fastapi.exceptions import RequestValidationError, WebSocketRequestValidationError

async def http_exception_handler(request: Request, exc: Exception) -> Response: ...
async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse: ...
async def websocket_request_validation_exception_handler(
    websocket: WebSocket, exc: WebSocketRequestValidationError
) -> None: ...