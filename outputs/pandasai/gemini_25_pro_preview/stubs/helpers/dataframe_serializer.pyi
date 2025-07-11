from __future__ import annotations

from typing import TYPE_CHECKING, Type

import pandas as pd

if TYPE_CHECKING:
    from ..dataframe.base import DataFrame

class DataframeSerializer:
    MAX_COLUMN_TEXT_LENGTH: int
    @classmethod
    def serialize(cls: Type[DataframeSerializer], df: DataFrame, dialect: str = ...) -> str: ...
    @classmethod
    def _truncate_dataframe(
        cls: Type[DataframeSerializer], df: pd.DataFrame
    ) -> pd.DataFrame: ...