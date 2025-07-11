from enum import Enum
from fastapi._compat import CoreSchema as CoreSchema, GetJsonSchemaHandler as GetJsonSchemaHandler, JsonSchemaValue as JsonSchemaValue, with_info_plain_validator_function as with_info_plain_validator_function
from fastapi.logger import logger as logger
from pydantic import AnyUrl as AnyUrl, BaseModel, EmailStr
from typing import Any, Callable, Dict, Iterable, List, Optional, Type, Union
from typing_extensions import TypedDict

class EmailStr(str):
    @classmethod
    def __get_validators__(cls) -> Iterable[Callable[..., Any]]: ...
    @classmethod
    def validate(cls, v: Any) -> str: ...
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue: ...
    @classmethod
    def __get_pydantic_core_schema__(cls, source: Type[Any], handler: Callable[..., CoreSchema]) -> CoreSchema: ...

class BaseModelWithConfig(BaseModel):
    model_config: Dict[str, Any]
    class Config:
        extra: str

class Contact(BaseModelWithConfig):
    name: Optional[str]
    url: Optional[AnyUrl]
    email: Optional[EmailStr]

class License(BaseModelWithConfig):
    name: str
    identifier: Optional[str]
    url: Optional[AnyUrl]

class Info(BaseModelWithConfig):
    title: str
    summary: Optional[str]
    description: Optional[str]
    termsOfService: Optional[str]
    contact: Optional[Contact]
    license: Optional[License]
    version: str

class ServerVariable(BaseModelWithConfig):
    enum: Optional[List[str]]
    default: str
    description: Optional[str]

class Server(BaseModelWithConfig):
    url: Union[AnyUrl, str]
    description: Optional[str]
    variables: Optional[Dict[str, ServerVariable]]

class Reference(BaseModel):
    ref: str

class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]]

class XML(BaseModelWithConfig):
    name: Optional[str]
    namespace: Optional[str]
    prefix: Optional[str]
    attribute: Optional[bool]
    wrapped: Optional[bool]

class ExternalDocumentation(BaseModelWithConfig):
    description: Optional[str]
    url: AnyUrl

class Schema(BaseModelWithConfig):
    schema_: Optional[str]
    vocabulary: Optional[str]
    id: Optional[str]
    anchor: Optional[str]
    dynamicAnchor: Optional[str]
    ref: Optional[str]
    dynamicRef: Optional[str]
    defs: Optional[Dict[str, 'Schema']]
    comment: Optional[str]
    allOf: Optional[List['Schema']]
    anyOf: Optional[List['Schema']]
    oneOf: Optional[List['Schema']]
    not_: Optional['Schema']
    if_: Optional['Schema']
    then: Optional['Schema']
    else_: Optional['Schema']
    dependentSchemas: Optional[Dict[str, 'Schema']]
    prefixItems: Optional[List['Schema']]
    items: Optional[Union['Schema', bool]]
    contains: Optional['Schema']
    properties: Optional[Dict[str, 'Schema']]
    patternProperties: Optional[Dict[str, 'Schema']]
    additionalProperties: Optional['Schema']
    propertyNames: Optional['Schema']
    unevaluatedItems: Optional['Schema']
    unevaluatedProperties: Optional['Schema']
    type: Optional[str]
    enum: Optional[List[Any]]
    const: Optional[Any]
    multipleOf: Optional[float]
    maximum: Optional[float]
    exclusiveMaximum: Optional[float]
    minimum: Optional[float]
    exclusiveMinimum: Optional[float]
    maxLength: Optional[int]
    minLength: Optional[int]
    pattern: Optional[str]
    maxItems: Optional[int]
    minItems: Optional[int]
    uniqueItems: Optional[bool]
    maxContains: Optional[int]
    minContains: Optional[int]
    maxProperties: Optional[int]
    minProperties: Optional[int]
    required: Optional[List[str]]
    dependentRequired: Optional[Dict[str, List[str]]]
    format: Optional[str]
    contentEncoding: Optional[str]
    contentMediaType: Optional[str]
    contentSchema: Optional['Schema']
    title: Optional[str]
    description: Optional[str]
    default: Optional[Any]
    deprecated: Optional[bool]
    readOnly: Optional[bool]
    writeOnly: Optional[bool]
    examples: Optional[List[Any]]
    discriminator: Optional[Discriminator]
    xml: Optional[XML]
    externalDocs: Optional[ExternalDocumentation]
    example: Optional[Any]
SchemaOrBool = Union[Schema, bool]

class Example(TypedDict, total=False):
    summary: Optional[str]
    description: Optional[str]
    value: Optional[Any]
    externalValue: Optional[AnyUrl]

