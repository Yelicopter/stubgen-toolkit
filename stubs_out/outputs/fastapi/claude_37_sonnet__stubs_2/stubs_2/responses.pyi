from starlette.responses import JSONResponse as JSONResponse
from typing import Any, Optional, Type

ujson_module: Optional[Type[Any]]
orjson_module: Optional[Type[Any]]

class UJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes: ...

class ORJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes: ...
