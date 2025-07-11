from ..data_loader.loader import DatasetLoader as DatasetLoader
from ..data_loader.semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema, Transformation as Transformation
from ..helpers.sql_sanitizer import sanitize_view_column_name as sanitize_view_column_name
from .base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from .sql_transformation_manager import SQLTransformationManager as SQLTransformationManager
from _typeshed import Incomplete
from sqlglot import expressions as expressions
from sqlglot.expressions import Subquery as Subquery
from typing import Dict

class ViewQueryBuilder(BaseQueryBuilder):
    schema_dependencies_dict: Incomplete
    def __init__(self, schema: SemanticLayerSchema, schema_dependencies_dict: Dict[str, DatasetLoader]) -> None: ...
    @staticmethod
    def normalize_view_column_name(name: str) -> str: ...
    @staticmethod
    def normalize_view_column_alias(name: str) -> str: ...
    def build_query(self) -> str: ...
    def get_head_query(self, n: int = ...): ...
