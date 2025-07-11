from ghunt.objects.apis import Parser
from typing import List

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
