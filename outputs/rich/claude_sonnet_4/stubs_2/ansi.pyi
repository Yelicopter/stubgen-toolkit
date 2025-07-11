from typing import Iterable, List, NamedTuple, Optional, Tuple
from .style import Style
from .text import Text

class AnsiDecoder:
    def __init__(self) -> None: ...
    def decode(self, data: str) -> Iterable[Text]: ...