from alive_progress import alive_bar as alive_bar
from ghunt.apis.playgames import PlayGames as PlayGames
from ghunt.apis.playgateway import PlayGatewayPaGrpc as PlayGatewayPaGrpc
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.objects.utils import TMPrinter as TMPrinter
from ghunt.parsers.playgames import Player as Player, PlayerProfile as PlayerProfile
from ghunt.parsers.playgateway import PlayerSearchResult as PlayerSearchResult
from typing import Any

async def get_player(ghunt_creds: GHuntCreds, as_client: Any, player_id: str) -> tuple[bool, Player]: ...
async def search_player(ghunt_creds: GHuntCreds, as_client: Any, query: str) -> list[PlayerSearchResult]: ...
