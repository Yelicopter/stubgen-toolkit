from typing import Any, Dict, Optional

import duckdb
import pandas as pd

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