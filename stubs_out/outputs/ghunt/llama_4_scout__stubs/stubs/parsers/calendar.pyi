from _typeshed import Incomplete
from ghunt.helpers.utils import get_datetime_utc as get_datetime_utc
from ghunt.objects.apis import Parser

class ConferenceProperties(Parser):
    allowed_conference_solution_types: Incomplete
    def __init__(self) -> None: ...

class Calendar(Parser):
    id: str
    summary: str
    time_zone: str
    conference_properties: Incomplete
    def __init__(self) -> None: ...

class CalendarReminder(Parser):
    method: str
    minutes: int
    def __init__(self) -> None: ...

class CalendarPerson(Parser):
    email: str
    display_name: str
    self: Incomplete
    def __init__(self) -> None: ...

class CalendarTime(Parser):
    date_time: Incomplete
    time_zone: str
    def __init__(self) -> None: ...

class CalendarReminders(Parser):
    use_default: int
    overrides: Incomplete
    def __init__(self) -> None: ...

class CalendarEvent(Parser):
    id: str
    status: str
    html_link: str
    created: Incomplete
    updated: Incomplete
    summary: str
    description: str
    location: str
    creator: Incomplete
    organizer: Incomplete
    start: Incomplete
    end: Incomplete
    recurring_event_id: str
    original_start_time: Incomplete
    visibility: str
    ical_uid: str
    sequence: int
    guest_can_invite_others: Incomplete
    reminders: Incomplete
    event_type: str
    def __init__(self) -> None: ...

class CalendarEvents(Parser):
    summary: str
    updated: Incomplete
    time_zone: str
    access_role: str
    default_reminders: Incomplete
    next_page_token: str
    items: Incomplete
    def __init__(self) -> None: ...
