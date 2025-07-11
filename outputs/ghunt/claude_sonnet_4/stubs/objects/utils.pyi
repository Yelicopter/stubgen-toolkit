from ghunt.helpers.utils import *
from ghunt.errors import *
from ghunt.objects.base import SmartObj
from typing import *

class TMPrinter(SmartObj):
    def __init__(self) -> None: ...
    max_len: int
    
    def out(self, text: str) -> None: ...
    def clear(self) -> None: ...