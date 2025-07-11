from typing import Dict, List

class PlayerSearchResult:
    def __init__(self) -> None:
        self.name: str = ""
        self.id: str = ""
        self.avatar_url: str = ""

    def _scrape(self, player_result_data: Dict) -> None:
        ...

class PlayerSearchResults:
    def __init__(self) -> None:
        self.results: List[PlayerSearchResult] = []

    def _scrape(self, proto_results: Dict) -> None:
        ...

class PlayerProfile:
    def __init__(self) -> None:
        self.achievements_count: int = 0
        self.played_games_count: int = 0

    def _scrape(self, proto_results: Dict) -> None:
        ...