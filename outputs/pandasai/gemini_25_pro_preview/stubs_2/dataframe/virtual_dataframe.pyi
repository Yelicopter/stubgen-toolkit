from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import pandas as pd

from pandasai.dataframe.base import DataFrame
from pandasai.query_builders.base_query_builder import BaseQueryBuilder

if TYPE_CHECKING:
    from pandasai.data_loader.sql_loader import SQLDatasetLoader

class VirtualDataFrame(DataFrame):
    _metadata: list[str]
    _loader: SQLDatasetLoader
    _head: Optional[pd.DataFrame]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def head(self, n: int = 5) -> pd.DataFrame: ...
    @property
    def rows_count(self) -> int: ...
    @property
    def query_builder(self) -> BaseQueryBuilder: ...
    def execute_sql_query(self, query: str) -> pd.DataFrame: ...