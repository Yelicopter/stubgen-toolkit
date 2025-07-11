from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds
from ghunt import globals as gb
from ghunt.protos.playgatewaypa.search_player_pb2 import PlayerSearchProto
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto
from ghunt.protos.playgatewaypa.get_player_pb2 import GetPlayerProto
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto
from ghunt.parsers.playgateway import PlayerSearchResults
from ghunt.parsers.playgateway import PlayerProfile
import httpx
from typing import *
from struct import pack
import inspect

class PlayGatewayPaGrpc(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    async def search_player(self, as_client: httpx.AsyncClient, query: str) -> PlayerSearchResults: ...
    async def get_player_stats(self, as_client: httpx.AsyncClient, player_id: str) -> PlayerProfile: ...