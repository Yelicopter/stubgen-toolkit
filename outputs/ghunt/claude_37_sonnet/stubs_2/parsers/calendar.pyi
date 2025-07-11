from datetime import datetime
from typing import *
from ghunt.helpers.utils import get_datetime_utc
from ghunt.objects.apis import Parser

class ConferenceProperties(Parser):
    allowed_conference_solution_types: List[str]
    def __init__(self) -> None: ...
    def _scrape(self, conference_props_data: Dict[str, Any]) -> None: ...

class Calendar(Parser):
    id: str
    summary: str
    time_zone: str
    conference_properties: ConferenceProperties
    def __init__(self) -> None: ...
    def _scrape(self, calendar_data: Dict[str, Any]) -> None: ...

class CalendarReminder(Parser):
    method: str
    minutes: int
    def __init__(self) -> None: ...
    def _scrape(self, reminder_data: Dict[str, Any]) -> None: ...

class CalendarPerson(Parser):
    email: str
    display_name: str
    self: Optional[bool]
    def __init__(self) -> None: ...
    def _scrape(self, person_data: Dict[str, Any]) -> None: ...

class CalendarTime(Parser):
    date_time: Optional[datetime]
    time_zone: str
    def __init__(self) -> None: ...
    def _scrape(self, time_data: Dict[str, Any]) -> None: ...

class CalendarReminders(Parser):
    use_default: int
    overrides: List[CalendarReminder]
    def __init__(self) -> None: ...
    def _scrape(self, reminders_data: Dict[str, Any]) -> None: ...

class CalendarEvent(Parser):
    id: str
    status: str
    html_link: str
    created: Union[str, datetime, None]
    updated: Union[str, datetime, None]
    summary: str
    description: str
    location: str
    creator: CalendarPerson
    organizer: CalendarPerson
    start: CalendarTime
    end: CalendarTime
    recurring_event_id: str
    original_start_time: CalendarTime
    visibility: str
    ical_uid: str
    sequence: int
    guest_can_invite_others: Optional[bool]
    reminders: CalendarReminders
    event_type: str
    def __init__(self) -> None: ...
    def _scrape(self, event_data: Dict[str, Any]) -> None: ...

class CalendarEvents(Parser):
    summary: str
    updated: Union[str, datetime, None]
    time_zone: str
    access_role: str
    default_reminders: List[CalendarReminder]
    next_page_token: str
    items: List[CalendarEvent]
    def __init__(self) -> None: ...
    def _scrape(self, events_data: Dict[str, Any]) -> None: ...