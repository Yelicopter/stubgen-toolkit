from starlette.responses import JSONResponse as JSONResponse
from typing import Any, Optional

ujson_module: Optional[Any]
orjson_module: Optional[Any]

class UJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes: ...

class ORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes: ...
