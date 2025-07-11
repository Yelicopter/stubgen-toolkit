import httpx
from ghunt.parsers.calendar import Calendar, CalendarEvents
from ghunt.objects.base import GHuntCreds
from typing import Tuple, Optional

async def fetch_all(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, email_address: str) -> Tuple[bool, Optional[Calendar], Optional[CalendarEvents]]: ...
def out(calendar: Calendar, events: CalendarEvents, email_address: str, display_name: str = ..., limit: int = ...) -> None: ...