from datetime import datetime
from typing import List, Dict

class ConferenceProperties:
    def __init__(self) -> None:
        self.allowed_conference_solution_types: List[str] = []

    def _scrape(self, conference_props_data: Dict) -> None:
        ...

class Calendar:
    def __init__(self) -> None:
        self.id: str = ""
        self.summary: str = ""
        self.time_zone: str = ""
        self.conference_properties: ConferenceProperties = ConferenceProperties()

    def _scrape(self, calendar_data: Dict) -> None:
        ...

class CalendarReminder:
    def __init__(self) -> None:
        self.method: str = ""
        self.minutes: int = 0

    def _scrape(self, reminder_data: Dict) -> None:
        ...

class CalendarPerson:
    def __init__(self) -> None:
        self.email: str = ""
        self.display_name: str = ""
        self.self: bool = None

    def _scrape(self, person_data: Dict) -> None:
        ...

class CalendarTime:
    def __init__(self) -> None:
        self.date_time: datetime = None
        self.time_zone: str = ""

    def _scrape(self, time_data: Dict) -> None:
        ...

class CalendarReminders:
    def __init__(self) -> None:
        self.use_default: int = 0
        self.overrides: List[CalendarReminder] = []

    def _scrape(self, reminders_data: Dict) -> None:
        ...

class CalendarEvent:
    def __init__(self) -> None:
        self.id: str = ""
        self.status: str = ""
        self.html_link: str = ""
        self.created: datetime = None
        self.updated: datetime = None
        self.summary: str = ""
        self.description: str = ""
        self.location: str = ""
        self.creator: CalendarPerson = CalendarPerson()
        self.organizer: CalendarPerson = CalendarPerson()
        self.start: CalendarTime = CalendarTime()
        self.end: CalendarTime = CalendarTime()
        self.recurring_event_id: str = ""
        self.original_start_time: CalendarTime = CalendarTime()
        self.visibility: str = ""
        self.ical_uid: str = ""
        self.sequence: int = 0
        self.guest_can_invite_others: bool = None
        self.reminders: CalendarReminders = CalendarReminders()
        self.event_type: str = ""

    def _scrape(self, event_data: Dict) -> None:
        ...

class CalendarEvents:
    def __init__(self) -> None:
        self.summary: str = ""
        self.updated: datetime = None
        self.time_zone: str = ""
        self.access_role: str = ""
        self.default_reminders: List[CalendarReminder] = []
        self.next_page_token: str = ""
        self.items: List[CalendarEvent] = []

    def _scrape(self, events_data: Dict) -> None:
        ...