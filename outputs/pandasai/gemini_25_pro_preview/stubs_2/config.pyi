from __future__ import annotations

from typing import Any, Dict, Optional, Type

from pydantic import BaseModel

from pandasai.helpers.filemanager import FileManager
from pandasai.llm.base import LLM

class Config(BaseModel):
    save_logs: bool
    verbose: bool
    max_retries: int
    llm: Optional[LLM]
    file_manager: FileManager
    @classmethod
    def from_dict(cls: Type[Config], config: Dict[str, Any]) -> Config: ...

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