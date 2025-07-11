from pandasai.data_loader.semantic_layer_schema import SemanticLayerSchema

from .base_query_builder import BaseQueryBuilder

class LocalQueryBuilder(BaseQueryBuilder):
    dataset_path: str
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
    def _get_table_expression(self) -> str: ...