from typing import List, Any
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto
from ghunt.objects.apis import Parser

class PlayerSearchResult(Parser):
    name: str
    id: str
    avatar_url: str
    def __init__(self) -> None: ...
    def _scrape(self, player_result_data: Any) -> None: ...

class PlayerSearchResults(Parser):
    results: List[PlayerSearchResult]
    def __init__(self) -> None: ...
    def _scrape(self, proto_results: PlayerSearchResultsProto) -> None: ...

class PlayerProfile(Parser):
    achievements_count: int
    played_games_count: int
    def __init__(self) -> None: ...
    def _scrape(self, proto_results: GetPlayerResponseProto) -> None: ...
