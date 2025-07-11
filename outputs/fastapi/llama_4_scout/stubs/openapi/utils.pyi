import http.client
import inspect
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union

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
from fastapi.datastructures import DefaultPlaceholder
from fastapi.dependencies.models import Dependant
from fastapi.dependencies.utils import (
    _get_flat_fields_from_params,
    get_flat_dependant,
    get_flat_params,
)
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

def get_openapi_security_definitions(
    flat_dependant: Dependant,
) -> Any:
    ...

def get_openapi_path(
    *,
    route: routing.APIRoute,
    operation_ids: Set[str],
    schema_generator: GenerateJsonSchema,
    model_name_map: ModelNameMap,
    field_mapping: Dict[ModelField, JsonSchemaValue],
    separate_input_output_schemas: bool = True,
) -> Any:
    ...

def get_openapi(
    *,
    title: str,
    version: str,
    openapi_version: str = "3.1.0",
    summary: str = None,
    description: str = None,
    routes: List[routing.APIRoute],
    webhooks: List[routing.APIRoute] = None,
    tags: List[Dict[str, Any]] = None,
    servers: List[Dict[str, Any]] = None,
    terms_of_service: str = None,
    contact: Dict[str, Any] = None,
    license_info: Dict[str, Any] = None,
    separate_input_output_schemas: bool = True,
) -> Any:
    ...