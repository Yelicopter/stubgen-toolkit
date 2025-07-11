import abc
from abc import ABC, abstractmethod

class Pager(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def show(self, content: str) -> None: ...

class SystemPager(Pager):
    def show(self, content: str) -> None: ...
