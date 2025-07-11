from ._loop import loop_last as loop_last
from ._pick import pick_bool as pick_bool
from ._wrap import divide_line as divide_line
from .align import AlignMethod as AlignMethod
from .cells import cell_len as cell_len, set_cell_size as set_cell_size
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod
from .containers import Lines as Lines
from .control import strip_control_codes as strip_control_codes
from .emoji import EmojiVariant as EmojiVariant
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from _typeshed import Incomplete
from functools import partial as partial, reduce as reduce
from math import gcd as gcd
from operator import itemgetter as itemgetter
from typing import Callable, NamedTuple, Optional

DEFAULT_JUSTIFY: str
DEFAULT_OVERFLOW: str
TextType: Incomplete
GetStyleCallable = Callable[[str], Optional[StyleType]]

class Span(NamedTuple): ...
class Text(JupyterMixin): ...
