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

load_dotenv()

class Session:
    _api_key: str
    _endpoint_url: str
    _logger: Logger

    def __init__(
        self,
        endpoint_url: str | None = None,
        api_key: str | None = None,
        logger: Logger | None = None,
    ) -> None:
        ...

    def get(self, path: str | None = None, **kwargs) -> dict:
        ...

    def post(self, path: str | None = None, **kwargs) -> dict:
        ...

    def patch(self, path: str | None = None, **kwargs) -> dict:
        ...

    def put(self, path: str | None = None, **kwargs) -> dict:
        ...

    def delete(self, path: str | None = None, **kwargs) -> dict:
        ...

    def make_request(
        self,
        method: str,
        path: str | None,
        headers: dict | None = None,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        timeout: int = 300,
        **kwargs,
    ) -> dict:
        ...

    def get_PandasAI_session() -> "Session":
        ...