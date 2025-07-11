import httpx

class AsyncClient(httpx.AsyncClient):
    def __init__(self, *args, **kwargs) -> None: ...
