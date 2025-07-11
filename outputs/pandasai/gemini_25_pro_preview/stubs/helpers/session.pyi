from typing import Any, Optional

from pandasai.helpers.logger import Logger

class Session:
    _api_key: str
    _endpoint_url: str
    _logger: Logger
    def __init__(
        self,
        endpoint_url: Optional[str] = ...,
        api_key: Optional[str] = ...,
        logger: Optional[Logger] = ...,
    ) -> None: ...
    def get(self, path: Optional[str] = ..., **kwargs: Any) -> Any: ...
    def post(self, path: Optional[str] = ..., **kwargs: Any) -> Any: ...
    def patch(self, path: Optional[str] = ..., **kwargs: Any) -> Any: ...
    def put(self, path: Optional[str] = ..., **kwargs: Any) -> Any: ...
    def delete(self, path: Optional[str] = ..., **kwargs: Any) -> Any: ...
    def make_request(
        self,
        method: str,
        path: str,
        headers: Optional[dict[str, str]] = ...,
        params: Optional[dict[str, Any]] = ...,
        data: Optional[Any] = ...,
        json: Optional[Any] = ...,
        timeout: int = ...,
        **kwargs: Any,
    ) -> Any: ...

def get_PandasAI_session() -> Session: ...