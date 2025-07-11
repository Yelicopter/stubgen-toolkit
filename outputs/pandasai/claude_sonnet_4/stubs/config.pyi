import os
from importlib.util import find_spec
from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict
from pandasai.helpers.filemanager import DefaultFileManager, FileManager
from pandasai.llm.base import LLM

class Config(BaseModel):
    save_logs: bool = True
    verbose: bool = False
    max_retries: int = 3
    llm: Optional[LLM] = None
    file_manager: FileManager = DefaultFileManager()
    
    model_config: ConfigDict
    
    @classmethod
    def from_dict(cls, config: Dict[str, Any]) -> Config: ...

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