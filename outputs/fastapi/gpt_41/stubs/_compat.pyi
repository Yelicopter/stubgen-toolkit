from typing import (
    Any,
    Callable,
    Deque,
    Dict,
    FrozenSet,
    List,
    Mapping,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)
from fastapi.exceptions import RequestErrorModel
from fastapi.types import IncEx, ModelNameMap, UnionType
from pydantic import BaseModel, create_model
from pydantic.version import VERSION as PYDANTIC_VERSION
from starlette.datastructures import UploadFile
from typing_extensions import Annotated, Literal, get_args, get_origin

PYDANTIC_VERSION_MINOR_TUPLE: Tuple[int, ...]
PYDANTIC_V2: bool

sequence_annotation_to_type: Dict[Any, Any]
sequence_types: Tuple[Any, ...]
# Url: Type[Any]

if PYDANTIC_V2:
    from pydantic import PydanticSchemaGenerationError as PydanticSchemaGenerationError
    from pydantic import TypeAdapter
    from pydantic import ValidationError as ValidationError
    from pydantic._internal._schema_generation_shared import GetJsonSchemaHandler as GetJsonSchemaHandler
    from pydantic._internal._typing_extra import eval_type_lenient
    from pydantic._internal._utils import lenient_issubclass as lenient_issubclass
    from pydantic.fields import FieldInfo
    from pydantic.json_schema import GenerateJsonSchema as GenerateJsonSchema
    from pydantic.json_schema import JsonSchemaValue as JsonSchemaValue
    from pydantic_core import CoreSchema as CoreSchema
    from pydantic_core import PydanticUndefined, PydanticUndefinedType
    from pydantic_core import Url as Url

    try:
        from pydantic_core.core_schema import with_info_plain_validator_function as with_info_plain_validator_function
    except ImportError:
        from pydantic_core.core_schema import general_plain_validator_function as with_info_plain_validator_function

    RequiredParam: Any
    Undefined: Any
    UndefinedType: Any
    evaluate_forwardref: Callable[..., Any]
    Validator: Any

    class BaseConfig:
        ...

    class ErrorWrapper(Exception):
        ...

    class ModelField:
        field_info: Any
        name: str
        mode: str
        @property
        def alias(self) -> str: ...
        @property
        def required(self) -> bool: ...
        @property
        def default(self) -> Any: ...
        @property
        def type_(self) -> Any: ...
        def __post_init__(self) -> None: ...
        def get_default(self) -> Any: ...
        def validate(
            self,
            value: Any,
            values: Any = ...,
            *,
            loc: Any = ...,
        ) -> Tuple[Any, Any]: ...
        def serialize(
            self,
            value: Any,
            *,
            mode: str = ...,
            include: Any = ...,
            exclude: Any = ...,
            by_alias: bool = ...,
            exclude_unset: bool = ...,
            exclude_defaults: bool = ...,
            exclude_none: bool = ...,
        ) -> Any: ...
        def __hash__(self) -> int: ...

    def get_annotation_from_field_info(
        annotation: Any, field_info: Any, field_name: str
    ) -> Any: ...
    def _normalize_errors(errors: Any) -> Any: ...
    def _model_rebuild(model: Any) -> None: ...
    def _model_dump(
        model: Any, mode: str = ..., **kwargs: Any
    ) -> Any: ...
    def _get_model_config(model: Any) -> Any: ...
    def get_schema_from_model_field(
        *,
        field: Any,
        schema_generator: Any,
        model_name_map: Any,
        field_mapping: Any,
        separate_input_output_schemas: bool = ...,
    ) -> Any: ...
    def get_compat_model_name_map(fields: Any) -> Any: ...
    def get_definitions(
        *,
        fields: Any,
        schema_generator: Any,
        model_name_map: Any,
        separate_input_output_schemas: bool = ...,
    ) -> Any: ...
    def is_scalar_field(field: Any) -> bool: ...
    def is_sequence_field(field: Any) -> bool: ...
    def is_scalar_sequence_field(field: Any) -> bool: ...
    def is_bytes_field(field: Any) -> bool: ...
    def is_bytes_sequence_field(field: Any) -> bool: ...
    def copy_field_info(*, field_info: Any, annotation: Any) -> Any: ...
    def serialize_sequence_value(*, field: Any, value: Any) -> Any: ...
    def get_missing_field_error(loc: Any) -> Any: ...
    def create_body_model(
        *, fields: Any, model_name: str
    ) -> Any: ...
    def get_model_fields(model: Any) -> Any: ...
