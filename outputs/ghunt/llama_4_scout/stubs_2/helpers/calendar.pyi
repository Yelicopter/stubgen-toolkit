from xmlrpc.client import Boolean
from dateutil.relativedelta import relativedelta
from beautifultable import BeautifulTable
import httpx

from typing import Any
from copy import deepcopy

from ghunt.parsers.calendar import Calendar, CalendarEvents
from ghunt.objects.base import GHuntCreds
from ghunt.objects.utils import TMPrinter
from ghunt.apis.calendar import CalendarHttp

async def fetch_all(ghunt_creds: GHuntCreds, as_client: Any, email_address: str) -> tuple[bool, Calendar, CalendarEvents]:
    ...

def out(calendar: Calendar, events: CalendarEvents, email_address: str, display_name: str = "", limit: int = 5) -> None:
    ...