from fastapi.encoders import jsonable_encoder as jsonable_encoder
from starlette.responses import HTMLResponse
from typing import Any, Dict, Optional
from typing_extensions import Annotated

swagger_ui_default_parameters: Annotated[Dict[str, Any], None]

def get_swagger_ui_html(*, openapi_url: Annotated[str, None], title: Annotated[str, None], swagger_js_url: Annotated[str, None] = ..., swagger_css_url: Annotated[str, None] = ..., swagger_favicon_url: Annotated[str, None] = ..., oauth2_redirect_url: Annotated[Optional[str], None] = ..., init_oauth: Annotated[Optional[Dict[str, Any]], None] = ..., swagger_ui_parameters: Annotated[Optional[Dict[str, Any]], None] = ...) -> HTMLResponse: ...
def get_redoc_html(*, openapi_url: Annotated[str, None], title: Annotated[str, None], redoc_js_url: Annotated[str, None] = ..., redoc_favicon_url: Annotated[str, None] = ..., with_google_fonts: Annotated[bool, None] = ...) -> HTMLResponse: ...
def get_swagger_ui_oauth2_redirect_html() -> HTMLResponse: ...
