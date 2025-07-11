from typing import Any, Callable, Dict, List, Optional, Union
import os
import pandas as pd

from pandasai.config import APIKeyManager, ConfigManager
from pandasai.constants import DEFAULT_API_URL
from pandasai.data_loader.semantic_layer_schema import (
    Column,
    Relation,
    SemanticLayerSchema,
    Source,
    Transformation,
    TransformationParams,
)
from pandasai.exceptions import DatasetNotFound, InvalidConfigError, PandasAIApiKeyError
from pandasai.helpers.path import (
    find_project_root,
    get_validated_dataset_path,
    transform_dash_to_underscore,
)
from pandasai.helpers.session import get_PandasAI_session
from pandasai.query_builders.sql_query_builder import SqlQueryBuilder
from pandasai.sandbox.sandbox import Sandbox

from .agent import Agent
from .constants import LOCAL_SOURCE_TYPES, SQL_SOURCE_TYPES
from .data_loader.loader import DatasetLoader
from .data_loader.semantic_layer_schema import (
    Column,
)
from .dataframe import DataFrame, VirtualDataFrame
from .helpers.sql_sanitizer import sanitize_file_name, sanitize_sql_table_name
from .smart_dataframe import SmartDataframe
from .smart_datalake import SmartDatalake

def create(
    path: str,
    df: Optional["DataFrame"] = ...,
    description: Optional[str] = ...,
    columns: Optional[List[dict]] = ...,
    source: Optional[dict] = ...,
    relations: Optional[dict] = ...,
    view: bool = ...,
    group_by: Optional[List[str]] = ...,
    transformations: Optional[List[dict]] = ...,
) -> Union["DataFrame", "VirtualDataFrame"]:
    ...

def chat(query: str, *dataframes: "DataFrame", sandbox: Optional[Sandbox] = ...) -> Any:
    ...

def follow_up(query: str) -> Any:
    ...

def load(dataset_path: str) -> "DataFrame":
    ...

def read_csv(filepath: str) -> "DataFrame":
    ...

config: ConfigManager
api_key: APIKeyManager

__all__: list
