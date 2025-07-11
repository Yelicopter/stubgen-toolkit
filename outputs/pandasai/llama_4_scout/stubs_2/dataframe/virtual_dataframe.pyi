from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import pandas as pd

from pandasai.dataframe.base import DataFrame
from pandasai.exceptions import VirtualizationError

if TYPE_CHECKING:
    from pandasai.data_loader.sql_loader import SQLDatasetLoader

class VirtualDataFrame(DataFrame):
    ...

    def __init__(self, *args, **kwargs) -> None:
        ...

    def head(self) -> pd.DataFrame:
        ...

    @property
    def rows_count(self) -> int:
        ...

    @property
    def query_builder(self):
        ...

    def execute_sql_query(self, query: str) -> pd.DataFrame:
        ...