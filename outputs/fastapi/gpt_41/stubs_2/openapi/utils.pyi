from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, Type, Union, cast

def get_openapi_security_definitions(
    flat_dependant: Any,
) -> Tuple[Dict[str, Any], List[Any]]: ...
def _get_openapi_operation_parameters(
    *,
    dependant: Any,
    schema_generator: Any,
    model_name_map: Any,
    field_mapping: Any,
    separate_input_output_schemas: bool = ...,
) -> List[Dict[str, Any]]: ...
def get_openapi_operation_request_body(
    *,
    body_field: Any,
    schema_generator: Any,
    model_name_map: Any,
    field_mapping: Any,
    separate_input_output_schemas: bool = ...,
) -> Optional[Dict[str, Any]]: ...
def generate_operation_id(
    *, route: Any, method: str
) -> str: ...
def generate_operation_summary(*, route: Any, method: str) -> str: ...
def get_openapi_operation_metadata(
    *, route: Any, method: str, operation_ids: Set[str]
) -> Dict[str, Any]: ...
def get_openapi_path(
    *,
    route: Any,
    operation_ids: Set[str],
    schema_generator: Any,
    model_name_map: Any,
    field_mapping: Any,
    separate_input_output_schemas: bool = ...,
) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]: ...
def get_fields_from_routes(
    routes: Sequence[Any],
) -> List[Any]: ...
def get_openapi(
    *,
    title: str,
    version: str,
    openapi_version: str = ...,
    summary: Optional[str] = ...,
    description: Optional[str] = ...,
    routes: Sequence[Any],
    webhooks: Optional[Sequence[Any]] = ...,
    tags: Optional[List[Any]] = ...,
    servers: Optional[List[Any]] = ...,
    terms_of_service: Optional[str] = ...,
    contact: Optional[Dict[str, Any]] = ...,
    license_info: Optional[Dict[str, Any]] = ...,
    separate_input_output_schemas: bool = ...,
) -> Dict[str, Any]: ...