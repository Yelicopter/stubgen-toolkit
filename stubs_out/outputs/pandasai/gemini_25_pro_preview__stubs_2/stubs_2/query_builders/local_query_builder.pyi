from .base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from pandasai.data_loader.semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema

class LocalQueryBuilder(BaseQueryBuilder):
    dataset_path: str
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
