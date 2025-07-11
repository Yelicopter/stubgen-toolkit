from abc import ABC
from typing import Any, Optional

class RichRenderable(ABC):
    @classmethod
    def __subclasshook__(cls, other: Any) -> Optional[bool]: ...
