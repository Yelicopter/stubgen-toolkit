from typing import Any, Dict

class SmartObj: ...

class AndroidCreds(SmartObj):
    master_token: str
    authorization_tokens: Dict[str, Any]
    def __init__(self) -> None: ...

class GHuntCreds(SmartObj):
    cookies: Dict[str, Any]
    osids: Dict[str, Any]
    android: AndroidCreds
    creds_path: Any
    def __init__(self, creds_path: Any = ...) -> None: ...
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
    tags: list
    types: list
    cost_level: int
    def __init__(self) -> None: ...

class MapsReview(SmartObj):
    id: str
    comment: str
    rating: int
    location: MapsLocation
    date: Any
    def __init__(self) -> None: ...

class MapsPhoto(SmartObj):
    id: str
    url: str
    location: MapsLocation
    date: Any
    def __init__(self) -> None: ...

class DriveExtractedUser(SmartObj):
    gaia_id: str
    name: str
    email_address: str
    role: str
    is_last_modifying_user: bool
    def __init__(self) -> None: ...
