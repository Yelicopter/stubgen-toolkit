import re
from functools import lru_cache
from typing import Dict, Iterable, List, Match, NamedTuple, Optional, Tuple, Union

from . import errors
from ._emoji_replace import _emoji_replace
from .emoji import EmojiVariant
from .style import Style, StyleType
from .text import Span, Text

class Tag(NamedTuple):
    name: Optional[str]
    parameters: Optional[str]

def escape(markup: str) -> str: ...
def render(
    markup: str,
    style: Union[str, Style] = "",
    emoji: bool = True,
    emoji_variant: Optional[EmojiVariant] = None
) -> Text: ...