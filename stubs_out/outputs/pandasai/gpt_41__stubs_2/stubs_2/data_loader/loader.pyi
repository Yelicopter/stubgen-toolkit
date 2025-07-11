import abc
from abc import ABC, abstractmethod
from typing import Any, Optional

class DatasetLoader(ABC, metaclass=abc.ABCMeta):
    schema: Any
    org_name: str
    dataset_name: str
    dataset_path: str
    def __init__(self, schema: Any, dataset_path: str) -> None: ...
    @property
    @abstractmethod
    def query_builder(self) -> Any: ...
    @abstractmethod
    def execute_query(self, query: str, params: Optional[Any] = ...) -> Any: ...
    @classmethod
    def create_loader_from_schema(cls, schema: Any, dataset_path: str) -> DatasetLoader: ...
    @classmethod
    def create_loader_from_path(cls, dataset_path: str) -> DatasetLoader: ...
    def load(self) -> Any: ...
