import abc
from .semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema
from abc import ABC, abstractmethod
from pandasai.dataframe.base import DataFrame as DataFrame
from pandasai.query_builders.base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from typing import Any, List, Optional

class DatasetLoader(ABC, metaclass=abc.ABCMeta):
    schema: SemanticLayerSchema
    org_name: str
    dataset_name: str
    dataset_path: str
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
    @property
    @abstractmethod
    def query_builder(self) -> BaseQueryBuilder: ...
    @abstractmethod
    def execute_query(self, query: str, params: Optional[List[Any]] = ...) -> Any: ...
    @classmethod
    def create_loader_from_schema(cls, schema: SemanticLayerSchema, dataset_path: str) -> DatasetLoader: ...
    @classmethod
    def create_loader_from_path(cls, dataset_path: str) -> DatasetLoader: ...
    def load(self) -> DataFrame: ...
