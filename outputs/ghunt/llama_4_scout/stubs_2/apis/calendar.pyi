from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.calendar import Calendar, CalendarEvents
from datetime import datetime, timezone
from typing import Any

class CalendarHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def get_calendar(self, as_client: Any, calendar_id: str) -> tuple:
        ...

    async def get_events(self, as_client: Any, calendar_id: str, params_template: str = "next_events", 
                        time_min: str = datetime.today().replace(tzinfo=timezone.utc).isoformat(), max_results: int = 250, page_token: str = "") -> tuple:
        ...