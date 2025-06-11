from typing import Callable, Match, Optional
import re

_ReStringMatch = Match[str]
_ReSubCallable = Callable[[_ReStringMatch], str]
_EmojiSubMethod = Callable[[_ReSubCallable, str], str]

def _emoji_replace(text: str, default_variant: Optional[str] = None, _emoji_sub: _EmojiSubMethod = re.compile('(:(\\S*?)(?:(?:\\-)(emoji|text))?:)').sub) -> str:
    ...