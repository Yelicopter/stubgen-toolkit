from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style

class Padding(JupyterMixin):
    def __init__(self, renderable: RenderableType, *, padding: PaddingDimensions = ...) -> None: ...
