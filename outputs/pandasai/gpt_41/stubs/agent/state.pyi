from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field

from pandasai.config import Config, ConfigManager
from pandasai.vectorstores.vectorstore import VectorStore

@dataclass
class AgentState:
    dfs: Any
    _config: Any
    memory: Any
    vectorstore: Optional[VectorStore]
    intermediate_values: dict
    logger: Any
    last_code_generated: Any
    last_code_executed: Any
    last_prompt_id: Any
    last_prompt_used: Any
    output_type: Any

    def __post_init__(self) -> None: ...
    def initialize(
        self,
        dfs: Any,
        config: Optional[Union[Config, dict]] = ...,
        memory_size: int = ...,
        vectorstore: Optional[VectorStore] = ...,
        description: Optional[str] = ...,
    ) -> None: ...
    def _configure(self) -> None: ...
    def _get_config(self, config: Optional[Union[Config, dict]]) -> Config: ...
    def _get_llm(self, llm: Optional[Any] = ...) -> Any: ...
    def assign_prompt_id(self) -> None: ...
    def reset_intermediate_values(self) -> None: ...
    def add(self, key: str, value: Any) -> None: ...
    def add_many(self, values: dict) -> None: ...
    def get(self, key: str, default: Any = ...) -> Any: ...
    @property
    def config(self) -> Config: ...
    @config.setter
    def config(self, value: Union[Config, dict]) -> None: ...