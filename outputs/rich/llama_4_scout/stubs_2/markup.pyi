import re
from ast import literal_eval
from operator import attrgetter
from typing import Callable, Iterable, List, Match, NamedTuple, Optional, Tuple, Union

from ._emoji_replace import _emoji_replace
from .emoji import EmojiVariant
from .errors import MarkupError
from .style import Style
from .text import Span, Text


class Tag(NamedTuple):
    ...

def escape(
    markup: str,
) -> str:
    ...

def render(
    markup: str,
    style: str = "",
    emoji: bool = True,
    emoji_variant: Optional[EmojiVariant] = None,
) -> Text:
    ...