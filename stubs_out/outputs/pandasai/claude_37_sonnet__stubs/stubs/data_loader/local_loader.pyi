import pandas as pd
from ..helpers.sql_sanitizer import is_sql_query_safe as is_sql_query_safe
from .duck_db_connection_manager import DuckDBConnectionManager as DuckDBConnectionManager
from .loader import DatasetLoader as DatasetLoader
from .semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema
from pandasai.dataframe.base import DataFrame
from pandasai.exceptions import MaliciousQueryError as MaliciousQueryError
from pandasai.query_builders import LocalQueryBuilder as LocalQueryBuilder
from typing import Any, Dict, Optional

class LocalDatasetLoader(DatasetLoader):
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
    @property
    def query_builder(self) -> LocalQueryBuilder: ...
    def register_table(self) -> None: ...
    def load(self) -> DataFrame: ...
    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = ...) -> pd.DataFrame: ...
