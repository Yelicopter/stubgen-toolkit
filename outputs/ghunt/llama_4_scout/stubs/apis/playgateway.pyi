from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds
from ghunt import globals as gb

class PlayGatewayPaGrpc(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def search_player(self, as_client: Any, query: str) -> Any:
        ...

    async def get_player_stats(self, as_client: Any, player_id: str) -> Any:
        ...