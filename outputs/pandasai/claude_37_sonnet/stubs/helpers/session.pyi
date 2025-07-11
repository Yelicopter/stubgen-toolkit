import logging
import os
import traceback
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests

from pandasai.constants import DEFAULT_API_URL
from pandasai.exceptions import PandasAIApiCallError, PandasAIApiKeyError
from pandasai.helpers import load_dotenv
from pandasai.helpers.logger import Logger

class Session:
    _api_key: str
    _endpoint_url: str
    _version_path: str
    _logger: Logger
    
    def __init__(
        self,
        endpoint_url: Optional[str] = None,
        api_key: Optional[str] = None,
        logger: Optional[Logger] = None,
    ) -> None: ...
    
    def get(self, path=None, **kwargs) -> Any: ...
    
    def post(self, path=None, **kwargs) -> Any: ...
    
    def patch(self, path=None, **kwargs) -> Any: ...
    
    def put(self, path=None, **kwargs) -> Any: ...
    
    def delete(self, path=None, **kwargs) -> Any: ...
    
    def make_request(
        self,
        method,
        path,
        headers=None,
        params=None,
        data=None,
        json=None,
        timeout=300,
        **kwargs,
    ) -> Any: ...

def get_PandasAI_session() -> Session: ...