from typing import TYPE_CHECKING, Optional, Union

from . import box
from .align import AlignMethod
from .jupyter import JupyterMixin
from .measure import Measurement
from .padding import PaddingDimensions
from .segment import Segment
from .style import StyleType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType, RenderResult

class Panel(JupyterMixin):
    def __init__(
        self,
        renderable: "RenderableType",
        box: box.Box = box.ROUNDED,
        *,
        safe_box: Optional[bool] = None,
        expand: bool = True,
        style: StyleType = "none",
        border_style: StyleType = "none",
        width: Optional[int] = None,
        height: Optional[int] = None,
        padding: PaddingDimensions = (0, 1),
        highlight: bool = False,
        title: Optional["RenderableType"] = None,
        title_align: AlignMethod = "center",
        subtitle: Optional["RenderableType"] = None,
        subtitle_align: AlignMethod = "center"
    ) -> None: ...
    
    @classmethod
    def fit(
        cls,
        renderable: "RenderableType",
        box: box.Box = box.ROUNDED,
        *,
        safe_box: Optional[bool] = None,
        style: StyleType = "none",
        border_style: StyleType = "none",
        width: Optional[int] = None,
        padding: PaddingDimensions = (0, 1),
        title: Optional["RenderableType"] = None,
        title_align: AlignMethod = "center",
        subtitle: Optional["RenderableType"] = None,
        subtitle_align: AlignMethod = "center"
    ) -> "Panel": ...
    
    @property
    def _title(self) -> Optional["RenderableType"]: ...
    
    @_title.setter
    def _title(self, title: Optional["RenderableType"]) -> None: ...
    
    @property
    def _subtitle(self) -> Optional["RenderableType"]: ...
    
    @_subtitle.setter
    def _subtitle(self, subtitle: Optional["RenderableType"]) -> None: ...
    
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...
    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> Measurement: ...