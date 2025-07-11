from typing import *
from pathlib import Path
import json
from dateutil.relativedelta import relativedelta
from datetime import datetime
import base64
from autoslot import Slots
from ghunt.errors import GHuntInvalidSession

class SmartObj(Slots):
    pass

class AndroidCreds(SmartObj):
    master_token: str
    authorization_tokens: Dict[str, Dict[str, Any]]
    def __init__(self) -> None: ...

class GHuntCreds(SmartObj):
    cookies: Dict[str, str]
    osids: Dict[str, str]
    android: AndroidCreds
    creds_path: str
    
    def __init__(self, creds_path: str = "") -> None: ...
    def are_creds_loaded(self) -> bool: ...
    def load_creds(self, silent: bool = False) -> None: ...
    def save_creds(self, silent: bool = False) -> None: ...

class Position(SmartObj):
    latitude: float
    longitude: float
    def __init__(self) -> None: ...

class MapsLocation(SmartObj):
    id: str
    name: str
    address: str
    position: Position
    tags: List[str]
    types: List[str]
    cost_level: int
    def __init__(self) -> None: ...

class MapsReview(SmartObj):
    id: str
    comment: str
    rating: int
    location: MapsLocation
    date: Optional[datetime]
    def __init__(self) -> None: ...

class MapsPhoto(SmartObj):
    id: str
    url: str
    location: MapsLocation
    date: Optional[datetime]
    def __init__(self) -> None: ...

class DriveExtractedUser(SmartObj):
    gaia_id: str
    name: str
    email_address: str
    role: str
    is_last_modifying_user: bool
    def __init__(self) -> None: ...