import abc
from ..constants import LOCAL_SOURCE_TYPES as LOCAL_SOURCE_TYPES
from ..query_builders.base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from .semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema
from abc import ABC, abstractmethod
from pandasai.config import ConfigManager as ConfigManager
from pandasai.dataframe.base import DataFrame as DataFrame
from pandasai.exceptions import MethodNotImplementedError as MethodNotImplementedError
from pandasai.helpers.path import get_validated_dataset_path as get_validated_dataset_path, transform_underscore_to_dash as transform_underscore_to_dash
from typing import Any, Optional

class DatasetLoader(ABC, metaclass=abc.ABCMeta):
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
    @property
    @abstractmethod
    def query_builder(self) -> BaseQueryBuilder: ...
    @abstractmethod
    def execute_query(self, query: str, params: Optional[dict] = ...) -> Any: ...
    @classmethod
    def create_loader_from_schema(cls, schema: SemanticLayerSchema, dataset_path: str) -> DatasetLoader: ...
    @classmethod
    def create_loader_from_path(cls, dataset_path: str) -> DatasetLoader: ...
    def load(self) -> DataFrame: ...
