from typing import Any, Dict, Optional
from pydantic import BaseModel

class Config(BaseModel):
    save_logs: bool
    verbose: bool
    max_retries: int
    llm: Optional[Any]
    file_manager: Any

    @classmethod
    def from_dict(cls, config: Dict[str, Any]) -> "Config": ...

class ConfigManager:
    _config: Config

    @classmethod
    def set(cls, config_dict: Dict[str, Any]) -> None: ...
    @classmethod
    def get(cls) -> Config: ...
    @classmethod
    def update(cls, config_dict: Dict[str, Any]) -> None: ...
    @classmethod
    def validate_llm(cls) -> None: ...

class APIKeyManager:
    _api_key: Optional[str]

    @classmethod
    def set(cls, api_key: str) -> None: ...
    @classmethod
    def get(cls) -> Optional[str]: ...