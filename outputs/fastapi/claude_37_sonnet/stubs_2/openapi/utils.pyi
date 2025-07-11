import http.client
import inspect
import warnings
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union, cast

from fastapi import routing
from fastapi.datastructures import DefaultPlaceholder
from fastapi.dependencies.models import Dependant
from fastapi.dependencies.utils import (
    _get_flat_fields_from_params,
    get_flat_dependant,
    get_flat_params,
)
from fastapi.encoders import jsonable_encoder
from fastapi.openapi.constants import METHODS_WITH_BODY, REF_PREFIX, REF_TEMPLATE
from fastapi.openapi.models import OpenAPI
from fastapi.params import Body, ParamTypes
from fastapi.responses import Response
from fastapi.types import ModelNameMap
from fastapi.utils import (
    deep_dict_update,
    generate_operation_id_for_path,
    is_body_allowed_for_status_code,
)
from pydantic import BaseModel
from starlette.responses import JSONResponse
from starlette.routing import BaseRoute
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from typing_extensions import Literal

validation_error_definition: Dict[str, Any]
validation_error_response_definition: Dict[str, Any]
status_code_ranges: Dict[str, str]

def get_openapi_security_definitions(
    flat_dependant: Dependant,
) -> Tuple[Dict[str, Any], List[Dict[str, List[str]]]]: ...

def _get_openapi_operation_parameters(
    *,
    dependant: Dependant,
    schema_generator: Any,
    model_name_map: ModelNameMap,
    field_mapping: Dict[Tuple[Any, Optional[str]], Dict[str, Any]],
    separate_input_output_schemas: bool = ...,
) -> List[Dict[str, Any]]: ...

def get_openapi_operation_request_body(
    *,
    body_field: Optional[Any],
    schema_generator: Any,
    model_name_map: ModelNameMap,
    field_mapping: Dict[Tuple[Any, Optional[str]], Dict[str, Any]],
    separate_input_output_schemas: bool = ...,
) -> Optional[Dict[str, Any]]: ...

def generate_operation_id(
    *, route: routing.APIRoute, method: str
) -> str: ...

def generate_operation_summary(*, route: routing.APIRoute, method: str) -> str: ...

def get_openapi_operation_metadata(
    *, route: routing.APIRoute, method: str, operation_ids: Set[str]
) -> Dict[str, Any]: ...

def get_openapi_path(
    *,
    route: routing.APIRoute,
    operation_ids: Set[str],
    schema_generator: Any,
    model_name_map: ModelNameMap,
    field_mapping: Dict[Tuple[Any, Optional[str]], Dict[str, Any]],
    separate_input_output_schemas: bool = ...,
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]: ...

def get_fields_from_routes(
    routes: Sequence[BaseRoute],
) -> List[Any]: ...

def get_openapi(
    *,
    title: str,
    version: str,
    openapi_version: str = ...,
    summary: Optional[str] = ...,
    description: Optional[str] = ...,
    routes: Sequence[BaseRoute],
    webhooks: Optional[Sequence[BaseRoute]] = ...,
    tags: Optional[List[Dict[str, Any]]] = ...,
    servers: Optional[List[Dict[str, Union[str, Any]]]] = ...,
    terms_of_service: Optional[str] = ...,
    contact: Optional[Dict[str, Union[str, Any]]] = ...,
    license_info: Optional[Dict[str, Union[str, Any]]] = ...,
    separate_input_output_schemas: bool = ...,
) -> Dict[str, Any]: ...
