from abc import ABC
from typing import Any

class RichRenderable(ABC):
    @classmethod
    def __subclasshook__(cls, other: Any) -> bool: ...
