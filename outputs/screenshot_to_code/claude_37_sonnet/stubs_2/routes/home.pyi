from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router: APIRouter

@router.get("/")
async def get_status() -> HTMLResponse: ...