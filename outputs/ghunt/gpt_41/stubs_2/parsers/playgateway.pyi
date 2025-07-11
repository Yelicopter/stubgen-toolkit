from typing import Any, List
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
    def _scrape(self, proto_results: Any) -> None: ...

class PlayerProfile(Parser):
    achievements_count: int
    played_games_count: int
    def __init__(self) -> None: ...
    def _scrape(self, proto_results: Any) -> None: ...