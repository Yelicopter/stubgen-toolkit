import asyncio
from ghunt.objects.base import GHuntCreds as GHuntCreds, SmartObj
from typing import Dict, Optional

class EndpointConfig(SmartObj):
    headers: Dict[str, str]
    cookies: Dict[str, str]
    def __init__(self, headers: Dict[str, str], cookies: Dict[str, str]) -> None: ...

class GAPI(SmartObj):
    loaded_endpoints: Dict[str, EndpointConfig]
    creds: Optional[GHuntCreds]
    headers: Dict[str, str]
    cookies: Dict[str, str]
    gen_token_lock: Optional[asyncio.Semaphore]
    authentication_mode: str
    require_key: str
    key_origin: str
    def __init__(self) -> None: ...

class Parser(SmartObj): ...
