from typing import *
import httpx
from _typeshed import Incomplete
from ghunt.objects.apis import GAPI as GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.playgateway import PlayerProfile as PlayerProfile, PlayerSearchResults as PlayerSearchResults
from ghunt.protos.playgatewaypa.get_player_pb2 import GetPlayerProto as GetPlayerProto
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto as GetPlayerResponseProto
from ghunt.protos.playgatewaypa.search_player_pb2 import PlayerSearchProto as PlayerSearchProto
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto as PlayerSearchResultsProto

class PlayGatewayPaGrpc(GAPI):
    api_name: str
    package_name: str
    scopes: Incomplete
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: Incomplete
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def search_player(self, as_client: httpx.AsyncClient, query: str) -> PlayerSearchResults: ...
    async def get_player_stats(self, as_client: httpx.AsyncClient, player_id: str) -> PlayerProfile: ...
