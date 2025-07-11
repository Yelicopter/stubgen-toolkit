from enum import Enum
from pydantic import AnyUrl as AnyUrl, BaseModel, Field as Field
from typing import Any, Dict, Optional, Union

class EmailStr(str):
    @classmethod
    def __get_validators__(cls) -> Any: ...
    @classmethod
    def validate(cls, v: Any) -> str: ...
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: Any, handler: Any) -> Any: ...
    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: Any) -> Any: ...

class BaseModelWithConfig(BaseModel): ...

class Contact(BaseModelWithConfig):
    name: Any
    url: Any
    email: Any

class License(BaseModelWithConfig):
    name: str
    identifier: Any
    url: Any

class Info(BaseModelWithConfig):
    title: str
    summary: Any
    description: Any
    termsOfService: Any
    contact: Any
    license: Any
    version: str

class ServerVariable(BaseModelWithConfig):
    enum: Any
    default: str
    description: Any

class Server(BaseModelWithConfig):
    url: Union[AnyUrl, str]
    description: Any
    variables: Any

class Reference(BaseModel):
    ref: Any

class Discriminator(BaseModel):
    propertyName: str
    mapping: Any

class XML(BaseModelWithConfig):
    name: Any
    namespace: Any
    prefix: Any
    attribute: Any
    wrapped: Any

class ExternalDocumentation(BaseModelWithConfig):
    description: Any
    url: AnyUrl

class Schema(BaseModelWithConfig):
    schema_: Any
    vocabulary: Any
    id: Any
    anchor: Any
    dynamicAnchor: Any
    ref: Any
    dynamicRef: Any
    defs: Any
    comment: Any
    allOf: Any
    anyOf: Any
    oneOf: Any
    not_: Any
    if_: Any
    then: Any
    else_: Any
    dependentSchemas: Any
    prefixItems: Any
    items: Any
    contains: Any
    properties: Any
    patternProperties: Any
    additionalProperties: Any
    propertyNames: Any
    unevaluatedItems: Any
    unevaluatedProperties: Any
    type: Any
    enum: Any
    const: Any
    multipleOf: Any
    maximum: Any
    exclusiveMaximum: Any
    minimum: Any
    exclusiveMinimum: Any
    maxLength: Any
    minLength: Any
    pattern: Any
    maxItems: Any
    minItems: Any
    uniqueItems: Any
    maxContains: Any
    minContains: Any
    maxProperties: Any
    minProperties: Any
    required: Any
    dependentRequired: Any
    format: Any
    contentEncoding: Any
    contentMediaType: Any
    contentSchema: Any
    title: Any
    description: Any
    default: Any
    deprecated: Any
    readOnly: Any
    writeOnly: Any
    examples: Any
    discriminator: Any
    xml: Any
    externalDocs: Any
    example: Any
SchemaOrBool = Union[Schema, bool]

class Example(Dict[str, Any], total=False):
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
    contentType: Any
    headers: Any
    style: Any
    explode: Any
    allowReserved: Any

class MediaType(BaseModelWithConfig):
    schema_: Any
    example: Any
    examples: Any
    encoding: Any

class ParameterBase(BaseModelWithConfig):
    description: Any
    required: Any
    deprecated: Any
    style: Any
    explode: Any
    allowReserved: Any
    schema_: Any
    example: Any
    examples: Any
    content: Any

class Parameter(ParameterBase):
    name: str
    in_: Any

class Header(ParameterBase): ...

class RequestBody(BaseModelWithConfig):
    description: Any
    content: Dict[str, MediaType]
    required: Any

class Link(BaseModelWithConfig):
    operationRef: Any
    operationId: Any
    parameters: Any
    requestBody: Any
    description: Any
    server: Any

class Response(BaseModelWithConfig):
    description: str
    headers: Any
    content: Any
    links: Any

class Operation(BaseModelWithConfig):
    tags: Any
    summary: Any
    description: Any
    externalDocs: Any
    operationId: Any
    parameters: Any
    requestBody: Any
    responses: Any
    callbacks: Any
    deprecated: Any
    security: Any
    servers: Any

class PathItem(BaseModelWithConfig):
    ref: Any
    summary: Any
    description: Any
    get: Any
    put: Any
    post: Any
    delete: Any
    options: Any
    head: Any
    patch: Any
    trace: Any
    servers: Any
    parameters: Any

class SecuritySchemeType(Enum):
    apiKey: str
    http: str
    oauth2: str
    openIdConnect: str

class SecurityBase(BaseModelWithConfig):
    type_: Any
    description: Any

class APIKeyIn(Enum):
    query: str
    header: str
    cookie: str

class APIKey(SecurityBase):
    type_: Any
    in_: Any
    name: str

class HTTPBase(SecurityBase):
    type_: Any
    scheme: str

class HTTPBearer(HTTPBase):
    scheme: str
    bearerFormat: Any

class OAuthFlow(BaseModelWithConfig):
    refreshUrl: Any
    scopes: Any

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
    implicit: Any
    password: Any
    clientCredentials: Any
    authorizationCode: Any

class OAuth2(SecurityBase):
    type_: Any
    flows: OAuthFlows

class OpenIdConnect(SecurityBase):
    type_: Any
    openIdConnectUrl: str
SecurityScheme = Union[APIKey, HTTPBase, OAuth2, OpenIdConnect, HTTPBearer]

class Components(BaseModelWithConfig):
    schemas: Any
    responses: Any
    parameters: Any
    examples: Any
    requestBodies: Any
    headers: Any
    securitySchemes: Any
    links: Any
    callbacks: Any
    pathItems: Any

class Tag(BaseModelWithConfig):
    name: str
    description: Any
    externalDocs: Any

class OpenAPI(BaseModelWithConfig):
    openapi: str
    info: Info
    jsonSchemaDialect: Any
    servers: Any
    paths: Any
    webhooks: Any
    components: Any
    security: Any
    tags: Any
    externalDocs: Any
