from pandasai.helpers.sql_sanitizer import is_sql_query as is_sql_query
from pydantic import BaseModel
from typing import List, Tuple

class PaginationParams(BaseModel):
    page: int
    page_size: int
    search: str | None
    sort_by: str | None
    sort_order: str | None
    filters: str | None
    @classmethod
    def not_sql(cls, field: str) -> str: ...

class DatasetPaginator:
    @staticmethod
    def is_float(value: str) -> bool: ...
    @staticmethod
    def is_valid_boolean(value: str) -> bool: ...
    @staticmethod
    def is_valid_uuid(value: str) -> bool: ...
    @staticmethod
    def is_valid_datetime(value: str) -> bool: ...
    @staticmethod
    def apply_pagination(query: str, columns: List[dict], pagination: PaginationParams | None, target_dialect: str = ...) -> Tuple[str, List]: ...
