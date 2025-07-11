from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

import yaml

from pandasai.dataframe import DataFrame
from pandasai.query_builders import BaseQueryBuilder

class DatasetLoader(ABC):
    def __init__(self, schema: Any, dataset_path: str) -> None:
        ...

    @property
    @abstractmethod
    def query_builder(self) -> BaseQueryBuilder:
        ...

    @abstractmethod
    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> Any:
        ...

    @classmethod
    def create_loader_from_schema(
        cls, schema: Any, dataset_path: str
    ) -> "DatasetLoader":
        ...

    @classmethod
    def create_loader_from_path(cls, dataset_path: str) -> "DatasetLoader":
        ...

    @staticmethod
    def _read_schema_file(dataset_path: str) -> Any:
        ...

    def load(self) -> DataFrame:
        ...