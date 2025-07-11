from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, WebSocketRequestValidationError
from fastapi.utils import is_body_allowed_for_status_code
from fastapi.websockets import WebSocket
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, WS_1008_POLICY_VIOLATION

async def http_exception_handler(request: Request, exc: HTTPException) -> Response:
    ...

async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> Response:
    ...

async def websocket_request_validation_exception_handler(
    websocket: WebSocket, exc: WebSocketRequestValidationError
) -> None:
    ...