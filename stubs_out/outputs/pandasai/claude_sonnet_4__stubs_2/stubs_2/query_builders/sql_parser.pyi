from pandasai.exceptions import MaliciousQueryError as MaliciousQueryError
from sqlglot import ParseError as ParseError, exp as exp, parse_one as parse_one
from sqlglot.optimizer.qualify_columns import quote_identifiers as quote_identifiers
from typing import List, Optional

class SQLParser:
    @staticmethod
    def replace_table_and_column_names(query: str, table_mapping: dict) -> str: ...
    @staticmethod
    def transpile_sql_dialect(query: str, to_dialect: str, from_dialect: Optional[str] = ...) -> str: ...
    @staticmethod
    def extract_table_names(sql_query: str, dialect: str = ...) -> List[str]: ...
