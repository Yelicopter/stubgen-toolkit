from enum import Enum
from typing import Any, Callable, Dict, Iterable, List, Optional, Set, Type, Union

from fastapi._compat import (
    PYDANTIC_V2,
    CoreSchema,
    GetJsonSchemaHandler,
    JsonSchemaValue,
    _model_rebuild,
    with_info_plain_validator_function,
)
from fastapi.logger import logger
from pydantic import AnyUrl, BaseModel, Field
from typing_extensions import Annotated, Literal, TypedDict

class BaseModelWithConfig(BaseModel):
    ...

class Contact(BaseModelWithConfig):
    name: Optional[str] = None
    url: Optional[AnyUrl] = None
    email: Optional[str] = None

class License(BaseModelWithConfig):
    identifier: Optional[str] = None
    url: Optional[AnyUrl] = None

class Info(BaseModelWithConfig):
    title: str
    summary: Optional[str] = None
    description: Optional[str] = None
    termsOfService: Optional[AnyUrl] = None
    contact: Optional[Contact] = None
    license: Optional[License] = None
    version: str

class ServerVariable(BaseModelWithConfig):
    enum: Optional[List[str]] = None
    default: Optional[str] = None
    description: Optional[str] = None

class Server(BaseModelWithConfig):
    url: Union[AnyUrl, str]
    description: Optional[str] = None
    variables: Optional[Dict[str, ServerVariable]] = None

class Reference(BaseModel):
    ref: str = Field(alias="$ref")

class Discriminator(BaseModel):
    propertyName: str
    mapping: Optional[Dict[str, str]] = None

class XML(BaseModelWithConfig):
    name: Optional[str] = None
    namespace: Optional[str] = None
    prefix: Optional[str] = None
    attribute: Optional[bool] = None
    wrapped: Optional[bool] = None

class ExternalDocumentation(BaseModelWithConfig):
    description: Optional[str] = None
    url: AnyUrl

class Schema(BaseModelWithConfig):
    schema_: Optional[str] = Field(default=None, alias="$schema")
    vocabulary: Optional[str] = Field(default=None, alias="$vocabulary")
    id: Optional[str] = Field(default=None, alias="$id")
    anchor: Optional[str] = Field(default=None, alias="$anchor")
    dynamicAnchor: Optional[str] = Field(default=None, alias="$dynamicAnchor")
    ref: Optional[str] = Field(default=None, alias="$ref")
    dynamicRef: Optional[str] = Field(default=None, alias="$dynamicRef")
    defs: Optional[Dict[str, "Schema"]] = Field(default=None, alias="$defs")
    comment: Optional[str] = Field(default=None, alias="$comment")
    allOf: Optional[List["SchemaOrBool"]] = None
    anyOf: Optional[List["SchemaOrBool"]] = None
    oneOf: Optional[List["SchemaOrBool"]] = None
    not_: Optional["SchemaOrBool"] = Field(default=None, alias="not")
    if_: Optional["SchemaOrBool"] = Field(default=None, alias="if")
    then: Optional["SchemaOrBool"] = None
    else_: Optional["SchemaOrBool"] = Field(default=None, alias="else")
    dependentSchemas: Optional[Dict[str, "SchemaOrBool"]] = None
    prefixItems: Optional[List["SchemaOrBool"]] = None
    items: Optional["SchemaOrBool"] = None
    contains: Optional["SchemaOrBool"] = None
    properties: Optional[Dict[str, "SchemaOrBool"]] = None
    patternProperties: Optional[Dict[str, "SchemaOrBool"]] = None
    additionalProperties: Optional["SchemaOrBool"] = None
    propertyNames: Optional["SchemaOrBool"] = None
    unevaluatedItems: Optional["SchemaOrBool"] = None
    unevaluatedProperties: Optional["SchemaOrBool"] = None
    type: Optional[str] = None
    enum: Optional[List[Any]] = None
    const: Optional[Any] = None
    multipleOf: Optional[float] = Field(default=None, gt=0)
    maximum: Optional[float] = None
    exclusiveMaximum: Optional[float] = None
    minimum: Optional[float] = None
    exclusiveMinimum: Optional[float] = None
    maxLength: Optional[int] = Field(default=None, ge=0)
    minLength: Optional[int] = Field(default=None, ge=0)
    pattern: Optional[str] = None
    maxItems: Optional[int] = Field(default=None, ge=0)
    minItems: Optional[int] = Field(default=None, ge=0)
    uniqueItems: Optional[bool] = None
    maxContains: Optional[int] = Field(default=None, ge=0)
    minContains: Optional[int] = Field(default=None, ge=0)
    maxProperties: Optional[int] = Field(default=None, ge=0)
    minProperties: Optional[int] = Field(default=None, ge=0)
    required: Optional[List[str]] = None
    dependentRequired: Optional[Dict[str, List[str]]] = None
    discriminator: Optional[Discriminator] = None
    xml: Optional[XML] = None
    externalDocs: Optional[ExternalDocumentation] = None
    example: Optional[Any] = None

SchemaOrBool = Union[Schema, bool]

class Example(TypedDict, total=False):
    summary: Optional[str]
    description: Optional[str]
    value: Optional[Any]
    externalValue: Optional[AnyUrl]

    if PYDANTIC_V2:  # type: ignore [misc]
        __pydantic_config__ = {"extra": "allow"}

    else:

        class Config:
            extra = "allow"


