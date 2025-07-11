import warnings
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union, cast

from fastapi import routing
from fastapi._compat import (
    GenerateJsonSchema,
    JsonSchemaValue,
    ModelField,
    Undefined,
    get_compat_model_name_map,
    get_definitions,
    get_schema_from_model_field,
    lenient_issubclass,
)
from fastapi.dependencies.models import Dependant
from fastapi.params import ParamTypes
from fastapi.routing import APIRoute
from fastapi.types import ModelNameMap
from pydantic import BaseModel
from starlette.routing import BaseRoute
from typing_extensions import Literal

validation_error_definition: Dict[str, Any]
validation_error_response_definition: Dict[str, Any]
status_code_ranges: Dict[str, str]

def get_openapi_security_definitions(
    flat_dependant: Dependant,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]: ...
def _get_openapi_operation_parameters(
    *,
    dependant: Dependant,
    schema_generator: GenerateJsonSchema,
    model_name_map: ModelNameMap,
    field_mapping: Dict[Any, Any],
    separate_input_output_schemas: bool = True,
) -> List[Dict[str, Any]]: ...
def get_openapi_operation_request_body(
    *,
    body_field: Optional[ModelField],
    schema_generator: GenerateJsonSchema,
    model_name_map: ModelNameMap,
    field_mapping: Dict[Any, Any],
    separate_input_output_schemas: bool = True,
) -> Optional[Dict[str, Any]]: ...
def generate_operation_id(*, route: APIRoute, method: str) -> str: ...
def generate_operation_summary(*, route: APIRoute, method: str) -> str: ...
def get_openapi_operation_metadata(
    *, route: APIRoute, method: str, operation_ids: Set[str]
) -> Dict[str, Any]: ...
def get_openapi_path(
    *,
    route: APIRoute,
    operation_ids: Set[str],
    schema_generator: GenerateJsonSchema,
    model_name_map: ModelNameMap,
    field_mapping: Dict[Any, Any],
    separate_input_output_schemas: bool = True,
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]: ...
def get_fields_from_routes(routes: Sequence[BaseRoute]) -> List[ModelField]: ...
def get_openapi(
    *,
    title: str,
    version: str,
    openapi_version: str = "3.1.0",
    summary: Optional[str] = None,
    description: Optional[str] = None,
    routes: Sequence[BaseRoute],
    webhooks: Optional[Sequence[BaseRoute]] = None,
    tags: Optional[List[Dict[str, Any]]] = None,
    servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
    terms_of_service: Optional[str] = None,
    contact: Optional[Dict[str, Union[str, Any]]] = None,
    license_info: Optional[Dict[str, Union[str, Any]]] = None,
    separate_input_output_schemas: bool = True,
) -> Dict[str, Any]: ...