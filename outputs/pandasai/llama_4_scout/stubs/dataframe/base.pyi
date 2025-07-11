from __future__ import annotations

import hashlib
import os
from io import BytesIO
from typing import TYPE_CHECKING, Optional, Union
from zipfile import ZipFile

import pandas as pd
from pandas._typing import Axes, Dtype

import pandasai as pai
from pandasai import get_validated_dataset_path
from pandasai.config import Config, ConfigManager
from pandasai.constants import LOCAL_SOURCE_TYPES
from pandasai.core.response import BaseResponse
from pandasai.data_loader.semantic_layer_schema import (
    Column,
    SemanticLayerSchema,
    Source,
)
from pandasai.exceptions import DatasetNotFound, PandasAIApiKeyError
from pandasai.helpers.dataframe_serializer import DataframeSerializer
from pandasai.helpers.session import get_PandasAI_session
from pandasai.sandbox.sandbox import Sandbox

if TYPE_CHECKING:
    from pandasai.agent.base import Agent

class DataFrame(pd.DataFrame):
    ...

    def __init__(
        self,
        data=None,
        index=None,
        columns=None,
        dtype=None,
        copy=None,
        **kwargs,
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def _calculate_column_hash(self) -> str:
        ...

    @property
    def column_hash(self) -> str:
        ...

    @property
    def type(self) -> str:
        ...

    def chat(self, prompt: str, sandbox: Optional[Sandbox] = None) -> str:
        ...

    def follow_up(self, query: str, output_type: Optional[str] = None) -> str:
        ...

    @property
    def rows_count(self) -> int:
        ...

    @property
    def columns_count(self) -> int:
        ...

    def serialize_dataframe(self) -> str:
        ...

    def get_head(self) -> pd.DataFrame:
        ...

    def push(self) -> None:
        ...

    def pull(self) -> None:
        ...

    @staticmethod
    def get_column_type(column_dtype) -> str:
        ...

    @classmethod
    def get_default_schema(cls, dataframe: pd.DataFrame) -> SemanticLayerSchema:
        ...