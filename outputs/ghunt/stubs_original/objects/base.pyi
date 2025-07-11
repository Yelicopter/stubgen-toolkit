from typing import *
from _typeshed import Incomplete
from autoslot import Slots
from dateutil.relativedelta import relativedelta as relativedelta
from ghunt.errors import GHuntInvalidSession as GHuntInvalidSession

class SmartObj(Slots): ...

class AndroidCreds(SmartObj):
    master_token: str
    authorization_tokens: Incomplete
    def __init__(self) -> None: ...

class GHuntCreds(SmartObj):
    cookies: Incomplete
    osids: Incomplete
    android: Incomplete
    creds_path: Incomplete
    def __init__(self, creds_path: str = ...) -> None: ...
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
    position: Incomplete
    tags: Incomplete
    types: Incomplete
    cost_level: int
    def __init__(self) -> None: ...

class MapsReview(SmartObj):
    id: str
    comment: str
    rating: int
    location: Incomplete
    date: Incomplete
    def __init__(self) -> None: ...

class MapsPhoto(SmartObj):
    id: str
    url: str
    location: Incomplete
    date: Incomplete
    def __init__(self) -> None: ...

class DriveExtractedUser(SmartObj):
    gaia_id: str
    name: str
    email_address: str
    role: str
    is_last_modifying_user: bool
    def __init__(self) -> None: ...
