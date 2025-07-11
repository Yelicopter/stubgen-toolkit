from _typeshed import Incomplete

class ConferenceProperties:
    allowed_conference_solution_types: Incomplete
    def __init__(self) -> None: ...

class Calendar:
    id: str
    summary: str
    time_zone: str
    conference_properties: Incomplete
    def __init__(self) -> None: ...

class CalendarReminder:
    method: str
    minutes: int
    def __init__(self) -> None: ...

class CalendarPerson:
    email: str
    display_name: str
    self: Incomplete
    def __init__(self) -> None: ...

class CalendarTime:
    date_time: Incomplete
    time_zone: str
    def __init__(self) -> None: ...

class CalendarReminders:
    use_default: int
    overrides: Incomplete
    def __init__(self) -> None: ...

class CalendarEvent:
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

class CalendarEvents:
    summary: str
    updated: Incomplete
    time_zone: str
    access_role: str
    default_reminders: Incomplete
    next_page_token: str
    items: Incomplete
    def __init__(self) -> None: ...
