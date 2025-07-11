import importlib
from typing import Optional

import pandas as pd

from pandasai.dataframe.virtual_dataframe import VirtualDataFrame
from pandasai.exceptions import InvalidDataSourceType, MaliciousQueryError
from pandasai.helpers.sql_sanitizer import is_sql_query_safe
from pandasai.query_builders import SqlQueryBuilder

from ..constants import SUPPORTED_SOURCE_CONNECTORS
from ..query_builders.sql_parser import SQLParser
from .loader import DatasetLoader
from .semantic_layer_schema import SemanticLayerSchema

class SQLDatasetLoader(DatasetLoader):
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None:
        ...

    @property
    def query_builder(self) -> SqlQueryBuilder:
        ...

    def load(self) -> VirtualDataFrame:
        ...

    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        ...

    @staticmethod
    def _get_loader_function(source_type: str) -> Any:
        ...

    def load_head(self) -> pd.DataFrame:
        ...

    def get_row_count(self) -> int:
        ...