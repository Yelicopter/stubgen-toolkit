import abc
from abc import ABC, abstractmethod
from typing import Optional, TypedDict

class InvalidProxyConfig(Exception): ...

class RequestsProxyConfigDict(TypedDict):
    http: str
    https: str

class ProxyConfig(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def to_requests_dict(self) -> RequestsProxyConfigDict: ...
    @property
    def prevent_keeping_connections_alive(self) -> bool: ...
    @property
    def retries_when_blocked(self) -> int: ...

class GenericProxyConfig(ProxyConfig):
    http_url: Optional[str]
    https_url: Optional[str]
    def __init__(self, http_url: Optional[str] = ..., https_url: Optional[str] = ...) -> None: ...
    def to_requests_dict(self) -> RequestsProxyConfigDict: ...

class WebshareProxyConfig(GenericProxyConfig):
    DEFAULT_DOMAIN_NAME: str
    DEFAULT_PORT: int
    proxy_username: str
    proxy_password: str
    domain_name: str
    proxy_port: int
    def __init__(self, proxy_username: str, proxy_password: str, retries_when_blocked: int = ..., domain_name: str = ..., proxy_port: int = ...) -> None: ...
    @property
    def url(self) -> str: ...
    @property
    def http_url(self) -> str: ...
    @property
    def https_url(self) -> str: ...
    @property
    def prevent_keeping_connections_alive(self) -> bool: ...
    @property
    def retries_when_blocked(self) -> int: ...
