from abc import ABC
from typing import Any, Optional

class RichRenderable(ABC):
    @classmethod
    def __subclasshook__(cls, other: Any) -> Optional[bool]:
        """Check if this class supports the rich render protocol."""
        return hasattr(other, "__rich_console__") or hasattr(other, "__rich__") or other is cls