from typing import Iterable, NamedTuple, Optional
from .color import Color
from .style import Style
from .text import Text

class _AnsiToken(NamedTuple):
    plain: str
    sgr: str
    osc: str

def _ansi_tokenize(ansi_text: str) -> Iterable[_AnsiToken]:
    ...

SGR_STYLE_MAP: dict[int, str]

class AnsiDecoder:
    style: Style

    def __init__(self) -> None:
        ...

    def decode(self, terminal_text: str) -> Iterable[Text]:
        ...

    def decode_line(self, line: str) -> Text:
        ...