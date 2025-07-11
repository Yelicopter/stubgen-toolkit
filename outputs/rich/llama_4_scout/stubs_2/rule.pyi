from typing import Union

from .align import AlignMethod
from .cells import cell_len, set_cell_size
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .style import Style
from .text import Text

class Rule(JupyterMixin):
    """A console renderable to draw a horizontal rule (line).

    Args:
        title (Union[str, Text], optional): Text to render in the rule. Defaults to "".
        characters (str, optional): Character(s) used to draw the line. Defaults to "─".
        style (StyleType, optional): Style of Rule. Defaults to "rule.line".
        end (str, optional): Character at end of Rule. defaults to "\\\\n"
        align (str, optional): How to align the title, one of "left", "center", or "right". Defaults to "center".
    """

    def __init__(
        self,
        title: Union[str, Text] = "",
        *,
        characters: str = "─",
        style: StyleType = "rule.line",
        end: str = "\n",
        align: str = "center",
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        ...

    def _rule_line(self, chars_len: int, width: int) -> Text:
        ...

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        ...