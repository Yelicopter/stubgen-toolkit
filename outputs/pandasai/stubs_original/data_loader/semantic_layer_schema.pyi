from pandasai.constants import LOCAL_SOURCE_TYPES as LOCAL_SOURCE_TYPES, REMOTE_SOURCE_TYPES as REMOTE_SOURCE_TYPES, VALID_COLUMN_TYPES as VALID_COLUMN_TYPES, VALID_TRANSFORMATION_TYPES as VALID_TRANSFORMATION_TYPES
from pandasai.helpers.path import validate_underscore_name_format as validate_underscore_name_format
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Union

class SQLConnectionConfig(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str
    def __eq__(self, other): ...

class Column(BaseModel):
    name: str
    type: Optional[str]
    description: Optional[str]
    expression: Optional[str]
    alias: Optional[str]
    @classmethod
    def is_column_type_supported(cls, type: str) -> str: ...
    @classmethod
    def is_expression_valid(cls, expr: str) -> str: ...

class Relation(BaseModel):
    name: Optional[str]
    description: Optional[str]
    from_: str
    to: str

class TransformationParams(BaseModel):
    column: Optional[str]
    value: Optional[Union[str, int, float, bool]]
    mapping: Optional[Dict[str, str]]
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
    add_ellipsis: Optional[bool]
    width: Optional[int]
    side: Optional[str]
    pad_char: Optional[str]
    lower: Optional[Union[int, float]]
    upper: Optional[Union[int, float]]
    bins: Optional[Union[int, List[Union[int, float]]]]
    labels: Optional[List[str]]
    drop_first: Optional[bool]
    drop_invalid: Optional[bool]
    start_date: Optional[str]
    end_date: Optional[str]
    country_code: Optional[str]
    columns: Optional[List[str]]
    keep: Optional[str]
    ref_table: Optional[Any]
    ref_column: Optional[str]
    drop_negative: Optional[bool]
    @classmethod
    def validate_required_params(cls, values: dict) -> dict: ...

class Transformation(BaseModel):
    type: str
    params: Optional[TransformationParams]
    @classmethod
    def is_transformation_type_supported(cls, type: str) -> str: ...
    @classmethod
    def set_transform_type(cls, values: dict) -> dict: ...

class Source(BaseModel):
    type: str
    path: Optional[str]
    connection: Optional[SQLConnectionConfig]
    table: Optional[str]
    def is_compatible_source(self, source2: Source): ...
    @classmethod
    def validate_type_and_fields(cls, values): ...

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
    def to_dict(self) -> Dict[str, Any]: ...
    def to_yaml(self) -> str: ...

def is_schema_source_same(schema1: SemanticLayerSchema, schema2: SemanticLayerSchema) -> bool: ...
