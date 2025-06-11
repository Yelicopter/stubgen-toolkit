from abc import ABC, abstractmethod
from typing import Any

class Pager(ABC):
    @abstractmethod
    def show(self, content: str) -> None: ...

class SystemPager(Pager):
    def _pager(self, content: str) -> Any: ...

    def show(self, content: str) -> None: ...