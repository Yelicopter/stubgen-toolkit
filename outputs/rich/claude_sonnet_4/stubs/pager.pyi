from abc import ABC, abstractmethod
from typing import Iterable, Optional

class Pager(ABC):
    @abstractmethod
    def show(self, content: str) -> None: ...

class SystemPager(Pager):
    def __init__(self, pager: Optional[str] = None) -> None: ...
    def show(self, content: str) -> None: ...