from ..data_loader.loader import DatasetLoader as DatasetLoader
from ..data_loader.semantic_layer_schema import SemanticLayerSchema as SemanticLayerSchema, Transformation as Transformation
from ..helpers.sql_sanitizer import sanitize_view_column_name as sanitize_view_column_name
from .base_query_builder import BaseQueryBuilder as BaseQueryBuilder
from .sql_transformation_manager import SQLTransformationManager as SQLTransformationManager
from sqlglot import exp as exp, expressions as expressions, parse_one as parse_one, select as select
from sqlglot.expressions import Subquery as Subquery
from sqlglot.optimizer.normalize_identifiers import normalize_identifiers as normalize_identifiers
from sqlglot.optimizer.qualify_columns import quote_identifiers as quote_identifiers
from typing import Dict

class ViewQueryBuilder(BaseQueryBuilder):
    def __init__(self, schema: SemanticLayerSchema, schema_dependencies_dict: Dict[str, DatasetLoader]) -> None: ...
    @staticmethod
    def normalize_view_column_name(name: str) -> str: ...
    @staticmethod
    def normalize_view_column_alias(name: str) -> str: ...
    def build_query(self) -> str: ...
    def get_head_query(self, n: int = ...) -> str: ...
