from typing import Any, List, Optional
from ghunt.objects.apis import Parser

class ConferenceProperties(Parser):
    allowed_conference_solution_types: List[Any]
    def __init__(self) -> None: ...
    def _scrape(self, conference_props_data: Any) -> None: ...

class Calendar(Parser):
    id: str
    summary: str
    time_zone: str
    conference_properties: ConferenceProperties
    def __init__(self) -> None: ...
    def _scrape(self, calendar_data: Any) -> None: ...

class CalendarReminder(Parser):
    method: str
    minutes: int
    def __init__(self) -> None: ...
    def _scrape(self, reminder_data: Any) -> None: ...

class CalendarPerson(Parser):
    email: str
    display_name: str
    self: Any
    def __init__(self) -> None: ...
    def _scrape(self, person_data: Any) -> None: ...

class CalendarTime(Parser):
    date_time: Optional[Any]
    time_zone: str
    def __init__(self) -> None: ...
    def _scrape(self, time_data: Any) -> None: ...

class CalendarReminders(Parser):
    use_default: int
    overrides: List[CalendarReminder]
    def __init__(self) -> None: ...
    def _scrape(self, reminders_data: Any) -> None: ...

class CalendarEvent(Parser):
    id: str
    status: str
    html_link: str
    created: Any
    updated: Any
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
    guest_can_invite_others: Any
    reminders: CalendarReminders
    event_type: str
    def __init__(self) -> None: ...
    def _scrape(self, event_data: Any) -> None: ...

class CalendarEvents(Parser):
    summary: str
    updated: Any
    time_zone: str
    access_role: str
    default_reminders: List[CalendarReminder]
    next_page_token: str
    items: List[CalendarEvent]
    def __init__(self) -> None: ...
    def _scrape(self, events_data: Any) -> None: ...