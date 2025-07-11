from ghunt.objects.base import GHuntCreds
from ghunt.apis.playgames import PlayGames
from ghunt.apis.playgateway import PlayGatewayPaGrpc
from ghunt.parsers.playgames import Player, PlayerProfile
from ghunt.parsers.playgateway import PlayerSearchResult
from ghunt.objects.utils import TMPrinter
import httpx
from typing import List, Tuple

async def get_player(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, player_id: str) -> Tuple[bool, Player]: ...
async def search_player(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, query: str) -> List[PlayerSearchResult]: ...
def output(player: Player) -> None: ...