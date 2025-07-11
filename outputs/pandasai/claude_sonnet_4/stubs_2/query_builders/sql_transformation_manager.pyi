from typing import Any, Dict, List, Optional, Union
from pandasai.data_loader.semantic_layer_schema import (
    Transformation,
    TransformationParams,
)

class SQLTransformationManager:
    @staticmethod
    def _quote_str(value: str) -> str: ...
    
    @staticmethod
    def _validate_numeric(
        value: Union[int, float, str], param_name: str
    ) -> Union[int, float]: ...
    
    @staticmethod
    def apply_transformations(expr: str, transformations: List[Transformation]) -> str: ...
    
    @staticmethod
    def _anonymize(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _fill_na(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _map_values(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _to_lowercase(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _to_uppercase(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _round_numbers(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _format_date(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _truncate(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _scale(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _normalize(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _standardize(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _convert_timezone(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _strip(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _to_numeric(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _to_datetime(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _replace(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _extract(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _pad(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _clip(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _bin(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _validate_email(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _validate_date_range(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _normalize_phone(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _remove_duplicates(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _validate_foreign_key(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _ensure_positive(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _standardize_categories(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def _rename(expr: str, params: TransformationParams) -> str: ...
    
    @staticmethod
    def get_column_transformations(
        column_name: str, schema_transformations: List[Transformation]
    ) -> List[Transformation]: ...
    
    @staticmethod
    def apply_column_transformations(
        expr: str, column_name: str, schema_transformations: List[Transformation]
    ) -> str: ...