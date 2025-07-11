from ghunt.errors import *
from typing import *
import httpx
from ghunt.objects.apis import GAPI as GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.calendar import Calendar as Calendar, CalendarEvents as CalendarEvents

class CalendarHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def get_calendar(self, as_client: httpx.AsyncClient, calendar_id: str) -> Tuple[bool, Calendar]: ...
    async def get_events(self, as_client: httpx.AsyncClient, calendar_id: str, params_template: str = ..., time_min=..., max_results: int = ..., page_token: str = ...) -> Tuple[bool, CalendarEvents]: ...
