from pandasai.helpers.sql_sanitizer import is_sql_query as is_sql_query
from pydantic import BaseModel
from typing import Any, List, Optional, Tuple

class PaginationParams(BaseModel):
    page: int
    page_size: int
    search: Optional[str]
    sort_by: Optional[str]
    sort_order: Optional[str]
    filters: Optional[str]
    @classmethod
    def not_sql(cls, field: Any) -> Any: ...

class DatasetPaginator:
    @staticmethod
    def is_float(value: str) -> bool: ...
    @staticmethod
    def is_valid_boolean(value: Any) -> bool: ...
    @staticmethod
    def is_valid_uuid(value: str) -> bool: ...
    @staticmethod
    def is_valid_datetime(value: str) -> bool: ...
    @staticmethod
    def apply_pagination(query: str, columns: List[dict], pagination: Optional[PaginationParams], target_dialect: str = ...) -> Tuple[str, List]: ...
