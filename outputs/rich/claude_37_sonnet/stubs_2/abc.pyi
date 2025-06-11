from abc import ABC
from typing import Any, Type

class RichRenderable(ABC):
    @classmethod
    def __subclasshook__(cls: Type['RichRenderable'], other: Any) -> bool:
        ...