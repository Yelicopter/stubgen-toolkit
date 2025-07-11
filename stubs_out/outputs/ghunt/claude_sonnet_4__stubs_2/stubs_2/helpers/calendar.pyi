import httpx
from copy import deepcopy as deepcopy
from dateutil.relativedelta import relativedelta as relativedelta
from ghunt.apis.calendar import CalendarHttp as CalendarHttp
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.objects.utils import TMPrinter as TMPrinter
from ghunt.parsers.calendar import Calendar as Calendar, CalendarEvents as CalendarEvents
from typing import Optional, Tuple
from xmlrpc.client import Boolean as Boolean

async def fetch_all(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, email_address: str) -> Tuple[bool, Optional[Calendar], Optional[CalendarEvents]]: ...
def out(calendar: Calendar, events: CalendarEvents, email_address: str, display_name: str = ..., limit: int = ...) -> None: ...
