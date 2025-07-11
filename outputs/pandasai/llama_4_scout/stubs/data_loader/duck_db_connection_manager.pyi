from typing import Optional

import duckdb

from pandasai.query_builders.sql_parser import SQLParser

class DuckDBConnectionManager:
    def __init__(self) -> None:
        ...

    def __del__(self) -> None:
        ...

    def register(self, name: str, df: pd.DataFrame) -> None:
        ...

    def unregister(self, name: str) -> None:
        ...

    def sql(self, query: str, params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        ...

    def close(self) -> None:
        ...