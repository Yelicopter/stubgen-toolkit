import re
from functools import partial
from typing import Any, Dict, List, Optional, Union
from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)
from sqlglot import ParseError, parse_one
from pandasai.constants import (
    LOCAL_SOURCE_TYPES,
    REMOTE_SOURCE_TYPES,
    VALID_COLUMN_TYPES,
    VALID_TRANSFORMATION_TYPES,
)
from pandasai.helpers.path import validate_underscore_name_format

class SQLConnectionConfig(BaseModel):
    host: str = Field(..., description="Host for the database server")
    port: int = Field(..., description="Port for the database server")
    database: str = Field(..., description="Target database name")
    user: str = Field(..., description="Database username")
    password: str = Field(..., description="Database password")
    
    def __eq__(self, other: object) -> bool: ...

class Column(BaseModel):
    name: str = Field(..., description="Name of the column.")
    type: Optional[str] = Field(None, description="Data type of the column.")
    description: Optional[str] = Field(None, description="Description of the column")
    expression: Optional[str] = Field(
        None, description="Aggregation expression (avg, min, max, sum)"
    )
    alias: Optional[str] = Field(None, description="Alias for the column")
    
    @field_validator("type")
    @classmethod
    def is_column_type_supported(cls, type: str) -> str: ...
    
    @field_validator("expression")
    @classmethod
    def is_expression_valid(cls, expr: str) -> str: ...

class Relation(BaseModel):
    name: Optional[str] = Field(None, description="Name of the relationship.")
    description: Optional[str] = Field(
        None, description="Description of the relationship."
    )
    from_: str = Field(
        ..., alias="from", description="Source column for the relationship."
    )
    to: str = Field(..., description="Target column for the relationship.")

class TransformationParams(BaseModel):
    column: Optional[str] = Field(None, description="Column to transform")
    value: Optional[Union[str, int, float]] = Field(
        None, description="Value for fill_na and other transformations"
    )
    mapping: Optional[Dict[str, str]] = Field(
        None, description="Mapping dictionary for map_values transformation"
    )
    format: Optional[str] = Field(None, description="Format string for date formatting")
    decimals: Optional[int] = Field(
        None, description="Number of decimal places for rounding"
    )
    factor: Optional[Union[int, float]] = Field(None, description="Scaling factor")
    to_tz: Optional[str] = Field(None, description="Target timezone or format")
    from_tz: Optional[str] = Field(None, description="From timezone or format")
    errors: Optional[str] = Field(
        None, description="Error handling mode for numeric/datetime conversion"
    )
    old_value: Optional[str] = Field(
        None, description="Old value for replace transformation"
    )
    new_value: Optional[str] = Field(
        None, description="New value for replace transformation"
    )
    new_name: Optional[str] = Field(
        None, description="New name for column in rename transformation"
    )
    pattern: Optional[str] = Field(
        None, description="Pattern for extract transformation"
    )
    length: Optional[int] = Field(
        None, description="Length for truncate transformation"
    )
    add_ellipsis: Optional[bool] = Field(
        True, description="Whether to add ellipsis in truncate"
    )
    width: Optional[int] = Field(None, description="Width for pad transformation")
    side: Optional[str] = Field("left", description="Side for pad transformation")
    pad_char: Optional[str] = Field(" ", description="Character for pad transformation")
    lower: Optional[Union[int, float]] = Field(None, description="Lower bound for clip")
    upper: Optional[Union[int, float]] = Field(None, description="Upper bound for clip")
    bins: Optional[Union[List[int], List[float]]] = Field(
        None, description="Bins for binning"
    )
    labels: Optional[List[str]] = Field(None, description="Labels for bins")
    drop_first: Optional[bool] = Field(
        True, description="Whether to drop first category in encoding"
    )
    drop_invalid: Optional[bool] = Field(
        False, description="Whether to drop invalid values"
    )
    start_date: Optional[str] = Field(
        None, description="Start date for date range validation"
    )
    end_date: Optional[str] = Field(
        None, description="End date for date range validation"
    )
    country_code: Optional[str] = Field(
        "+1", description="Country code for phone normalization"
    )
    columns: Optional[List[str]] = Field(
        None, description="List of columns for multi-column operations"
    )
    keep: Optional[str] = Field("first", description="Which duplicates to keep")
    ref_table: Optional[str] = Field(
        None, description="Reference DataFrame for foreign key validation"
    )
    ref_column: Optional[str] = Field(
        None, description="Reference column for foreign key validation"
    )
    drop_negative: Optional[bool] = Field(
        False, description="Whether to drop negative values"
    )
    
    @model_validator(mode="before")
    @classmethod
    def validate_required_params(cls, values: dict) -> dict: ...

class Transformation(BaseModel):
    type: str = Field(..., description="Type of transformation to be applied.")
    params: Optional[TransformationParams] = Field(
        None, description="Parameters for the transformation."
    )
    
    @field_validator("type")
    @classmethod
    def is_transformation_type_supported(cls, type: str) -> str: ...
    
    @model_validator(mode="before")
    @classmethod
    def set_transform_type(cls, values: dict) -> dict: ...

class Source(BaseModel):
    type: str = Field(..., description="Type of the data source.")
    path: Optional[str] = Field(None, description="Path of the local data source.")
    connection: Optional[SQLConnectionConfig] = Field(
        None, description="Connection object of the data source."
    )
    table: Optional[str] = Field(None, description="Table of the data source.")
    
    def is_compatible_source(self, source2: Source) -> bool: ...
    
    @model_validator(mode="before")
    @classmethod
    def validate_type_and_fields(cls, values: dict) -> dict: ...

class Destination(BaseModel):
    type: str = Field(..., description="Type of the destination.")
    format: str = Field(..., description="Format of the output file.")
    path: str = Field(..., description="Path to save the output file.")
    
    @field_validator("format")
    @classmethod
    def is_format_supported(cls, format: str) -> str: ...

class SemanticLayerSchema(BaseModel):
    name: str = Field(..., description="Dataset name.")
    source: Optional[Source] = Field(None, description="Data source for your dataset.")
    view: Optional[bool] = Field(None, description="Whether table is a view")
    description: Optional[str] = Field(
        None, description="Dataset's contents and purpose description."
    )
    columns: Optional[List[Column]] = Field(
        None, description="Structure and metadata of your dataset's columns"
    )
    relations: Optional[List[Relation]] = Field(
        None, description="Relationships between columns and tables."
    )
    order_by: Optional[List[str]] = Field(
        None, description="Ordering criteria for the dataset."
    )
    limit: Optional[int] = Field(
        None, description="Maximum number of records to retrieve."
    )
    transformations: Optional[List[Transformation]] = Field(
        None, description="List of transformations to apply to the data."
    )
    destination: Optional[Destination] = Field(
        None, description="Destination for saving the dataset."
    )
    update_frequency: Optional[str] = Field(
        None, description="Frequency of dataset updates."
    )
    group_by: Optional[List[str]] = Field(
        None,
        description="List of columns to group by. Every non-aggregated column must be included in group_by.",
    )
    
    @model_validator(mode="after")
    def validate_schema(self) -> SemanticLayerSchema: ...
    
    def _validate_name(self) -> None: ...
    def _validate_group_by_columns(self) -> None: ...
    def _validate_columns_relations(self) -> SemanticLayerSchema: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def to_yaml(self) -> str: ...

def is_schema_source_same(
    schema1: SemanticLayerSchema, schema2: SemanticLayerSchema
) -> bool: ...