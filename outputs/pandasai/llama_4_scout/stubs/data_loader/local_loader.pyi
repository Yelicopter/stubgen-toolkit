import re
from typing import Optional

import duckdb
import pandas as pd

from pandasai.dataframe.base import DataFrame
from pandasai.exceptions import MaliciousQueryError
from pandasai.query_builders import LocalQueryBuilder

from ..helpers.sql_sanitizer import is_sql_query_safe
from .duck_db_connection_manager import DuckDBConnectionManager
from .loader import DatasetLoader
from .semantic_layer_schema import SemanticLayerSchema

class LocalDatasetLoader(DatasetLoader):
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None:
        ...

    @property
    def query_builder(self) -> LocalQueryBuilder:
        ...

    def register_table(self) -> None:
        ...

    def load(self) -> DataFrame:
        ...

    def _replace_readparquet_block_with_table(
        self, sql_query: str, table: str = "dummy_table"
    ) -> str:
        ...

    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        ...