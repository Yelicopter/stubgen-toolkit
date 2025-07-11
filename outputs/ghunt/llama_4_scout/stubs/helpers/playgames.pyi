from ghunt.objects.base import GHuntCreds
from ghunt.apis.playgames import PlayGames
from ghunt.apis.playgateway import PlayGatewayPaGrpc
from ghunt.parsers.playgames import Player, PlayerProfile
from ghunt.parsers.playgateway import PlayerSearchResult
from ghunt.objects.utils import TMPrinter

import httpx
from alive_progress import alive_bar

async def get_player(ghunt_creds: GHuntCreds, as_client: Any, player_id: str) -> tuple[bool, Player]:
    ...

async def search_player(ghunt_creds: GHuntCreds, as_client: Any, query: str) -> list[PlayerSearchResult]:
    ...