class ParameterInType(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"


class Encoding(BaseModelWithConfig):
    contentType: Optional[str] = None
    headers: Optional[Dict[str, Any]] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None


class MediaType(BaseModelWithConfig):
    schema_: Optional[Schema] = Field(default=None, alias="schema")
    example: Optional[Any] = None
    examples: Optional[Dict[str, Any]] = None
    encoding: Optional[Dict[str, Encoding]] = None


class ParameterBase(BaseModelWithConfig):
    description: Optional[str] = None
    required: Optional[bool] = None
    deprecated: Optional[bool] = None
    style: Optional[str] = None
    explode: Optional[bool] = None
    allowReserved: Optional[bool] = None
    schema_: Optional[Schema] = Field(default=None, alias="schema")
    example: Optional[Any] = None
    examples: Optional[Dict[str, Any]] = None
    content: Optional[Dict[str, MediaType]] = None


class Parameter(ParameterBase):
    name: str
    in_: ParameterInType = Field(alias="in")


class Header(ParameterBase):
    ...


class RequestBody(BaseModelWithConfig):
    description: Optional[str] = None
    content: Dict[str, MediaType]
    required: Optional[bool] = None


class Link(BaseModelWithConfig):
    operationRef: Optional[str] = None
    operationId: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    requestBody: Optional[Any] = None
    description: Optional[str] = None
    server: Optional[Server] = None


class Response(BaseModelWithConfig):
    description: str
    headers: Optional[Dict[str, Header]] = None
    content: Optional[Dict[str, MediaType]] = None
    links: Optional[Dict[str, Link]] = None


class Operation(BaseModelWithConfig):
    tags: Optional[List[str]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None
    operationId: Optional[str] = None
    parameters: Optional[List[Parameter]] = None
    requestBody: Optional[RequestBody] = None
    responses: Dict[str, Response]
    callbacks: Optional[Dict[str, Any]] = None
    deprecated: Optional[bool] = None
    security: Optional[List[Dict[str, List[str]]]] = None
    servers: Optional[List[Server]] = None


class PathItem(BaseModelWithConfig):
    ref: Optional[str] = Field(default=None, alias="$ref")
    summary: Optional[str] = None
    description: Optional[str] = None
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
    trace: Optional[Operation] = None
    servers: Optional[List[Server]] = None
    parameters: Optional[List[Parameter]] = None


class SecuritySchemeType(Enum):
    apiKey = "apiKey"
    http = "http"
    oauth2 = "oauth2"
    openIdConnect = "openIdConnect"


class SecurityBase(BaseModelWithConfig):
    type_: SecuritySchemeType = Field(alias="type")
    description: Optional[str] = None


class APIKeyIn(Enum):
    query = "query"
    header = "header"
    cookie = "cookie"


class APIKey(SecurityBase):
    type_: SecuritySchemeType = Field(default=SecuritySchemeType.apiKey, alias="type")
    in_: APIKeyIn = Field(alias="in")
    name: str


class HTTPBase(SecurityBase):
    type_: SecuritySchemeType = Field(default=SecuritySchemeType.http, alias="type")
    scheme: str


class HTTPBearer(HTTPBase):
    scheme: str = "bearer"
    bearerFormat: Optional[str] = None


class OAuthFlow(BaseModelWithConfig):
    refreshUrl: Optional[str] = None
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
    implicit: Optional[OAuthFlowImplicit] = None
    password: Optional[OAuthFlowPassword] = None
    clientCredentials: Optional[OAuthFlowClientCredentials] = None
    authorizationCode: Optional[OAuthFlowAuthorizationCode] = None


class OAuth2(SecurityBase):
    type_: SecuritySchemeType = Field(default=SecuritySchemeType.oauth2, alias="type")
    flows: OAuthFlows


class OpenIdConnect(SecurityBase):
    type_: SecuritySchemeType = Field(
        default=SecuritySchemeType.openIdConnect, alias="type"
    )
    openIdConnectUrl: str

SecurityScheme = Union[APIKey, HTTPBase, OAuth2, OpenIdConnect, HTTPBearer]

class Components(BaseModelWithConfig):
    schemas: Optional[Dict[str, Schema]] = None
    responses: Optional[Dict[str, Response]] = None
    parameters: Optional[Dict[str, Parameter]] = None
    examples: Optional[Dict[str, Any]] = None
    requestBodies: Optional[Dict[str, RequestBody]] = None
    headers: Optional[Dict[str, Header]] = None
    securitySchemes: Optional[Dict[str, SecurityScheme]] = None
    links: Optional[Dict[str, Link]] = None
    callbacks: Optional[Dict[str, Any]] = None
    pathItems: Optional[Dict[str, PathItem]] = None


class Tag(BaseModelWithConfig):
    name: str
    description: Optional[str] = None
    externalDocs: Optional[ExternalDocumentation] = None


class OpenAPI(BaseModelWithConfig):
    openapi: str
    info: Info
    jsonSchemaDialect: Optional[str] = None
    servers: Optional[List[Server]] = None
    paths: Optional[Dict[str, PathItem]] = None
    webhooks: Optional[Dict[str, PathItem]] = None
    components: Optional[Components] = None
    security: Optional[List[Dict[str, List[str]]]] = None
    tags: Optional[List[Tag]] = None
    externalDocs: Optional[ExternalDocumentation] = None