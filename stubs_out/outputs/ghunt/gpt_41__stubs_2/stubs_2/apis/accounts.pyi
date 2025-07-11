from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from typing import Any, Dict, Optional, Tuple

class Accounts(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def OAuthLogin(self, as_client: Any) -> Tuple[bool, str]: ...
