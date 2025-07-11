from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from datetime import datetime
from autoslot import Slots  # type: ignore

class SmartObj(Slots): ...

class AndroidCreds(SmartObj):
    master_token: str
    authorization_tokens: Dict[str, Dict[str, Any]]
    def __init__(self) -> None: ...

class GHuntCreds(SmartObj):
    cookies: Dict[str, str]
    osids: Dict[str, str]
    android: AndroidCreds
    creds_path: Path
    def __init__(self, creds_path: Union[str, Path] = ...) -> None: ...
    def are_creds_loaded(self) -> bool: ...
    def load_creds(self, silent: bool = ...) -> None: ...
    def save_creds(self, silent: bool = ...) -> None: ...

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