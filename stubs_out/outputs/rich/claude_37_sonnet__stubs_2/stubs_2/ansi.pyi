from .color import Color as Color
from .style import Style as Style
from .text import Text as Text
from typing import Iterable, NamedTuple

class _AnsiToken(NamedTuple):
    plain: str
    sgr: str
    osc: str

SGR_STYLE_MAP: dict[int, str]

class AnsiDecoder:
    style: Style
    def __init__(self) -> None: ...
    def decode(self, terminal_text: str) -> Iterable[Text]: ...
    def decode_line(self, line: str) -> Text: ...
