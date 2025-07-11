from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.playgames import PlayedGames, PlayerAchievements, PlayerProfile
import httpx
from typing import *
import inspect
import json

class PlayGames(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    async def get_profile(self, as_client: httpx.AsyncClient, player_id: str) -> Tuple[bool, PlayerProfile]: ...
    async def get_played_games(self, as_client: httpx.AsyncClient, player_id: str, page_token: str = "") -> Tuple[bool, str, PlayedGames]: ...
    async def get_achievements(self, as_client: httpx.AsyncClient, player_id: str, page_token: str = "") -> Tuple[bool, str, PlayerAchievements]: ...