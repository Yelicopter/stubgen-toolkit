from typing import Any, Dict, Optional, Tuple
from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.calendar import Calendar, CalendarEvents

class CalendarHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def get_calendar(self, as_client: Any, calendar_id: str) -> Tuple[bool, Calendar]: ...
    async def get_events(
        self,
        as_client: Any,
        calendar_id: str,
        params_template: str = ...,
        time_min: str = ...,
        max_results: int = ...,
        page_token: str = ...,
    ) -> Tuple[bool, CalendarEvents]: ...