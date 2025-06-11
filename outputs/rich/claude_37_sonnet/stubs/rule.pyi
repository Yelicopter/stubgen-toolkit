from typing import Union

from .align import AlignMethod
from .cells import cell_len, set_cell_size
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .style import Style
from .text import Text

class Rule(JupyterMixin):
    def __init__(
        self,
        title: Union[str, Text] = ...,
        *,
        characters: str = ...,
        style: Union[str, Style] = ...,
        end: str = ...,
        align: AlignMethod = ...,
    ) -> None: ...
    title: Union[str, Text]
    characters: str
    style: Union[str, Style]
    end: str
    align: AlignMethod
    def __repr__(self) -> str: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def _rule_line(self, chars_len: int, width: int) -> Text: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...