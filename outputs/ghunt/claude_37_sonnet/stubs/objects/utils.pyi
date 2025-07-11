from ghunt.helpers.utils import *
from ghunt.errors import *
from ghunt.objects.base import SmartObj
from typing import *

class TMPrinter(SmartObj):
    max_len: int
    def __init__(self) -> None: ...
    def out(self, text: str) -> None: ...
    def clear(self) -> None: ...