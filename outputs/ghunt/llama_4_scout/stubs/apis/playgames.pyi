from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.playgames import PlayedGames, PlayerAchievements, PlayerProfile

class PlayGames(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def get_profile(self, as_client: Any, player_id: str) -> tuple:
        ...

    async def get_played_games(self, as_client: Any, player_id: str, page_token: str = "") -> tuple:
        ...

    async def get_achievements(self, as_client: Any, player_id: str, page_token: str = "") -> tuple:
        ...