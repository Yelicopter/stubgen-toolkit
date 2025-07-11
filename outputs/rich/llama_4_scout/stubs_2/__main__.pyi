import colorsys
import io
from time import process_time

from rich import box
from rich.color import Color
from rich.console import Console, ConsoleOptions, Group, RenderableType, RenderResult
from rich.markdown import Markdown
from rich.measure import Measurement
from rich.pretty import Pretty
from rich.segment import Segment
from rich.style import Style
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text


class ColorBox:
    def __rich_console__(
        self, console: "Console", options: ConsoleOptions
    ) -> Iterable[Segment]:
        ...

    def __rich_measure__(
        self, console: "Console", options: ConsoleOptions
    ) -> Measurement:
        ...


def make_test_card() -> Table:
    """Get a renderable that demonstrates a number of features."""
    ...