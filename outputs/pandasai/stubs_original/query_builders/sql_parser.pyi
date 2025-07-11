from pandasai.exceptions import MaliciousQueryError as MaliciousQueryError
from typing import List, Optional

class SQLParser:
    @staticmethod
    def replace_table_and_column_names(query, table_mapping): ...
    @staticmethod
    def transpile_sql_dialect(query: str, to_dialect: str, from_dialect: Optional[str] = ...): ...
    @staticmethod
    def extract_table_names(sql_query: str, dialect: str = ...) -> List[str]: ...
