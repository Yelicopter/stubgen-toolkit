from xmlrpc.client import Boolean
from dateutil.relativedelta import relativedelta
import httpx
from typing import Dict, List, Optional, Tuple
from copy import deepcopy
from ghunt.parsers.calendar import Calendar, CalendarEvents
from ghunt.objects.base import GHuntCreds
from ghunt.objects.utils import TMPrinter
from ghunt.apis.calendar import CalendarHttp

async def fetch_all(ghunt_creds: GHuntCreds, as_client: httpx.AsyncClient, email_address: str) -> Tuple[bool, Optional[Calendar], Optional[CalendarEvents]]: ...
def out(calendar: Calendar, events: CalendarEvents, email_address: str, display_name: str = "", limit: int = 5) -> None: ...