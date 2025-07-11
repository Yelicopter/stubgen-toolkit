from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Type, Union

import pandas as pd
from pandas._typing import Axes, Dtype

from pandasai.core.response import BaseResponse
from pandasai.data_loader.semantic_layer_schema import SemanticLayerSchema
from pandasai.sandbox.sandbox import Sandbox

if TYPE_CHECKING:
    from pandasai.agent.base import Agent

class DataFrame(pd.DataFrame):
    _metadata: list[str]
    _agent: Optional[Agent]
    _column_hash: str
    _table_name: Optional[str]
    config: Any
    path: Optional[str]
    schema: SemanticLayerSchema
    def __init__(
        self,
        data: Any = ...,
        index: Optional[Axes] = ...,
        columns: Optional[Axes] = ...,
        dtype: Optional[Dtype] = ...,
        copy: Optional[bool] = ...,
        **kwargs: Any,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def _calculate_column_hash(self) -> str: ...
    @property
    def column_hash(self) -> str: ...
    @property
    def type(self) -> str: ...
    def chat(self, prompt: str, sandbox: Optional[Sandbox] = ...) -> BaseResponse: ...
    def follow_up(self, query: str, output_type: Optional[str] = ...) -> BaseResponse: ...
    @property
    def rows_count(self) -> int: ...
    @property
    def columns_count(self) -> int: ...
    def serialize_dataframe(self) -> str: ...
    def get_head(self) -> pd.DataFrame: ...
    def push(self) -> None: ...
    def pull(self) -> None: ...
    @staticmethod
    def get_column_type(column_dtype: Any) -> Optional[str]: ...
    @classmethod
    def get_default_schema(
        cls: Type[DataFrame], dataframe: DataFrame
    ) -> SemanticLayerSchema: ...