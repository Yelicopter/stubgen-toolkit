from ghunt.helpers.utils import *
from ghunt.errors import *
from ghunt.helpers.auth import *
from typing import *
import asyncio
from datetime import datetime as datetime, timezone as timezone
from ghunt.errors import GHuntCorruptedHeadersError as GHuntCorruptedHeadersError
from ghunt.helpers.knowledge import get_api_key as get_api_key, get_origin_of_key as get_origin_of_key
from ghunt.objects.base import GHuntCreds as GHuntCreds, SmartObj

class EndpointConfig(SmartObj):
    def __init__(self, headers: Dict[str, str], cookies: str) -> None: ...
    headers: Dict[str, str]
    cookies: str

class GAPI(SmartObj):
    def __init__(self) -> None: ...
    loaded_endpoints: Dict[str, EndpointConfig]
    creds: Optional[GHuntCreds]
    headers: Dict[str, str]
    cookies: Dict[str, str]
    gen_token_lock: Optional[asyncio.Semaphore]
    authentication_mode: str
    require_key: str
    key_origin: str

class Parser(SmartObj): ...
