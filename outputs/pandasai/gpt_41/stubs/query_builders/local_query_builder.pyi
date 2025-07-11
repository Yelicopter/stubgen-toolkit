from .base_query_builder import BaseQueryBuilder

class LocalQueryBuilder(BaseQueryBuilder):
    dataset_path: str

    def __init__(self, schema: Any, dataset_path: str): ...
    def _get_table_expression(self) -> str: ...