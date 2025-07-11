import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.playgateway import PlayerProfile as PlayerProfile, PlayerSearchResults as PlayerSearchResults
from typing import Dict

class PlayGatewayPaGrpc(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def search_player(self, as_client: httpx.AsyncClient, query: str) -> PlayerSearchResults: ...
    async def get_player_stats(self, as_client: httpx.AsyncClient, player_id: str) -> PlayerProfile: ...
