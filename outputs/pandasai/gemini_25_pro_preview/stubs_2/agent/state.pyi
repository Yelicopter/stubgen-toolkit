from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union

from pandasai.config import Config
from pandasai.helpers.logger import Logger
from pandasai.helpers.memory import Memory
from pandasai.llm.base import LLM
from pandasai.vectorstores.vectorstore import VectorStore

if TYPE_CHECKING:
    from pandasai.dataframe.base import DataFrame
    from pandasai.dataframe.virtual_dataframe import VirtualDataFrame

class AgentState:
    dfs: List[Union[DataFrame, VirtualDataFrame]]
    _config: Optional[Config]
    memory: Memory
    vectorstore: Optional[VectorStore]
    intermediate_values: Dict[str, Any]
    logger: Optional[Logger]
    last_code_generated: Optional[str]
    last_code_executed: Optional[str]
    last_prompt_id: Optional[str]
    last_prompt_used: Optional[str]
    output_type: Optional[str]
    def __init__(
        self,
        dfs: List[Union[DataFrame, VirtualDataFrame]] = ...,
        _config: Dict[str, Any] = ...,
        memory: Memory = ...,
        vectorstore: Optional[VectorStore] = ...,
        intermediate_values: Dict[str, Any] = ...,
        logger: Optional[Logger] = ...,
        last_code_generated: Optional[str] = ...,
        last_code_executed: Optional[str] = ...,
        last_prompt_id: Optional[str] = ...,
        last_prompt_used: Optional[str] = ...,
        output_type: Optional[str] = ...,
    ) -> None: ...
    def __post_init__(self) -> None: ...
    def initialize(
        self,
        dfs: Union[Union[DataFrame, VirtualDataFrame], List[Union[DataFrame, VirtualDataFrame]]],
        config: Optional[Union[Config, Dict[str, Any]]] = ...,
        memory_size: int = ...,
        vectorstore: Optional[VectorStore] = ...,
        description: Optional[str] = ...,
    ) -> None: ...
    def _configure(self) -> None: ...
    def _get_config(self, config: Optional[Union[Config, Dict[str, Any]]]) -> Config: ...
    def _get_llm(self, llm: Optional[LLM] = ...) -> LLM: ...
    def assign_prompt_id(self) -> None: ...
    def reset_intermediate_values(self) -> None: ...
    def add(self, key: str, value: Any) -> None: ...
    def add_many(self, values: Dict[str, Any]) -> None: ...
    def get(self, key: str, default: Any = ...) -> Any: ...
    @property
    def config(self) -> Config: ...
    @config.setter
    def config(self, value: Union[Config, Dict[str, Any]]) -> None: ...