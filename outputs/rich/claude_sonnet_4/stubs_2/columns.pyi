from typing import TYPE_CHECKING, Iterable, List, Optional, Tuple, Union

from .console import RenderableType
from .constrain import Constrain
from .jupyter import JupyterMixin
from .measure import Measurement

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult

class Columns(JupyterMixin):
    def __init__(
        self,
        renderables: Optional[Iterable[RenderableType]] = None,
        width: Optional[int] = None,
        *,
        padding: Union[int, Tuple[int, int]] = (0, 1),
        expand: bool = False,
        equal: bool = False,
        column_first: bool = False,
        right_to_left: bool = False,
        align: str = "left",
        title: Optional[RenderableType] = None
    ) -> None: ...
    
    def add_renderable(self, renderable: RenderableType) -> None: ...
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...
    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> Measurement: ...