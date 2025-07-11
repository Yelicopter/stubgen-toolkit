from .emoji import EmojiVariant as EmojiVariant
from .errors import MarkupError as MarkupError
from .style import Style as Style
from .text import Span as Span, Text as Text
from ast import literal_eval as literal_eval
from operator import attrgetter as attrgetter
from typing import NamedTuple, Optional, Pattern, Union

RE_TAGS: Pattern[str]
RE_HANDLER: Pattern[str]

class Tag(NamedTuple):
    name: str
    parameters: Optional[str]
    @property
    def markup(self) -> str: ...

def escape(markup: str, _escape: _EscapeSubMethod = ...) -> str: ...
def render(markup: str, style: Union[str, Style] = ..., emoji: bool = ..., emoji_variant: Optional[EmojiVariant] = ...) -> Text: ...
