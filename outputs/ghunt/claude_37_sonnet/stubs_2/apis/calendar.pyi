from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.calendar import Calendar, CalendarEvents
from typing import Dict, List, Optional, Tuple
import inspect
import json
from datetime import datetime, timezone
import httpx

class CalendarHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    
    async def get_calendar(self, as_client: httpx.AsyncClient, calendar_id: str) -> Tuple[bool, Calendar]: ...
    
    async def get_events(self, as_client: httpx.AsyncClient, calendar_id: str, params_template: str = "next_events",
                        time_min: str = datetime.today().replace(tzinfo=timezone.utc).isoformat(), 
                        max_results: int = 250, page_token: str = "") -> Tuple[bool, CalendarEvents]: ...