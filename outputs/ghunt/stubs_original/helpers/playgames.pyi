from typing import *
import httpx
from ghunt.apis.playgames import PlayGames as PlayGames
from ghunt.apis.playgateway import PlayGatewayPaGrpc as PlayGatewayPaGrpc
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.objects.utils import TMPrinter as TMPrinter
from ghunt.parsers.playgames import Player as Player, PlayerProfile as PlayerProfile
from ghunt.parsers.playgateway import PlayerSearchResult as PlayerSearchResult

async def get_player(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, player_id: str): ...
async def search_player(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, query: str) -> List[PlayerSearchResult]: ...
def output(player: Player): ...
