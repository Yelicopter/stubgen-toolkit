from typing import TYPE_CHECKING, List, Optional, Tuple, Union

if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        RenderableType,
        RenderResult,
    )

from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style


class Padding(JupyterMixin):
    ...