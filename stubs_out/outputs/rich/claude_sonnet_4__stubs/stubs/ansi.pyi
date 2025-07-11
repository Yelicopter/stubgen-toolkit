from .style import Style as Style
from .text import Text as Text
from typing import Iterable

class AnsiDecoder:
    def __init__(self) -> None: ...
    def decode(self, data: str) -> Iterable[Text]: ...
