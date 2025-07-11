import re
from typing import Any, Dict, Optional

import duckdb
import pandas as pd

from pandasai.dataframe import DataFrame
from pandasai.exceptions import MaliciousQueryError
from pandasai.query_builders import LocalQueryBuilder

class LocalDatasetLoader:
    def __init__(self, schema: Any, dataset_path: str) -> None:
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