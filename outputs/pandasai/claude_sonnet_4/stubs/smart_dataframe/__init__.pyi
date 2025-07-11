import uuid
import warnings
from functools import cached_property
from io import StringIO
from typing import Any, List, Optional, Union
import pandas as pd
from pandasai.agent import Agent
from pandasai.dataframe.base import DataFrame
from ..config import Config
from ..helpers.logger import Logger

class SmartDataframe:
    _table_name: str
    _table_description: str
    _custom_head: Optional[str] = None
    _original_import: any
    
    def __init__(
        self,
        df: pd.DataFrame,
        name: Optional[str] = None,
        description: Optional[str] = None,
        custom_head: Optional[pd.DataFrame] = None,
        config: Optional[Config] = None,
    ): ...
    
    def load_df(self, df: any, name: str, description: str, custom_head: Optional[pd.DataFrame]) -> DataFrame: ...
    def chat(self, query: str, output_type: Optional[str] = None) -> any: ...
    
    @cached_property
    def head_df(self) -> pd.DataFrame: ...
    
    @cached_property
    def head_csv(self) -> str: ...
    
    @property
    def last_prompt(self) -> any: ...
    
    @property
    def last_prompt_id(self) -> Optional[str]: ...
    
    @property
    def last_code_generated(self) -> any: ...
    
    @property
    def last_code_executed(self) -> any: ...
    
    def original_import(self) -> any: ...
    
    @property
    def logger(self) -> Logger: ...
    
    @logger.setter
    def logger(self, logger: Logger) -> None: ...
    
    @property
    def logs(self) -> any: ...
    
    @property
    def verbose(self) -> bool: ...
    
    @verbose.setter
    def verbose(self, verbose: bool) -> None: ...
    
    @property
    def save_logs(self) -> bool: ...
    
    @save_logs.setter
    def save_logs(self, save_logs: bool) -> None: ...
    
    @property
    def save_charts(self) -> bool: ...
    
    @save_charts.setter
    def save_charts(self, save_charts: bool) -> None: ...
    
    @property
    def save_charts_path(self) -> str: ...
    
    @save_charts_path.setter
    def save_charts_path(self, save_charts_path: str) -> None: ...
    
    @property
    def table_name(self) -> str: ...
    
    @property
    def table_description(self) -> str: ...
    
    @property
    def custom_head(self) -> pd.DataFrame: ...
    
    def __len__(self) -> int: ...
    def __eq__(self, other: SmartDataframe) -> bool: ...
    def __getattr__(self, name: str) -> any: ...
    def __getitem__(self, key: any) -> any: ...
    def __setitem__(self, key: any, value: any) -> any: ...

def load_smartdataframes(
    dfs: List[Union[pd.DataFrame, Any]], config: Config
) -> List[SmartDataframe]: ...