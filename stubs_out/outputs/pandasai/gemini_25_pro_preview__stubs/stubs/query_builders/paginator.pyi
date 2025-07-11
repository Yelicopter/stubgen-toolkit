from pydantic import BaseModel
from typing import Any, List, Optional, Tuple

class PaginationParams(BaseModel):
    page: int
    page_size: int
    search: Optional[str]
    sort_by: Optional[str]
    sort_order: Optional[str]
    filters: Optional[Any]
    @classmethod
    def not_sql(cls, field: Any) -> Any: ...

class DatasetPaginator:
    @staticmethod
    def is_float(value: Any) -> bool: ...
    @staticmethod
    def is_valid_boolean(value: Any) -> bool: ...
    @staticmethod
    def is_valid_uuid(value: Any) -> bool: ...
    @staticmethod
    def is_valid_datetime(value: str) -> bool: ...
    @staticmethod
    def apply_pagination(query: str, columns: List[dict[str, str]], pagination: Optional[PaginationParams], target_dialect: str = ...) -> Tuple[str, List[Any]]: ...
