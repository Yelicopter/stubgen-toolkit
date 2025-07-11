from typing import Any, Dict, List, Optional, Union
from io import BytesIO
from zipfile import ZipFile

import pandas as pd

from pandasai.config import APIKeyManager, ConfigManager
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

from .agent.base import Agent
from .constants import LOCAL_SOURCE_TYPES, SQL_SOURCE_TYPES
from .data_loader.loader import DatasetLoader
from .data_loader.semantic_layer_schema import Column
from .dataframe.base import DataFrame
from .dataframe.virtual_dataframe import VirtualDataFrame
from .helpers.sql_sanitizer import sanitize_file_name, sanitize_sql_table_name
from .smart_dataframe import SmartDataframe
from .smart_datalake import SmartDatalake

def create(
    path: str,
    df: Optional[DataFrame] = None,
    description: Optional[str] = None,
    columns: Optional[List[dict]] = None,
    source: Optional[dict] = None,
    relations: Optional[List[dict]] = None,
    view: bool = False,
    group_by: Optional[List[str]] = None,
    transformations: Optional[List[dict]] = None,
) -> Union[DataFrame, VirtualDataFrame]: ...

_current_agent: Optional[Agent] = None

config: ConfigManager

api_key: APIKeyManager

def chat(query: str, *dataframes: DataFrame, sandbox: Optional[Sandbox] = None) -> Any: ...

def follow_up(query: str) -> Any: ...

def load(dataset_path: str) -> DataFrame: ...

def read_csv(filepath: str) -> DataFrame: ...

__all__: List[str]