from fastapi import APIRouter as APIRouter, WebSocket as WebSocket

router: APIRouter

async def stream_code(websocket: WebSocket) -> None: ...
