import logging
import os
import traceback
from typing import Optional, Any
from urllib.parse import urljoin
import requests
from pandasai.constants import DEFAULT_API_URL
from pandasai.exceptions import PandasAIApiCallError, PandasAIApiKeyError
from pandasai.helpers.logger import Logger

class Session:
    _api_key: str
    _endpoint_url: str
    _logger: Logger
    
    def __init__(
        self,
        endpoint_url: Optional[str] = None,
        api_key: Optional[str] = None,
        logger: Optional[Logger] = None,
    ) -> None: ...
    
    def get(self, path: Optional[str] = None, **kwargs) -> Any: ...
    def post(self, path: Optional[str] = None, **kwargs) -> Any: ...
    def patch(self, path: Optional[str] = None, **kwargs) -> Any: ...
    def put(self, path: Optional[str] = None, **kwargs) -> Any: ...
    def delete(self, path: Optional[str] = None, **kwargs) -> Any: ...
    def make_request(
        self,
        method: str,
        path: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        data: Optional[Any] = None,
        json: Optional[dict] = None,
        timeout: int = 300,
        **kwargs,
    ) -> Any: ...

def get_PandasAI_session() -> Session: ...