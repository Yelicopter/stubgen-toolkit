from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.calendar import Calendar, CalendarEvents
import httpx
from typing import Dict, Tuple

class CalendarHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def get_calendar(self, as_client: httpx.AsyncClient, calendar_id: str) -> Tuple[bool, Calendar]: ...
    async def get_events(
        self,
        as_client: httpx.AsyncClient,
        calendar_id: str,
        params_template: str = ...,
        time_min: str = ...,
        max_results: int = ...,
        page_token: str = ...,
    ) -> Tuple[bool, CalendarEvents]: ...