from .base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from typing import Any

class LocalQueryBuilder(BaseQueryBuilder):
    dataset_path: str
    def __init__(self, schema: Any, dataset_path: str) -> None: ...
