from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, ClassVar, Dict, List, Optional, Union

from pandasai.config import Config, ConfigManager
from pandasai.constants import DEFAULT_CHART_DIRECTORY
from pandasai.data_loader.semantic_layer_schema import is_schema_source_same
from pandasai.exceptions import InvalidConfigError
from pandasai.helpers.folder import Folder
from pandasai.helpers.logger import Logger
from pandasai.helpers.memory import Memory
from pandasai.llm.bamboo_llm.base import BambooLLM
from pandasai.vectorstores.vectorstore import VectorStore

from pandasai.dataframe.base import DataFrame
from pandasai.dataframe.virtual_dataframe import VirtualDataFrame
from pandasai.llm.base import LLM

@dataclass
class AgentState:
    dfs: List[Union[DataFrame, VirtualDataFrame]] = field(default_factory=list)
    _config: Union[Config, dict] = field(default_factory=dict)
    memory: Memory = field(default_factory=Memory)
    vectorstore: Optional[VectorStore] = None
    intermediate_values: Dict[str, Any] = field(default_factory=dict)
    logger: Optional[Logger] = None
    last_code_generated: Optional[str] = None
    last_code_executed: Optional[str] = None
    last_prompt_id: Optional[str] = None
    last_prompt_used: Optional[str] = None
    output_type: Optional[str] = None
    
    def initialize(
        self,
        dfs: Union[Union[DataFrame, VirtualDataFrame], List[Union[DataFrame, VirtualDataFrame]]],
        config: Optional[Union[Config, dict]] = None,
        memory_size: int = 10,
        vectorstore: Optional[VectorStore] = None,
        description: Optional[str] = None,
    ) -> None: ...
    
    def _configure(self) -> None: ...
    
    def _get_config(self, config: Optional[Union[Config, dict]]) -> Config: ...
    
    def _get_llm(self, llm: Optional[LLM] = None) -> LLM: ...
    
    def assign_prompt_id(self) -> None: ...
    
    def reset_intermediate_values(self) -> None: ...
    
    def add(self, key: str, value: Any) -> None: ...
    
    def add_many(self, values: Dict[str, Any]) -> None: ...
    
    def get(self, key: str, default: Any = "") -> Any: ...
    
    @property
    def config(self) -> Config: ...
    
    @config.setter
    def config(self, value: Union[Config, dict]) -> None: ...