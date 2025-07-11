import os
from abc import ABC, abstractmethod
from typing import Optional

import yaml

from pandasai.dataframe.base import DataFrame
from pandasai.exceptions import MethodNotImplementedError
from pandasai.helpers.path import (
    get_validated_dataset_path,
    transform_underscore_to_dash,
)

from .. import ConfigManager
from ..constants import LOCAL_SOURCE_TYPES
from ..query_builders.base_query_builder import BaseQueryBuilder
from .semantic_layer_schema import SemanticLayerSchema

class DatasetLoader(ABC):
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None:
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
        cls, schema: SemanticLayerSchema, dataset_path: str
    ) -> "DatasetLoader":
        ...

    @classmethod
    def create_loader_from_path(cls, dataset_path: str) -> "DatasetLoader":
        ...

    @staticmethod
    def _read_schema_file(dataset_path: str) -> SemanticLayerSchema:
        ...

    def load(self) -> DataFrame:
        ...