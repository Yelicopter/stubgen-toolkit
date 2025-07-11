from fastapi import routing as routing
from fastapi._compat import GenerateJsonSchema as GenerateJsonSchema, JsonSchemaValue as JsonSchemaValue, ModelField as ModelField, Undefined as Undefined, get_compat_model_name_map as get_compat_model_name_map, get_definitions as get_definitions, get_schema_from_model_field as get_schema_from_model_field, lenient_issubclass as lenient_issubclass
from fastapi.datastructures import DefaultPlaceholder as DefaultPlaceholder
from fastapi.dependencies.models import Dependant as Dependant
from fastapi.dependencies.utils import get_flat_dependant as get_flat_dependant, get_flat_params as get_flat_params
from fastapi.openapi.constants import METHODS_WITH_BODY as METHODS_WITH_BODY, REF_PREFIX as REF_PREFIX, REF_TEMPLATE as REF_TEMPLATE
from fastapi.openapi.models import OpenAPI as OpenAPI
from fastapi.params import Body as Body, ParamTypes as ParamTypes
from fastapi.responses import Response as Response
from fastapi.types import ModelNameMap as ModelNameMap
from fastapi.utils import deep_dict_update as deep_dict_update, generate_operation_id_for_path as generate_operation_id_for_path, is_body_allowed_for_status_code as is_body_allowed_for_status_code
from pydantic import BaseModel as BaseModel
from starlette.responses import JSONResponse as JSONResponse
from starlette.routing import BaseRoute as BaseRoute
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY as HTTP_422_UNPROCESSABLE_ENTITY
from typing import Any, Dict, List, Set

def get_openapi_security_definitions(flat_dependant: Dependant) -> Any: ...
def get_openapi_path(*, route: routing.APIRoute, operation_ids: Set[str], schema_generator: GenerateJsonSchema, model_name_map: ModelNameMap, field_mapping: Dict[ModelField, JsonSchemaValue], separate_input_output_schemas: bool = ...) -> Any: ...
def get_openapi(*, title: str, version: str, openapi_version: str = ..., summary: str = ..., description: str = ..., routes: List[routing.APIRoute], webhooks: List[routing.APIRoute] = ..., tags: List[Dict[str, Any]] = ..., servers: List[Dict[str, Any]] = ..., terms_of_service: str = ..., contact: Dict[str, Any] = ..., license_info: Dict[str, Any] = ..., separate_input_output_schemas: bool = ...) -> Any: ...
