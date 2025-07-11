from .data_loader.loader import DatasetLoader as DatasetLoader
from pandasai.agent import Agent as Agent
from pandasai.config import APIKeyManager as APIKeyManager, ConfigManager as ConfigManager
from pandasai.constants import DEFAULT_API_URL as DEFAULT_API_URL
from pandasai.data_loader.semantic_layer_schema import Column as Column, Relation as Relation, SemanticLayerSchema as SemanticLayerSchema, Source as Source, Transformation as Transformation, TransformationParams as TransformationParams
from pandasai.dataframe import DataFrame as DataFrame, VirtualDataFrame as VirtualDataFrame
from pandasai.exceptions import DatasetNotFound as DatasetNotFound, InvalidConfigError as InvalidConfigError, PandasAIApiKeyError as PandasAIApiKeyError
from pandasai.helpers.path import find_project_root as find_project_root, get_validated_dataset_path as get_validated_dataset_path
from pandasai.query_builders import SqlQueryBuilder as SqlQueryBuilder
from pandasai.sandbox.sandbox import Sandbox as Sandbox
from typing import Any, List, Optional, Union

def create(path: str, df: Optional[DataFrame] = ..., description: Optional[str] = ..., columns: Optional[List[dict]] = ..., source: Optional[dict] = ..., relations: Optional[dict] = ..., view: bool = ..., group_by: Optional[List[str]] = ..., transformations: Optional[List[dict]] = ...) -> Union[DataFrame, VirtualDataFrame]: ...
def chat(query: str, *dataframes, sandbox: Optional[Sandbox] = ...) -> Any: ...
def follow_up(query: str) -> Any: ...
def load(dataset_path: str) -> DataFrame: ...
def read_csv(filepath: str) -> DataFrame: ...
