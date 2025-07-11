from typing import Dict, List

from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto
from ghunt.objects.apis import Parser

class PlayerSearchResult(Parser):
    def __init__(self) -> None:
        self.name: str = ""
        self.id: str = ""
        self.avatar_url: str = ""

    def _scrape(self, player_result_data: Dict) -> None:
        ...

class PlayerSearchResults(Parser):
    def __init__(self) -> None:
        self.results: List[PlayerSearchResult] = []

    def _scrape(self, proto_results: Dict) -> None:
        ...

class PlayerProfile(Parser):
    def __init__(self) -> None:
        self.achievements_count: int = 0
        self.played_games_count: int = 0

    def _scrape(self, proto_results: Dict) -> None:
        ...