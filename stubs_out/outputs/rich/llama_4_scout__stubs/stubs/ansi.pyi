from .color import Color as Color
from .style import Style as Style
from .text import Text as Text
from _typeshed import Incomplete
from contextlib import suppress as suppress
from typing import Iterable, NamedTuple

re_ansi: Incomplete

class _AnsiToken(NamedTuple):
    plain: str
    sgr: str
    osc: str

SGR_STYLE_MAP: Incomplete

class AnsiDecoder:
    style: Incomplete
    def __init__(self) -> None: ...
    def decode(self, terminal_text: Iterable[str]) -> Iterable[Text]: ...
    def decode_line(self, line: str) -> Text: ...
