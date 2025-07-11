from typing import Any, Awaitable, Callable, Dict, List

def extract_image_from_messages(
    messages: List[Dict[str, Any]],
) -> Dict[str, str]: ...

async def stream_gemini_response(
    messages: List[Dict[str, Any]],
    api_key: str,
    callback: Callable[[str], Awaitable[None]],
    model_name: str,
) -> Dict[str, Any]: ...