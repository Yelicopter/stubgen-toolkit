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
    headers: Dict[str, str]
    cookies: Dict[str, str]
    def __init__(self, headers: Dict[str, str], cookies: Dict) -> None: ...

class GAPI(SmartObj):
    loaded_endpoints: Dict[str, EndpointConfig]
    creds: Optional[GHuntCreds]
    headers: Dict[str, str]
    cookies: Dict[str, str]
    gen_token_lock: Optional[asyncio.Semaphore]
    authentication_mode: str
    require_key: str
    key_origin: str
    api_name: str
    package_name: str
    scopes: List[str]
    hostname: str
    scheme: str
    def __init__(self) -> None: ...

class Parser(SmartObj): ...
