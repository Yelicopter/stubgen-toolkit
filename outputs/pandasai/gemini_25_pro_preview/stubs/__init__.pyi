from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

import pandas as pd

from .agent import Agent
from .config import APIKeyManager, ConfigManager
from .dataframe import DataFrame, VirtualDataFrame
from .sandbox import Sandbox
from .smart_dataframe import SmartDataframe
from .smart_datalake import SmartDatalake

def create(
    path: str,
    df: Optional[DataFrame] = ...,
    description: Optional[str] = ...,
    columns: Optional[List[Dict[str, Any]]] = ...,
    source: Optional[Dict[str, Any]] = ...,
    relations: Optional[List[Dict[str, Any]]] = ...,
    view: bool = ...,
    group_by: Optional[List[str]] = ...,
    transformations: Optional[List[Dict[str, Any]]] = ...,
) -> Union[DataFrame, VirtualDataFrame]: ...

_current_agent: Optional[Agent]
config: ConfigManager
api_key: APIKeyManager

def chat(query: str, *dataframes: Union[DataFrame, VirtualDataFrame], sandbox: Optional[Sandbox] = ...) -> Any: ...
def follow_up(query: str) -> Any: ...
def load(dataset_path: str) -> DataFrame: ...
def read_csv(filepath: str) -> DataFrame: ...

__all__: list[str]