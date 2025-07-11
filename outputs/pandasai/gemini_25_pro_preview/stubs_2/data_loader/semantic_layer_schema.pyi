from __future__ import annotations

from typing import Any, Dict, List, Optional, Type, Union

from pydantic import BaseModel

class SQLConnectionConfig(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str
    def __eq__(self, other: Any) -> bool: ...

class Column(BaseModel):
    name: str
    type: Optional[str]
    description: Optional[str]
    expression: Optional[str]
    alias: Optional[str]
    @classmethod
    def is_column_type_supported(cls, type: Optional[str]) -> Optional[str]: ...
    @classmethod
    def is_expression_valid(cls, expr: Optional[str]) -> Optional[str]: ...

class Relation(BaseModel):
    name: Optional[str]
    description: Optional[str]
    from_: str
    to: str

class TransformationParams(BaseModel):
    column: Optional[str]
    value: Optional[Union[str, int, float]]
    mapping: Optional[Dict[str, Any]]
    format: Optional[str]
    decimals: Optional[int]
    factor: Optional[Union[int, float]]
    to_tz: Optional[str]
    from_tz: Optional[str]
    errors: Optional[str]
    old_value: Optional[Any]
    new_value: Optional[Any]
    new_name: Optional[str]
    pattern: Optional[str]
    length: Optional[int]
    add_ellipsis: bool
    width: Optional[int]
    side: str
    pad_char: str
    lower: Optional[Union[int, float]]
    upper: Optional[Union[int, float]]
    bins: Optional[List[Union[int, float]]]
    labels: Optional[List[str]]
    drop_first: bool
    drop_invalid: bool
    start_date: Optional[str]
    end_date: Optional[str]
    country_code: str
    columns: Optional[List[str]]
    keep: str
    ref_table: Optional[str]
    ref_column: Optional[str]
    drop_negative: bool
    @classmethod
    def validate_required_params(cls, values: Dict[str, Any]) -> Dict[str, Any]: ...

class Transformation(BaseModel):
    type: str
    params: Optional[TransformationParams]
    @classmethod
    def is_transformation_type_supported(cls, type: str) -> str: ...
    @classmethod
    def set_transform_type(cls, values: Dict[str, Any]) -> Dict[str, Any]: ...

class Source(BaseModel):
    type: str
    path: Optional[str]
    connection: Optional[SQLConnectionConfig]
    table: Optional[str]
    def is_compatible_source(self, source2: Source) -> bool: ...
    @classmethod
    def validate_type_and_fields(cls, values: Dict[str, Any]) -> Dict[str, Any]: ...

class Destination(BaseModel):
    type: str
    format: str
    path: str
    @classmethod
    def is_format_supported(cls, format: str) -> str: ...

class SemanticLayerSchema(BaseModel):
    name: str
    source: Optional[Source]
    view: Optional[bool]
    description: Optional[str]
    columns: Optional[List[Column]]
    relations: Optional[List[Relation]]
    order_by: Optional[List[str]]
    limit: Optional[int]
    transformations: Optional[List[Transformation]]
    destination: Optional[Destination]
    update_frequency: Optional[str]
    group_by: Optional[List[str]]
    def validate_schema(self) -> SemanticLayerSchema: ...
    def _validate_name(self) -> None: ...
    def _validate_group_by_columns(self) -> None: ...
    def _validate_columns_relations(self) -> SemanticLayerSchema: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def to_yaml(self) -> str: ...

def is_schema_source_same(
    schema1: SemanticLayerSchema, schema2: SemanticLayerSchema
) -> bool: ...