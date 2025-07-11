from ghunt.helpers.utils import *
from ghunt.errors import *
from ghunt.helpers.auth import *
from typing import *
from _typeshed import Incomplete
from ghunt.errors import GHuntCorruptedHeadersError as GHuntCorruptedHeadersError
from ghunt.helpers.knowledge import get_api_key as get_api_key, get_origin_of_key as get_origin_of_key
from ghunt.objects.base import GHuntCreds as GHuntCreds, SmartObj as SmartObj

class EndpointConfig(SmartObj):
    headers: Incomplete
    cookies: Incomplete
    def __init__(self, headers: Dict[str, str], cookies: str) -> None: ...

class GAPI(SmartObj):
    loaded_endpoints: Incomplete
    creds: Incomplete
    headers: Incomplete
    cookies: Incomplete
    gen_token_lock: Incomplete
    authentication_mode: str
    require_key: str
    key_origin: str
    def __init__(self) -> None: ...

class Parser(SmartObj): ...
