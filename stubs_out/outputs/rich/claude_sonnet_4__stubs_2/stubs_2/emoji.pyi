from _typeshed import Incomplete
from typing import Union

EmojiVariant: Incomplete

class NoEmoji: ...

class Emoji:
    def __init__(self, name: str, style: EmojiVariant = ...) -> None: ...
    def replace(self, style: EmojiVariant = ...) -> Union['Emoji', NoEmoji]: ...
