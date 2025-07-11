from .constants import LOCAL_SOURCE_TYPES as LOCAL_SOURCE_TYPES, SQL_SOURCE_TYPES as SQL_SOURCE_TYPES
from .data_loader.loader import DatasetLoader as DatasetLoader
from .dataframe import DataFrame, VirtualDataFrame
from .helpers.sql_sanitizer import sanitize_file_name as sanitize_file_name, sanitize_sql_table_name as sanitize_sql_table_name
from .smart_dataframe import SmartDataframe as SmartDataframe
from .smart_datalake import SmartDatalake as SmartDatalake
from io import BytesIO as BytesIO
from pandasai.config import APIKeyManager as APIKeyManager, ConfigManager as ConfigManager
from pandasai.data_loader.semantic_layer_schema import Relation as Relation, SemanticLayerSchema as SemanticLayerSchema, Source as Source, Transformation as Transformation, TransformationParams as TransformationParams
from pandasai.exceptions import DatasetNotFound as DatasetNotFound, InvalidConfigError as InvalidConfigError, PandasAIApiKeyError as PandasAIApiKeyError
from pandasai.helpers.path import find_project_root as find_project_root, get_validated_dataset_path as get_validated_dataset_path, transform_dash_to_underscore as transform_dash_to_underscore
from pandasai.helpers.session import get_PandasAI_session as get_PandasAI_session
from pandasai.query_builders import SqlQueryBuilder as SqlQueryBuilder
from pandasai.sandbox.sandbox import Sandbox as Sandbox
from typing import Any, List, Optional, Union
from zipfile import ZipFile as ZipFile

def create(path: str, df: Optional[DataFrame] = ..., description: Optional[str] = ..., columns: Optional[List[dict]] = ..., source: Optional[dict] = ..., relations: Optional[List[dict]] = ..., view: bool = ..., group_by: Optional[List[str]] = ..., transformations: Optional[List[dict]] = ...) -> Union[DataFrame, VirtualDataFrame]: ...

config: ConfigManager
api_key: APIKeyManager

def chat(query: str, *dataframes: DataFrame, sandbox: Optional[Sandbox] = ...) -> Any: ...
def follow_up(query: str) -> Any: ...
def load(dataset_path: str) -> DataFrame: ...
def read_csv(filepath: str) -> DataFrame: ...
