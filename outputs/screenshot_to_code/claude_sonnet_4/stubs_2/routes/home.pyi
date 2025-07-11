from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router: APIRouter

async def get_status() -> HTMLResponse: ...