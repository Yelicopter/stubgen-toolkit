import logging
import os
import traceback
from typing import Optional
from urllib.parse import urljoin
import requests
from pandasai.constants import DEFAULT_API_URL
from pandasai.exceptions import PandasAIApiCallError, PandasAIApiKeyError
from pandasai.helpers import load_dotenv
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
    
    def get(self, path: Optional[str] = None, **kwargs) -> any: ...
    def post(self, path: Optional[str] = None, **kwargs) -> any: ...
    def patch(self, path: Optional[str] = None, **kwargs) -> any: ...
    def put(self, path: Optional[str] = None, **kwargs) -> any: ...
    def delete(self, path: Optional[str] = None, **kwargs) -> any: ...
    def make_request(
        self,
        method: str,
        path: str,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        data: Optional[any] = None,
        json: Optional[dict] = None,
        timeout: int = 300,
        **kwargs,
    ) -> any: ...

def get_PandasAI_session() -> Session: ...