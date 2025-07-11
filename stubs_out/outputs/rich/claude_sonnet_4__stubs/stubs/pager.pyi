import abc
from abc import ABC, abstractmethod
from typing import Optional

class Pager(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def show(self, content: str) -> None: ...

class SystemPager(Pager):
    def __init__(self, pager: Optional[str] = ...) -> None: ...
    def show(self, content: str) -> None: ...
