import pandas as pd
from .loader import DatasetLoader as DatasetLoader
from .semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema, Source as Source
from .sql_loader import SQLDatasetLoader as SQLDatasetLoader
from pandasai.dataframe.virtual_dataframe import VirtualDataFrame as VirtualDataFrame
from pandasai.query_builders.view_query_builder import ViewQueryBuilder as ViewQueryBuilder
from typing import Any, Dict, List, Optional, Set

class ViewDatasetLoader(SQLDatasetLoader):
    dependencies_datasets: Set[str]
    schema_dependencies_dict: Dict[str, DatasetLoader]
    source: Source
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
    @property
    def query_builder(self) -> ViewQueryBuilder: ...
    def load(self) -> VirtualDataFrame: ...
    def execute_local_query(self, query: str, params: Optional[List[Any]] = ...) -> pd.DataFrame: ...
    def execute_query(self, query: str, params: Optional[List[Any]] = ...) -> pd.DataFrame: ...
