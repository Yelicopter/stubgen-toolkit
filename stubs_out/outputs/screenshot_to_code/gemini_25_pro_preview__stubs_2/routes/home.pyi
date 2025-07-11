from fastapi import APIRouter as APIRouter
from fastapi.responses import HTMLResponse as HTMLResponse

router: APIRouter

async def get_status() -> HTMLResponse: ...
