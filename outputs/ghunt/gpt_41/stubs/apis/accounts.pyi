from typing import Any, Dict, Optional, Tuple
from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI

class Accounts(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def OAuthLogin(self, as_client: Any) -> Tuple[bool, str]: ...