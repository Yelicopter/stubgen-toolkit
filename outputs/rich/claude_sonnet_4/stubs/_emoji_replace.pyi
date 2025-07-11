from typing import Optional
from .emoji import EmojiVariant

def _emoji_replace(
    text: str,
    default_variant: Optional[EmojiVariant] = None,
    _emoji_sub: Optional[object] = None
) -> str: ...