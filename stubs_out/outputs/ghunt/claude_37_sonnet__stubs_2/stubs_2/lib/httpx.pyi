import httpx
from typing import Any

class AsyncClient(httpx.AsyncClient):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
