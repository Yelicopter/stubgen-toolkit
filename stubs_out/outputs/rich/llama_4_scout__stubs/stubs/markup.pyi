from .emoji import EmojiVariant as EmojiVariant
from .errors import MarkupError as MarkupError
from .style import Style as Style
from .text import Span as Span, Text as Text
from ast import literal_eval as literal_eval
from operator import attrgetter as attrgetter
from typing import NamedTuple, Optional

class Tag(NamedTuple): ...

def escape(markup: str) -> str: ...
def render(markup: str, style: str = ..., emoji: bool = ..., emoji_variant: Optional[EmojiVariant] = ...) -> Text: ...
