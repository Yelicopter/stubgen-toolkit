import re
from typing import Dict, List

from sqlglot import exp, expressions, parse_one, select
from sqlglot.expressions import Subquery
from sqlglot.optimizer.normalize_identifiers import normalize_identifiers
from sqlglot.optimizer.qualify_columns import quote_identifiers

from ..data_loader.loader import DatasetLoader
from ..data_loader.semantic_layer_schema import SemanticLayerSchema, Transformation
from ..helpers.sql_sanitizer import sanitize_view_column_name
from .base_query_builder import BaseQueryBuilder
from .sql_transformation_manager import SQLTransformationManager

class ViewQueryBuilder(BaseQueryBuilder):
    schema_dependencies_dict: Dict[str, DatasetLoader]
    
    def __init__(
        self,
        schema: SemanticLayerSchema,
        schema_dependencies_dict: Dict[str, DatasetLoader],
    ) -> None: ...
    
    @staticmethod
    def normalize_view_column_name(name: str) -> str: ...
    
    @staticmethod
    def normalize_view_column_alias(name: str) -> str: ...
    
    def _get_group_by_columns(self) -> List[str]: ...
    
    def _get_aliases(self) -> List[str]: ...
    
    def _get_columns(self) -> List[str]: ...
    
    def build_query(self) -> str: ...
    
    def get_head_query(self, n=5) -> str: ...
    
    def _get_sub_query_from_loader(self, loader: DatasetLoader) -> Subquery: ...
    
    def _get_table_expression(self) -> str: ...