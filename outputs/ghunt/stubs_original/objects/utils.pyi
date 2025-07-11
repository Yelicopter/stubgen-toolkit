from ghunt.helpers.utils import *
from ghunt.errors import *
from typing import *
from ghunt.objects.base import SmartObj as SmartObj

class TMPrinter(SmartObj):
    max_len: int
    def __init__(self) -> None: ...
    def out(self, text: str): ...
    def clear(self) -> None: ...
