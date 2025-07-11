from typing import Any, Dict, Optional, Set

import duckdb
import pandas as pd

from pandasai.dataframe import VirtualDataFrame
from pandasai.query_builders import ViewQueryBuilder

class ViewDatasetLoader:
    def __init__(self, schema: Any, dataset_path: str) -> None:
        ...

    @property
    def query_builder(self) -> ViewQueryBuilder:
        ...

    def _get_dependencies_datasets(self) -> Set[str]:
        ...

    def _get_dependencies_schemas(self) -> Dict[str, Any]:
        ...

    def load(self) -> VirtualDataFrame:
        ...

    def execute_local_query(
        self, query: str, params: Optional[Dict[str, Any]] = None
    ) -> pd.DataFrame:
        ...

    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        ...