else:
    from fastapi.openapi.constants import REF_PREFIX as REF_PREFIX
    from pydantic import AnyUrl as Url
    from pydantic import BaseConfig as BaseConfig
    from pydantic import ValidationError as ValidationError
    from pydantic.class_validators import Validator as Validator
    from pydantic.error_wrappers import ErrorWrapper as ErrorWrapper
    from pydantic.errors import MissingError
    from pydantic.fields import (
        SHAPE_FROZENSET,
        SHAPE_LIST,
        SHAPE_SEQUENCE,
        SHAPE_SET,
        SHAPE_SINGLETON,
        SHAPE_TUPLE,
        SHAPE_TUPLE_ELLIPSIS,
    )
    from pydantic.fields import FieldInfo as FieldInfo
    from pydantic.fields import ModelField as ModelField
    RequiredParam: Any
    from pydantic.fields import Undefined as Undefined
    from pydantic.fields import UndefinedType as UndefinedType
    from pydantic.schema import (
        field_schema,
        get_flat_models_from_fields,
        get_model_name_map,
        model_process_schema,
    )
    from pydantic.schema import get_annotation_from_field_info as get_annotation_from_field_info
    from pydantic.typing import evaluate_forwardref as evaluate_forwardref
    from pydantic.utils import lenient_issubclass as lenient_issubclass

    GetJsonSchemaHandler: Any
    JsonSchemaValue: Any
    CoreSchema: Any

    sequence_shapes: Any
    sequence_shape_to_type: Any

    class GenerateJsonSchema:
        ref_template: str

    class PydanticSchemaGenerationError(Exception):
        ...

    def with_info_plain_validator_function(
        function: Any,
        *,
        ref: Any = ...,
        metadata: Any = ...,
        serialization: Any = ...,
    ) -> Any: ...
    def get_model_definitions(
        *,
        flat_models: Any,
        model_name_map: Any,
    ) -> Any: ...
    def is_pv1_scalar_field(field: Any) -> bool: ...
    def is_pv1_scalar_sequence_field(field: Any) -> bool: ...
    def _normalize_errors(errors: Any) -> Any: ...
    def _model_rebuild(model: Any) -> None: ...
    def _model_dump(
        model: Any, mode: str = ..., **kwargs: Any
    ) -> Any: ...
    def _get_model_config(model: Any) -> Any: ...
    def get_schema_from_model_field(
        *,
        field: Any,
        schema_generator: Any,
        model_name_map: Any,
        field_mapping: Any,
        separate_input_output_schemas: bool = ...,
    ) -> Any: ...
    def get_compat_model_name_map(fields: Any) -> Any: ...
    def get_definitions(
        *,
        fields: Any,
        schema_generator: Any,
        model_name_map: Any,
        separate_input_output_schemas: bool = ...,
    ) -> Any: ...
    def is_scalar_field(field: Any) -> bool: ...
    def is_sequence_field(field: Any) -> bool: ...
    def is_scalar_sequence_field(field: Any) -> bool: ...
    def is_bytes_field(field: Any) -> bool: ...
    def is_bytes_sequence_field(field: Any) -> bool: ...
    def copy_field_info(*, field_info: Any, annotation: Any) -> Any: ...
    def serialize_sequence_value(*, field: Any, value: Any) -> Any: ...
    def get_missing_field_error(loc: Any) -> Any: ...
    def create_body_model(
        *, fields: Any, model_name: str
    ) -> Any: ...
    def get_model_fields(model: Any) -> Any: ...

def _regenerate_error_with_loc(
    *, errors: Any, loc_prefix: Any
) -> Any: ...
def _annotation_is_sequence(annotation: Any) -> bool: ...
def field_annotation_is_sequence(annotation: Any) -> bool: ...
def value_is_sequence(value: Any) -> bool: ...
def _annotation_is_complex(annotation: Any) -> bool: ...
def field_annotation_is_complex(annotation: Any) -> bool: ...
def field_annotation_is_scalar(annotation: Any) -> bool: ...
def field_annotation_is_scalar_sequence(annotation: Any) -> bool: ...
def is_bytes_or_nonable_bytes_annotation(annotation: Any) -> bool: ...
def is_uploadfile_or_nonable_uploadfile_annotation(annotation: Any) -> bool: ...
def is_bytes_sequence_annotation(annotation: Any) -> bool: ...
def is_uploadfile_sequence_annotation(annotation: Any) -> bool: ...
def get_cached_model_fields(model: Any) -> Any: ...