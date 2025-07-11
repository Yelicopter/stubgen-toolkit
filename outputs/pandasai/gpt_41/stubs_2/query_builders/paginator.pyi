from typing import List, Optional, Tuple, Any
from pydantic import BaseModel

class PaginationParams(BaseModel):
    page: int
    page_size: int
    search: Optional[str]
    sort_by: Optional[str]
    sort_order: Optional[str]
    filters: Optional[Any]

class DatasetPaginator:
    @staticmethod
    def is_float(value: Any) -> bool: ...
    @staticmethod
    def is_valid_boolean(value: Any) -> bool: ...
    @staticmethod
    def is_valid_uuid(value: Any) -> bool: ...
    @staticmethod
    def is_valid_datetime(value: Any) -> bool: ...
    @staticmethod
    def apply_pagination(
        query: str,
        columns: List[dict],
        pagination: Optional[PaginationParams],
        target_dialect: str = ...,
    ) -> Tuple[str, List[Any]]: ...