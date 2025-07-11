from typing import Any, Dict, Optional, Tuple
from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.people import Person

class PeoplePaHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def people_lookup(
        self,
        as_client: Any,
        email: str,
        params_template: str = ...,
    ) -> Tuple[bool, Person]: ...
    async def people(
        self,
        as_client: Any,
        gaia_id: str,
        params_template: str = ...,
    ) -> Tuple[bool, Person]: ...