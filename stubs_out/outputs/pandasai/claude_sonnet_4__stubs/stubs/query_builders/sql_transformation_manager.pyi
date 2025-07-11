from pandasai.data_loader.semantic_layer_schema import Transformation as Transformation, TransformationParams as TransformationParams
from typing import List

class SQLTransformationManager:
    @staticmethod
    def apply_transformations(expr: str, transformations: List[Transformation]) -> str: ...
    @staticmethod
    def get_column_transformations(column_name: str, schema_transformations: List[Transformation]) -> List[Transformation]: ...
    @staticmethod
    def apply_column_transformations(expr: str, column_name: str, schema_transformations: List[Transformation]) -> str: ...
