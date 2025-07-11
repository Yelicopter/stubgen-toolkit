from ghunt.errors import GHuntCorruptedHeadersError
from ghunt.helpers.knowledge import get_origin_of_key, get_api_key
from ghunt.objects.base import GHuntCreds, SmartObj
from ghunt.helpers.utils import *
from ghunt.errors import *
from ghunt.helpers.auth import *

import httpx

from datetime import datetime, timezone
from typing import Any, Dict

class EndpointConfig(SmartObj):
    ...

class GAPI(SmartObj):
    ...

    def _load_api(self, creds: GHuntCreds, headers: Dict[str, str]) -> None:
        ...

    def _load_endpoint(self, endpoint_name: str, headers: Dict[str, str] = {}, ext_metadata: Dict[str, Any] = {}) -> None:
        ...

    async def _check_and_gen_authorization_token(self, as_client: Any, creds: GHuntCreds) -> str:
        ...

    async def _query(self, as_client: Any, verb: str, endpoint_name: str, base_url: str, params: Dict[str, Any] = None, data: Any = None, data_type: str = None) -> Any:
        ...