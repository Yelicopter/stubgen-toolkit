from typing import *
from pathlib import Path
import json
from dateutil.relativedelta import relativedelta
from datetime import datetime
import base64
from autoslot import Slots
from ghunt.errors import GHuntInvalidSession

class SmartObj(Slots): ...

class AndroidCreds(SmartObj):
    def __init__(self) -> None: ...
    master_token: str
    authorization_tokens: Dict[str, Dict[str, Any]]

class GHuntCreds(SmartObj):
    def __init__(self, creds_path: str = "") -> None: ...
    cookies: Dict[str, str]
    osids: Dict[str, str]
    android: AndroidCreds
    creds_path: str
    
    def are_creds_loaded(self) -> bool: ...
    def load_creds(self, silent: bool = False) -> None: ...
    def save_creds(self, silent: bool = False) -> None: ...

class Position(SmartObj):
    def __init__(self) -> None: ...
    latitude: float
    longitude: float

class MapsLocation(SmartObj):
    def __init__(self) -> None: ...
    id: str
    name: str
    address: str
    position: Position
    tags: List[str]
    types: List[str]
    cost_level: int

class MapsReview(SmartObj):
    def __init__(self) -> None: ...
    id: str
    comment: str
    rating: int
    location: MapsLocation
    date: Optional[datetime]

class MapsPhoto(SmartObj):
    def __init__(self) -> None: ...
    id: str
    url: str
    location: MapsLocation
    date: Optional[datetime]

class DriveExtractedUser(SmartObj):
    def __init__(self) -> None: ...
    gaia_id: str
    name: str
    email_address: str
    role: str
    is_last_modifying_user: bool