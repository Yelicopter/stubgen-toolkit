from __future__ import annotations

from abc import ABC
from typing import Any, Type

class RichRenderable(ABC):
    @classmethod
    def __subclasshook__(cls, other: Type[Any]) -> bool: ...