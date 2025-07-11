from typing import Any
from pathlib import Path
import json
from dateutil.relativedelta import relativedelta
from datetime import datetime
import base64

from autoslot import Slots

from ghunt.errors import GHuntInvalidSession

class SmartObj(Slots):
    ...

class AndroidCreds(SmartObj):
    ...

class GHuntCreds(SmartObj):
    ...

    def __init__(self, creds_path: Path = Path("")) -> None:
        ...

    def are_creds_loaded(self) -> bool:
        ...

    def load_creds(self, silent: bool = False) -> None:
        ...

    def save_creds(self, silent: bool = False) -> None:
        ...

### Maps

class Position(SmartObj):
    ...

class MapsLocation(SmartObj):
    ...

class MapsReview(SmartObj):
    ...

class MapsPhoto(SmartObj):
    ...

### Drive

class DriveExtractedUser(SmartObj):
    ...