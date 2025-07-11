from typing import Optional, Any
from abc import ABC, abstractmethod

class DatasetLoader(ABC):
    schema: Any
    org_name: str
    dataset_name: str
    dataset_path: str

    def __init__(self, schema: Any, dataset_path: str): ...
    @property
    @abstractmethod
    def query_builder(self) -> Any: ...
    @abstractmethod
    def execute_query(self, query: str, params: Optional[Any] = ...) -> Any: ...
    @classmethod
    def create_loader_from_schema(
        cls, schema: Any, dataset_path: str
    ) -> "DatasetLoader": ...
    @classmethod
    def create_loader_from_path(cls, dataset_path: str) -> "DatasetLoader": ...
    @staticmethod
    def _read_schema_file(dataset_path: str) -> Any: ...
    def load(self) -> Any: ...