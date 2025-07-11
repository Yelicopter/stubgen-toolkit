from pandasai.config import Config as Config, ConfigManager as ConfigManager
from pandasai.constants import DEFAULT_CHART_DIRECTORY as DEFAULT_CHART_DIRECTORY
from pandasai.data_loader.semantic_layer_schema import is_schema_source_same as is_schema_source_same
from pandasai.dataframe import DataFrame as DataFrame, VirtualDataFrame as VirtualDataFrame
from pandasai.exceptions import InvalidConfigError as InvalidConfigError
from pandasai.helpers.folder import Folder as Folder
from pandasai.helpers.logger import Logger as Logger
from pandasai.helpers.memory import Memory
from pandasai.llm.bamboo_llm import BambooLLM as BambooLLM
from pandasai.llm.base import LLM as LLM
from pandasai.vectorstores.vectorstore import VectorStore as VectorStore
from typing import Any, Dict, List, Optional, Union

class AgentState:
    dfs: List[Union[DataFrame, VirtualDataFrame]]
    memory: Memory
    vectorstore: Optional[VectorStore]
    intermediate_values: Dict[str, Any]
    logger: Optional[Logger]
    last_code_generated: Optional[str]
    last_code_executed: Optional[str]
    last_prompt_id: Optional[str]
    last_prompt_used: Optional[str]
    output_type: Optional[str]
    def initialize(self, dfs: Union[Union[DataFrame, VirtualDataFrame], List[Union[DataFrame, VirtualDataFrame]]], config: Optional[Union[Config, dict]] = ..., memory_size: int = ..., vectorstore: Optional[VectorStore] = ..., description: str = ...) -> None: ...
    def assign_prompt_id(self) -> None: ...
    def reset_intermediate_values(self) -> None: ...
    def add(self, key: str, value: Any) -> None: ...
    def add_many(self, values: Dict[str, Any]) -> None: ...
    def get(self, key: str, default: Any = ...) -> Any: ...
    @property
    def config(self) -> Config: ...
    def __init__(self, dfs, _config, memory, vectorstore, intermediate_values, logger, last_code_generated, last_code_executed, last_prompt_id, last_prompt_used, output_type) -> None: ...
