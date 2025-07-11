from typing import *
from ghunt.objects.apis import Parser
from ghunt.protos.playgatewaypa.get_player_response_pb2 import GetPlayerResponseProto as GetPlayerResponseProto
from ghunt.protos.playgatewaypa.search_player_results_pb2 import PlayerSearchResultsProto as PlayerSearchResultsProto

class PlayerSearchResult(Parser):
    name: str
    id: str
    avatar_url: str
    def __init__(self) -> None: ...

class PlayerSearchResults(Parser):
    results: List[PlayerSearchResult]
    def __init__(self) -> None: ...

class PlayerProfile(Parser):
    achievements_count: int
    played_games_count: int
    def __init__(self) -> None: ...
