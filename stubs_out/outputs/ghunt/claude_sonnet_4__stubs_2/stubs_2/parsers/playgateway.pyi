from typing import *
from ghunt.objects.apis import Parser
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto as GetPlayerResponseProto
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto as PlayerSearchResultsProto

class PlayerSearchResult(Parser):
    def __init__(self) -> None: ...
    name: str
    id: str
    avatar_url: str

class PlayerSearchResults(Parser):
    def __init__(self) -> None: ...
    results: List[PlayerSearchResult]

class PlayerProfile(Parser):
    def __init__(self) -> None: ...
    achievements_count: int
    played_games_count: int
