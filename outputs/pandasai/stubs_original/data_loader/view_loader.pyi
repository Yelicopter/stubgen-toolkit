import pandas as pd
from .. import LOCAL_SOURCE_TYPES as LOCAL_SOURCE_TYPES
from ..exceptions import MaliciousQueryError as MaliciousQueryError
from ..helpers.sql_sanitizer import is_sql_query_safe as is_sql_query_safe
from ..query_builders.base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from ..query_builders.sql_parser import SQLParser as SQLParser
from .duck_db_connection_manager import DuckDBConnectionManager as DuckDBConnectionManager
from .loader import DatasetLoader as DatasetLoader
from .local_loader import LocalDatasetLoader as LocalDatasetLoader
from .semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema, Source as Source
from .sql_loader import SQLDatasetLoader as SQLDatasetLoader
from _typeshed import Incomplete
from pandasai.dataframe.virtual_dataframe import VirtualDataFrame as VirtualDataFrame
from pandasai.query_builders import ViewQueryBuilder as ViewQueryBuilder
from typing import Any, List, Optional

class ViewDatasetLoader(SQLDatasetLoader):
    dependencies_datasets: Incomplete
    schema_dependencies_dict: Incomplete
    source: Incomplete
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
    @property
    def query_builder(self) -> ViewQueryBuilder: ...
    def load(self) -> VirtualDataFrame: ...
    def execute_local_query(self, query: str, params: Optional[List[Any]] = ...) -> pd.DataFrame: ...
    def execute_query(self, query: str, params: Optional[list] = ...) -> pd.DataFrame: ...
