from typing import Optional, Tuple

from .console import Console, ConsoleOptions, RenderableType, RenderResult
from .control import Control
from .segment import ControlType, Segment
from .style import StyleType
from .text import Text


VerticalOverflowMethod = Literal["crop", "ellipsis", "visible"]


class LiveRender:
    ...