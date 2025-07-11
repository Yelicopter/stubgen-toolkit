import uuid
import warnings
from typing import Any, Dict, List, Optional, Union

import pandas as pd

from pandasai.agent.base import Agent
from pandasai.dataframe.base import DataFrame

from ..config import Config

class SmartDatalake:
    _agent: Agent
    
    def __init__(
        self,
        dfs: List[Any],
        config: Optional[Union[Config, Dict[str, Any]]] = None,
    ) -> None: ...
    
    def load_dfs(self, dfs: List[Any]) -> List[DataFrame]: ...
    
    def chat(self, query: str, output_type: Optional[str] = None) -> Any: ...
    
    def clear_memory(self) -> None: ...
    
    @property
    def last_prompt(self) -> Any: ...
    
    @property
    def last_prompt_id(self) -> Optional[str]: ...
    
    @property
    def logs(self) -> Any: ...
    
    @property
    def logger(self) -> Any: ...
    
    @logger.setter
    def logger(self, logger) -> None: ...
    
    @property
    def config(self) -> Any: ...
    
    @property
    def verbose(self) -> bool: ...
    
    @verbose.setter
    def verbose(self, verbose: bool) -> None: ...
    
    @property
    def save_logs(self) -> bool: ...
    
    @save_logs.setter
    def save_logs(self, save_logs: bool) -> None: ...
    
    @property
    def custom_prompts(self) -> Any: ...
    
    @custom_prompts.setter
    def custom_prompts(self, custom_prompts: Dict) -> None: ...
    
    @property
    def save_charts(self) -> bool: ...
    
    @save_charts.setter
    def save_charts(self, save_charts: bool) -> None: ...
    
    @property
    def save_charts_path(self) -> str: ...
    
    @save_charts_path.setter
    def save_charts_path(self, save_charts_path: str) -> None: ...
    
    @property
    def last_code_generated(self) -> Any: ...
    
    @property
    def last_code_executed(self) -> Any: ...
    
    @property
    def last_result(self) -> Any: ...
    
    @property
    def last_error(self) -> Any: ...
    
    @property
    def dfs(self) -> List[DataFrame]: ...
    
    @property
    def memory(self) -> Any: ...