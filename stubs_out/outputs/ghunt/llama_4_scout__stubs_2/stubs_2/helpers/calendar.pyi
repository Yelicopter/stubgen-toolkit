from beautifultable import BeautifulTable as BeautifulTable
from copy import deepcopy as deepcopy
from dateutil.relativedelta import relativedelta as relativedelta
from ghunt.apis.calendar import CalendarHttp as CalendarHttp
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.objects.utils import TMPrinter as TMPrinter
from ghunt.parsers.calendar import Calendar as Calendar, CalendarEvents as CalendarEvents
from typing import Any
from xmlrpc.client import Boolean as Boolean

async def fetch_all(ghunt_creds: GHuntCreds, as_client: Any, email_address: str) -> tuple[bool, Calendar, CalendarEvents]: ...
def out(calendar: Calendar, events: CalendarEvents, email_address: str, display_name: str = ..., limit: int = ...) -> None: ...
