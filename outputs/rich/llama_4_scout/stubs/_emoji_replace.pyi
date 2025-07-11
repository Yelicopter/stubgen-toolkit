from typing import Callable, Match, Optional
import re

from ._emoji_codes import EMOJI


def _emoji_replace(
    text: str,
    default_variant: Optional[str] = None,
    _emoji_sub: Callable[[Callable[[Match[str]], str], str], str] = re.compile(
        r"(:(\S*?)(?:(?:\-)(emoji|text))?:)"
    ).sub,
) -> str:
    ...