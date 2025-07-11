from typing import Optional, Any

class Session:
    _api_key: str
    _endpoint_url: str
    _logger: Any

    def __init__(
        self,
        endpoint_url: Optional[str] = ...,
        api_key: Optional[str] = ...,
        logger: Optional[Any] = ...,
    ): ...
    def get(self, path: str = ..., **kwargs: Any) -> Any: ...
    def post(self, path: str = ..., **kwargs: Any) -> Any: ...
    def patch(self, path: str = ..., **kwargs: Any) -> Any: ...
    def put(self, path: str = ..., **kwargs: Any) -> Any: ...
    def delete(self, path: str = ..., **kwargs: Any) -> Any: ...
    def make_request(
        self,
        method: str,
        path: str,
        headers: Any = ...,
        params: Any = ...,
        data: Any = ...,
        json: Any = ...,
        timeout: int = ...,
        **kwargs: Any,
    ) -> Any: ...

def get_PandasAI_session() -> Session: ...