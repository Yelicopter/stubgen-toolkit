from typing import Any, Dict, Optional, Set

import duckdb

from pandasai.query_builders.sql_parser import SQLParser

class DuckDBConnectionManager:
    connection: duckdb.DuckDBPyConnection
    _registered_tables: Set[str]
    
    def __init__(self) -> None: ...
    
    def __del__(self) -> None: ...
    
    def register(self, name: str, df) -> None: ...
    
    def unregister(self, name: str) -> None: ...
    
    def sql(self, query: str, params: Optional[Dict[str, Any]] = None) -> duckdb.DuckDBPyRelation: ...
    
    def close(self) -> None: ...