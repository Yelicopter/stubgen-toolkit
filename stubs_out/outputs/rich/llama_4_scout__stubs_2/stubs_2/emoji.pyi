from ._emoji_codes import EMOJI as EMOJI
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .segment import Segment as Segment
from .style import Style as Style
from _typeshed import Incomplete
from typing import Optional, Union

EmojiVariant: Incomplete

class NoEmoji(Exception): ...

class Emoji(JupyterMixin):
    def __init__(self, name: str, style: Union[str, Style] = ..., variant: Optional[EmojiVariant] = ...) -> None: ...
    @classmethod
    def replace(cls, text: str) -> str: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
