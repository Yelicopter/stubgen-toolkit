import sys
from typing import TYPE_CHECKING, Optional, Union

from .jupyter import JupyterMixin
from .segment import Segment
from .style import Style
from ._emoji_codes import EMOJI
from ._emoji_replace import _emoji_replace

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal  # pragma: no cover


if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult


EmojiVariant = Literal["emoji", "text"]


class NoEmoji(Exception):
    ...


class Emoji(JupyterMixin):
    def __init__(self, name: str, style: Union[str, Style] = "none", variant: Optional[EmojiVariant] = None) -> None:
        ...

    @classmethod
    def replace(cls, text: str) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def __rich_console__(self, console: 'Console', options: 'ConsoleOptions') -> 'RenderResult':
        ...