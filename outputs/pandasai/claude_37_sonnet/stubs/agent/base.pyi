from typing import Any, List, Optional, Union

import pandas as pd

from pandasai.core.code_execution.code_executor import CodeExecutor
from pandasai.core.code_generation.base import CodeGenerator
from pandasai.core.response.error import ErrorResponse
from pandasai.core.response.parser import ResponseParser
from pandasai.core.user_query import UserQuery
from pandasai.dataframe.base import DataFrame
from pandasai.dataframe.virtual_dataframe import VirtualDataFrame
from pandasai.exceptions import CodeExecutionError, InvalidLLMOutputType, MissingVectorStoreError
from pandasai.sandbox import Sandbox
from pandasai.vectorstores.vectorstore import VectorStore

from ..config import Config
from ..data_loader.duck_db_connection_manager import DuckDBConnectionManager
from ..query_builders.base_query_builder import BaseQueryBuilder
from ..query_builders.sql_parser import SQLParser
from .state import AgentState

class Agent:
    def __init__(
        self,
        dfs: Union[Union[DataFrame, VirtualDataFrame], List[Union[DataFrame, VirtualDataFrame]]],
        config: Optional[Union[Config, dict]] = None,
        memory_size: int = 10,
        vectorstore: Optional[VectorStore] = None,
        description: str = None,
        sandbox: Sandbox = None,
    ) -> None: ...
    
    def chat(self, query: str, output_type: Optional[str] = None) -> Any: ...
    
    def follow_up(self, query: str, output_type: Optional[str] = None) -> Any: ...
    
    def generate_code(self, query: Union[str, UserQuery]) -> str: ...
    
    def execute_code(self, code: str) -> Any: ...
    
    def _execute_sql_query(self, query: str) -> pd.DataFrame: ...
    
    def generate_code_with_retries(self, query: str) -> str: ...
    
    def execute_with_retries(self, code: str) -> Any: ...
    
    def train(
        self,
        queries: Optional[List[str]] = None,
        codes: Optional[List[str]] = None,
        docs: Optional[List[str]] = None,
    ) -> None: ...
    
    def clear_memory(self) -> None: ...
    
    def add_message(self, message, is_user=False) -> None: ...
    
    def start_new_conversation(self) -> None: ...
    
    def _process_query(self, query: str, output_type: Optional[str] = None) -> Any: ...
    
    def _regenerate_code_after_error(self, code: str, error: Exception) -> str: ...
    
    def _handle_exception(self, code: str) -> Any: ...
    
    @property
    def last_generated_code(self) -> str: ...
    
    @property
    def last_code_executed(self) -> str: ...
    
    @property
    def last_prompt_used(self) -> str: ...