class ParameterInType(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Encoding(BaseModelWithConfig):
    contentType: Optional[str]
    headers: Optional[Dict[str, Union['Header', Reference]]]
    style: Optional[str]
    explode: Optional[bool]
    allowReserved: Optional[bool]

class MediaType(BaseModelWithConfig):
    schema_: Optional[Union[Schema, Reference]]
    example: Optional[Any]
    examples: Optional[Dict[str, Union[Example, Reference]]]
    encoding: Optional[Dict[str, Encoding]]

class ParameterBase(BaseModelWithConfig):
    description: Optional[str]
    required: Optional[bool]
    deprecated: Optional[bool]
    style: Optional[str]
    explode: Optional[bool]
    allowReserved: Optional[bool]
    schema_: Optional[Union[Schema, Reference]]
    example: Optional[Any]
    examples: Optional[Dict[str, Union[Example, Reference]]]
    content: Optional[Dict[str, MediaType]]

class Parameter(ParameterBase):
    name: str
    in_: ParameterInType

class Header(ParameterBase): ...

class RequestBody(BaseModelWithConfig):
    description: Optional[str]
    content: Dict[str, MediaType]
    required: Optional[bool]

class Link(BaseModelWithConfig):
    operationRef: Optional[str]
    operationId: Optional[str]
    parameters: Optional[Dict[str, Union[Any, str]]]
    requestBody: Optional[Union[Any, str]]
    description: Optional[str]
    server: Optional[Server]

class Response(BaseModelWithConfig):
    description: str
    headers: Optional[Dict[str, Union[Header, Reference]]]
    content: Optional[Dict[str, MediaType]]
    links: Optional[Dict[str, Union[Link, Reference]]]

class Operation(BaseModelWithConfig):
    tags: Optional[List[str]]
    summary: Optional[str]
    description: Optional[str]
    externalDocs: Optional[ExternalDocumentation]
    operationId: Optional[str]
    parameters: Optional[List[Union[Parameter, Reference]]]
    requestBody: Optional[Union[RequestBody, Reference]]
    responses: Optional[Dict[str, Union[Response, Reference]]]
    callbacks: Optional[Dict[str, Union[Dict[str, 'PathItem'], Reference]]]
    deprecated: Optional[bool]
    security: Optional[List[Dict[str, List[str]]]]
    servers: Optional[List[Server]]

class PathItem(BaseModelWithConfig):
    ref: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    get: Optional[Operation]
    put: Optional[Operation]
    post: Optional[Operation]
    delete: Optional[Operation]
    options: Optional[Operation]
    head: Optional[Operation]
    patch: Optional[Operation]
    trace: Optional[Operation]
    servers: Optional[List[Server]]
    parameters: Optional[List[Union[Parameter, Reference]]]

class SecuritySchemeType(Enum):
    apiKey: str
    http: str
    oauth2: str
    openIdConnect: str

class SecurityBase(BaseModelWithConfig):
    type_: SecuritySchemeType
    description: Optional[str]

class APIKeyIn(Enum):
    query: str
    header: str
    cookie: str

class APIKey(SecurityBase):
    type_: SecuritySchemeType
    in_: APIKeyIn
    name: str

class HTTPBase(SecurityBase):
    type_: SecuritySchemeType
    scheme: str

class HTTPBearer(HTTPBase):
    scheme: str
    bearerFormat: Optional[str]

class OAuthFlow(BaseModelWithConfig):
    refreshUrl: Optional[str]
    scopes: Dict[str, str]

class OAuthFlowImplicit(OAuthFlow):
    authorizationUrl: str

class OAuthFlowPassword(OAuthFlow):
    tokenUrl: str

class OAuthFlowClientCredentials(OAuthFlow):
    tokenUrl: str

class OAuthFlowAuthorizationCode(OAuthFlow):
    authorizationUrl: str
    tokenUrl: str

class OAuthFlows(BaseModelWithConfig):
    implicit: Optional[OAuthFlowImplicit]
    password: Optional[OAuthFlowPassword]
    clientCredentials: Optional[OAuthFlowClientCredentials]
    authorizationCode: Optional[OAuthFlowAuthorizationCode]

class OAuth2(SecurityBase):
    type_: SecuritySchemeType
    flows: OAuthFlows

class OpenIdConnect(SecurityBase):
    type_: SecuritySchemeType
    openIdConnectUrl: str
SecurityScheme = Union[APIKey, HTTPBase, OAuth2, OpenIdConnect, HTTPBearer]

class Components(BaseModelWithConfig):
    schemas: Optional[Dict[str, Union[Schema, Reference]]]
    responses: Optional[Dict[str, Union[Response, Reference]]]
    parameters: Optional[Dict[str, Union[Parameter, Reference]]]
    examples: Optional[Dict[str, Union[Example, Reference]]]
    requestBodies: Optional[Dict[str, Union[RequestBody, Reference]]]
    headers: Optional[Dict[str, Union[Header, Reference]]]
    securitySchemes: Optional[Dict[str, Union[SecurityScheme, Reference]]]
    links: Optional[Dict[str, Union[Link, Reference]]]
    callbacks: Optional[Dict[str, Union[Dict[str, PathItem], Reference]]]
    pathItems: Optional[Dict[str, Union[PathItem, Reference]]]

class Tag(BaseModelWithConfig):
    name: str
    description: Optional[str]
    externalDocs: Optional[ExternalDocumentation]

class OpenAPI(BaseModelWithConfig):
    openapi: str
    info: Info
    jsonSchemaDialect: Optional[str]
    servers: Optional[List[Server]]
    paths: Optional[Dict[str, Union[PathItem, Any]]]
    webhooks: Optional[Dict[str, Union[PathItem, Reference]]]
    components: Optional[Components]
    security: Optional[List[Dict[str, List[str]]]]
    tags: Optional[List[Tag]]
    externalDocs: Optional[ExternalDocumentation]
