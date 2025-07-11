from fastapi import APIRouter as APIRouter, HTTPException as HTTPException
from pydantic import BaseModel

router: APIRouter

def normalize_url(url: str) -> str: ...
def bytes_to_data_url(image_bytes: bytes, mime_type: str) -> str: ...
async def capture_screenshot(target_url: str, api_key: str, device: str = ...) -> bytes: ...

class ScreenshotRequest(BaseModel):
    url: str
    apiKey: str

class ScreenshotResponse(BaseModel):
    url: str

async def app_screenshot(request: ScreenshotRequest) -> ScreenshotResponse: ...
