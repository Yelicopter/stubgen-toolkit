from ..data_loader.semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema
from .base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from pandasai.config import ConfigManager as ConfigManager

class LocalQueryBuilder(BaseQueryBuilder):
    def __init__(self, schema: SemanticLayerSchema, dataset_path: str) -> None: ...
