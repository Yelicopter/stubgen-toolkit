import datetime
import json
import uuid
from typing import List, Optional, Tuple, Any
import sqlglot
from pydantic import BaseModel, Field, field_validator
from pandasai.helpers.sql_sanitizer import is_sql_query

class PaginationParams(BaseModel):
    page: int = Field(ge=1, description="Page number, starting from 1")
    page_size: int = Field(
        ge=1, le=100, description="Number of items per page, maximum 100"
    )
    search: Optional[str] = Field(
        None, description="Search term to filter across all fields"
    )
    sort_by: Optional[str] = Field(None, description="Column to sort by")
    sort_order: Optional[str] = Field(
        None, pattern="^(asc|desc)$", description="Sort order (asc or desc)"
    )
    filters: Optional[str] = Field(None, description="Filters to apply to the data")
    
    @field_validator("search", "filters", "sort_by", "sort_order")
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
    def apply_pagination(
        query: str,
        columns: List[dict],
        pagination: Optional[PaginationParams],
        target_dialect: str = "postgres",
    ) -> Tuple[str, List]: ...