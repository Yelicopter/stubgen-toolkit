from typing import Any
from starlette.responses import FileResponse as FileResponse
from starlette.responses import HTMLResponse as HTMLResponse
from starlette.responses import JSONResponse as JSONResponse
from starlette.responses import PlainTextResponse as PlainTextResponse
from starlette.responses import RedirectResponse as RedirectResponse
from starlette.responses import Response as Response
from starlette.responses import StreamingResponse as StreamingResponse

class UJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes: ...

class ORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes: ...