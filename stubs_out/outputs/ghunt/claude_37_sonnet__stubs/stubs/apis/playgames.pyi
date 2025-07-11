from ghunt.errors import *
from typing import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.playgames import PlayedGames as PlayedGames, PlayerAchievements as PlayerAchievements, PlayerProfile as PlayerProfile

class PlayGames(GAPI):
    api_name: str
    package_name: str
    scopes: List[str]
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: Optional[str]
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def get_profile(self, as_client: httpx.AsyncClient, player_id: str) -> Tuple[bool, PlayerProfile]: ...
    async def get_played_games(self, as_client: httpx.AsyncClient, player_id: str, page_token: str = ...) -> Tuple[bool, str, PlayedGames]: ...
    async def get_achievements(self, as_client: httpx.AsyncClient, player_id: str, page_token: str = ...) -> Tuple[bool, str, PlayerAchievements]: ...
