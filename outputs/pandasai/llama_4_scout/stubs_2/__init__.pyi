from typing import Any, List, Optional, Union

from pandasai.agent import Agent
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
from pandasai.dataframe import DataFrame, VirtualDataFrame
from pandasai.exceptions import (
    DatasetNotFound,
    InvalidConfigError,
    PandasAIApiKeyError,
)
from pandasai.helpers.path import find_project_root, get_validated_dataset_path
from pandasai.query_builders import SqlQueryBuilder
from pandasai.sandbox import Sandbox
from .data_loader import DatasetLoader

def create(
    path: str,
    df: Optional[DataFrame] = None,
    description: Optional[str] = None,
    columns: Optional[List[dict]] = None,
    source: Optional[dict] = None,
    relations: Optional[dict] = None,
    view: bool = False,
    group_by: Optional[List[str]] = None,
    transformations: Optional[List[dict]] = None,
) -> Union[DataFrame, VirtualDataFrame]:
    ...

def chat(
    query: str, 
    *dataframes, 
    sandbox: Optional[Sandbox] = None
) -> Any:
    ...

def follow_up(query: str) -> Any:
    ...

def load(dataset_path: str) -> DataFrame:
    ...

def read_csv(filepath: str) -> DataFrame:
    ...