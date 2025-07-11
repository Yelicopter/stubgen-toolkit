from importlib.util import find_spec as find_spec
from pandasai.helpers.filemanager import FileManager as FileManager
from pandasai.llm.base import LLM as LLM
from pydantic import BaseModel, ConfigDict as ConfigDict
from typing import Any, Dict, Optional

class Config(BaseModel):
    save_logs: bool
    verbose: bool
    max_retries: int
    llm: Optional[LLM]
    file_manager: FileManager
    model_config: ConfigDict
    @classmethod
    def from_dict(cls, config: Dict[str, Any]) -> Config: ...

class ConfigManager:
    @classmethod
    def set(cls, config_dict: Dict[str, Any]) -> None: ...
    @classmethod
    def get(cls) -> Config: ...
    @classmethod
    def update(cls, config_dict: Dict[str, Any]) -> None: ...
    @classmethod
    def validate_llm(cls) -> None: ...

class APIKeyManager:
    @classmethod
    def set(cls, api_key: str) -> None: ...
    @classmethod
    def get(cls) -> Optional[str]: ...
