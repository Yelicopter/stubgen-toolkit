from . import errors as errors
from .emoji import EmojiVariant as EmojiVariant
from .style import Style as Style, StyleType as StyleType
from .text import Span as Span, Text as Text
from functools import lru_cache as lru_cache
from typing import NamedTuple, Optional, Union

class Tag(NamedTuple):
    name: Optional[str]
    parameters: Optional[str]

def escape(markup: str) -> str: ...
def render(markup: str, style: Union[str, Style] = ..., emoji: bool = ..., emoji_variant: Optional[EmojiVariant] = ...) -> Text: ...
