from pydantic import BaseModel
from typing import Any, List, Optional

class SQLConnectionConfig(BaseModel):
    host: str
    port: int
    database: str
    user: str
    password: str
    def __eq__(self, other: object) -> bool: ...

class Column(BaseModel):
    name: str
    type: Optional[str]
    description: Optional[str]
    expression: Optional[str]
    alias: Optional[str]

class Relation(BaseModel):
    name: Optional[str]
    description: Optional[str]
    from_: str
    to: str

class TransformationParams(BaseModel):
    column: Optional[str]
    value: Any
    mapping: Optional[dict]
    format: Optional[str]
    decimals: Optional[int]
    factor: Optional[Any]
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
    lower: Optional[Any]
    upper: Optional[Any]
    bins: Optional[Any]
    labels: Optional[Any]
    drop_first: bool
    drop_invalid: bool
    start_date: Optional[Any]
    end_date: Optional[Any]
    country_code: str
    columns: Optional[Any]
    keep: str
    ref_table: Optional[Any]
    ref_column: Optional[Any]
    drop_negative: bool

class Transformation(BaseModel):
    type: str
    params: Optional[dict]

class Source(BaseModel):
    type: str
    path: Optional[str]
    connection: Optional[Any]
    table: Optional[str]
    def is_compatible_source(self, source2: Source) -> bool: ...

class Destination(BaseModel):
    type: str
    format: str
    path: str

class SemanticLayerSchema(BaseModel):
    name: str
    source: Optional[Source]
    view: Optional[bool]
    description: Optional[str]
    columns: Optional[List[Column]]
    relations: Optional[List[Relation]]
    order_by: Optional[Any]
    limit: Optional[Any]
    transformations: Optional[List[Transformation]]
    destination: Optional[Destination]
    update_frequency: Optional[Any]
    group_by: Optional[List[str]]
    def to_dict(self) -> dict: ...
    def to_yaml(self) -> str: ...

def is_schema_source_same(schema1: SemanticLayerSchema, schema2: SemanticLayerSchema) -> bool: ...
