from ghunt.errors import *
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.calendar import Calendar as Calendar, CalendarEvents as CalendarEvents
from typing import Any

class CalendarHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = ...) -> None: ...
    async def get_calendar(self, as_client: Any, calendar_id: str) -> tuple: ...
    async def get_events(self, as_client: Any, calendar_id: str, params_template: str = ..., time_min: str = ..., max_results: int = ..., page_token: str = ...) -> tuple: ...
