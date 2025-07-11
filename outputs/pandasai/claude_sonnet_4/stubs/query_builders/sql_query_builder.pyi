from sqlglot.optimizer.normalize_identifiers import normalize_identifiers
from .base_query_builder import BaseQueryBuilder

class SqlQueryBuilder(BaseQueryBuilder):
    def _get_table_expression(self) -> str: ...