from datetime import datetime
from typing import *
from ghunt.helpers.utils import get_datetime_utc
from ghunt.objects.apis import Parser

class ConferenceProperties(Parser):
    def __init__(self) -> None: ...
    allowed_conference_solution_types: List[str]
    
    def _scrape(self, conference_props_data: Dict[str, Any]) -> None: ...

class Calendar(Parser):
    def __init__(self) -> None: ...
    id: str
    summary: str
    time_zone: str
    conference_properties: ConferenceProperties
    
    def _scrape(self, calendar_data: Dict[str, Any]) -> None: ...

class CalendarReminder(Parser):
    def __init__(self) -> None: ...
    method: str
    minutes: int
    
    def _scrape(self, reminder_data: Dict[str, Any]) -> None: ...

class CalendarPerson(Parser):
    def __init__(self) -> None: ...
    email: str
    display_name: str
    self: Optional[bool]
    
    def _scrape(self, person_data: Dict[str, Any]) -> None: ...

class CalendarTime(Parser):
    def __init__(self) -> None: ...
    date_time: Optional[datetime]
    time_zone: str
    
    def _scrape(self, time_data: Dict[str, Any]) -> None: ...

class CalendarReminders(Parser):
    def __init__(self) -> None: ...
    use_default: int
    overrides: List[CalendarReminder]
    
    def _scrape(self, reminders_data: Dict[str, Any]) -> None: ...

class CalendarEvent(Parser):
    def __init__(self) -> None: ...
    id: str
    status: str
    html_link: str
    created: str
    updated: str
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
    
    def _scrape(self, event_data: Dict[str, Any]) -> None: ...

class CalendarEvents(Parser):
    def __init__(self) -> None: ...
    summary: str
    updated: str
    time_zone: str
    access_role: str
    default_reminders: List[CalendarReminder]
    next_page_token: str
    items: List[CalendarEvent]
    
    def _scrape(self, events_data: Dict[str, Any]) -> None: ...