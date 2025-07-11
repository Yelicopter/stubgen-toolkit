from typing import TYPE_CHECKING, Optional, Union

from .segment import Segment
from .style import StyleType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType, RenderResult

class Screen:
    def __init__(
        self,
        *renderables: "RenderableType",
        style: Optional[StyleType] = None,
        application_mode: bool = False
    ) -> None: ...
    
    @property
    def renderable(self) -> "RenderableType": ...
    
    @renderable.setter
    def renderable(self, renderable: "RenderableType") -> None: ...
    
    @property
    def style(self) -> Optional[StyleType]: ...
    
    @style.setter
    def style(self, style: Optional[StyleType]) -> None: ...
    
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...