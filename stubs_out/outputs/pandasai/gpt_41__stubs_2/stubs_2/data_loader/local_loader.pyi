import abc
from .loader import DatasetLoader as DatasetLoader
from typing import Any

class LocalDatasetLoader(DatasetLoader, metaclass=abc.ABCMeta):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def load(self) -> Any: ...
