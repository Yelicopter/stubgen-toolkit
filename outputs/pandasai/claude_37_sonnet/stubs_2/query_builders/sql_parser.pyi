from typing import Any, Dict, List, Optional

import sqlglot
from sqlglot import ParseError, exp, parse_one
from sqlglot.optimizer.qualify_columns import quote_identifiers

from pandasai.exceptions import MaliciousQueryError

class SQLParser:
    @staticmethod
    def replace_table_and_column_names(query: str, table_mapping: Dict[str, str]) -> str: ...
    
    @staticmethod
    def transpile_sql_dialect(
        query: str, to_dialect: str, from_dialect: Optional[str] = None
    ) -> str: ...
    
    @staticmethod
    def extract_table_names(sql_query: str, dialect: str = "postgres") -> List[str]: ...