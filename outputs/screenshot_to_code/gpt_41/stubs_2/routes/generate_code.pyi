from fastapi import APIRouter, WebSocket

router: APIRouter

async def stream_code(websocket: WebSocket) -> None: ...