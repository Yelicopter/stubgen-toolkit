import httpx
from http.cookiejar import CookieJar as CookieJar
from httpx._types import CookieTypes as CookieTypes
from typing import Any

class AsyncClient(httpx.AsyncClient):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
