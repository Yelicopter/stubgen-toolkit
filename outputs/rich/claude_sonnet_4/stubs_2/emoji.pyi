import sys
from typing import Dict, Optional, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

EmojiVariant = Optional[Literal["emoji", "text"]]

class NoEmoji:
    def __repr__(self) -> str: ...

class Emoji:
    __slots__ = ["name", "style"]
    
    def __init__(self, name: str, style: EmojiVariant = None) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def _repr_mimebundle_(self, include: object, exclude: object) -> Dict[str, str]: ...
    def replace(self, style: EmojiVariant = None) -> Union["Emoji", NoEmoji]: ...