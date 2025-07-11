from typing import *
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto
from ghunt.objects.apis import Parser

class PlayerSearchResult(Parser):
    def __init__(self) -> None: ...
    name: str
    id: str
    avatar_url: str
    
    def _scrape(self, player_result_data: Any) -> None: ...

class PlayerSearchResults(Parser):
    def __init__(self) -> None: ...
    results: List[PlayerSearchResult]
    
    def _scrape(self, proto_results: PlayerSearchResultsProto) -> None: ...

class PlayerProfile(Parser):
    def __init__(self) -> None: ...
    achievements_count: int
    played_games_count: int
    
    def _scrape(self, proto_results: GetPlayerResponseProto) -> None: ...