from enum import Enum
from fastapi._compat import CoreSchema as CoreSchema, GetJsonSchemaHandler as GetJsonSchemaHandler, JsonSchemaValue as JsonSchemaValue, PYDANTIC_V2 as PYDANTIC_V2, with_info_plain_validator_function as with_info_plain_validator_function
from fastapi.logger import logger as logger
from pydantic import AnyUrl as AnyUrl, BaseModel
from typing import Any, Dict, List, Optional, Union
from typing_extensions import TypedDict

class BaseModelWithConfig(BaseModel): ...

class Contact(BaseModelWithConfig):
    name: Optional[str]
    url: Optional[AnyUrl]
    email: Optional[str]

class License(BaseModelWithConfig):
    identifier: Optional[str]
    url: Optional[AnyUrl]

class Info(BaseModelWithConfig):
    title: str
    summary: Optional[str]
    description: Optional[str]
    termsOfService: Optional[AnyUrl]
    contact: Optional[Contact]
    license: Optional[License]
    version: str

class ServerVariable(BaseModelWithConfig):
    enum: Optional[List[str]]
    default: Optional[str]
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
    allOf: Optional[List['SchemaOrBool']]
    anyOf: Optional[List['SchemaOrBool']]
    oneOf: Optional[List['SchemaOrBool']]
    not_: Optional['SchemaOrBool']
    if_: Optional['SchemaOrBool']
    then: Optional['SchemaOrBool']
    else_: Optional['SchemaOrBool']
    dependentSchemas: Optional[Dict[str, 'SchemaOrBool']]
    prefixItems: Optional[List['SchemaOrBool']]
    items: Optional['SchemaOrBool']
    contains: Optional['SchemaOrBool']
    properties: Optional[Dict[str, 'SchemaOrBool']]
    patternProperties: Optional[Dict[str, 'SchemaOrBool']]
    additionalProperties: Optional['SchemaOrBool']
    propertyNames: Optional['SchemaOrBool']
    unevaluatedItems: Optional['SchemaOrBool']
    unevaluatedProperties: Optional['SchemaOrBool']
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
    headers: Optional[Dict[str, Any]]
    style: Optional[str]
    explode: Optional[bool]
    allowReserved: Optional[bool]

class MediaType(BaseModelWithConfig):
    schema_: Optional[Schema]
    example: Optional[Any]
    examples: Optional[Dict[str, Any]]
    encoding: Optional[Dict[str, Encoding]]

class ParameterBase(BaseModelWithConfig):
    description: Optional[str]
    required: Optional[bool]
    deprecated: Optional[bool]
    style: Optional[str]
    explode: Optional[bool]
    allowReserved: Optional[bool]
    schema_: Optional[Schema]
    example: Optional[Any]
    examples: Optional[Dict[str, Any]]
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
    parameters: Optional[Dict[str, Any]]
    requestBody: Optional[Any]
    description: Optional[str]
    server: Optional[Server]

class Response(BaseModelWithConfig):
    description: str
    headers: Optional[Dict[str, Header]]
    content: Optional[Dict[str, MediaType]]
    links: Optional[Dict[str, Link]]

class Operation(BaseModelWithConfig):
    tags: Optional[List[str]]
    summary: Optional[str]
    description: Optional[str]
    externalDocs: Optional[ExternalDocumentation]
    operationId: Optional[str]
    parameters: Optional[List[Parameter]]
    requestBody: Optional[RequestBody]
    responses: Dict[str, Response]
    callbacks: Optional[Dict[str, Any]]
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
    parameters: Optional[List[Parameter]]

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
    schemas: Optional[Dict[str, Schema]]
    responses: Optional[Dict[str, Response]]
    parameters: Optional[Dict[str, Parameter]]
    examples: Optional[Dict[str, Any]]
    requestBodies: Optional[Dict[str, RequestBody]]
    headers: Optional[Dict[str, Header]]
    securitySchemes: Optional[Dict[str, SecurityScheme]]
    links: Optional[Dict[str, Link]]
    callbacks: Optional[Dict[str, Any]]
    pathItems: Optional[Dict[str, PathItem]]

class Tag(BaseModelWithConfig):
    name: str
    description: Optional[str]
    externalDocs: Optional[ExternalDocumentation]

class OpenAPI(BaseModelWithConfig):
    openapi: str
    info: Info
    jsonSchemaDialect: Optional[str]
    servers: Optional[List[Server]]
    paths: Optional[Dict[str, PathItem]]
    webhooks: Optional[Dict[str, PathItem]]
    components: Optional[Components]
    security: Optional[List[Dict[str, List[str]]]]
    tags: Optional[List[Tag]]
    externalDocs: Optional[ExternalDocumentation]
