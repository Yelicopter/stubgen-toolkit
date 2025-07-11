from typing import Any, Dict, Optional

from starlette.responses import (
    FileResponse as FileResponse,
    HTMLResponse as HTMLResponse,
    JSONResponse as JSONResponse,
    PlainTextResponse as PlainTextResponse,
    RedirectResponse as RedirectResponse,
    Response as Response,
    StreamingResponse as StreamingResponse,
)

try:
    import ujson
except ImportError:  
    ujson = None  

try:
    import orjson
except ImportError:  
    orjson = None  

class UJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        ...

class ORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        ...