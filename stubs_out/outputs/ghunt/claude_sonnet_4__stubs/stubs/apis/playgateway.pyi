from typing import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.playgateway import PlayerProfile as PlayerProfile, PlayerSearchResults as PlayerSearchResults
from ghunt.protos.playgatewaypa.get_player_pb2 import GetPlayerProto as GetPlayerProto
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto as GetPlayerResponseProto
from ghunt.protos.playgatewaypa.search_player_pb2 import PlayerSearchProto as PlayerSearchProto
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto as PlayerSearchResultsProto
from struct import pack as pack

class PlayGatewayPaGrpc(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def search_player(self, as_client: httpx.AsyncClient, query: str) -> PlayerSearchResults: ...
    async def get_player_stats(self, as_client: httpx.AsyncClient, player_id: str) -> PlayerProfile: ...
