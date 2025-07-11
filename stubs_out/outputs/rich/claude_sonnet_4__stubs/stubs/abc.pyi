from abc import ABC

class RichRenderable(ABC):
    @classmethod
    def __subclasshook__(cls, other: type) -> bool: ...
