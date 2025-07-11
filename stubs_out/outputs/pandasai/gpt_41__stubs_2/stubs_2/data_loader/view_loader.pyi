import abc
from .sql_loader import SQLDatasetLoader as SQLDatasetLoader
from typing import Any

class ViewDatasetLoader(SQLDatasetLoader, metaclass=abc.ABCMeta):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def load(self) -> Any: ...
