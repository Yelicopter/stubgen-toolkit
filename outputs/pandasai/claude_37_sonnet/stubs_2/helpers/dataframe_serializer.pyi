import json
import typing
from typing import Any, Dict

import pandas as pd

if typing.TYPE_CHECKING:
    from ..dataframe.base import DataFrame

class DataframeSerializer:
    MAX_COLUMN_TEXT_LENGTH: int = 200
    
    @classmethod
    def serialize(cls, df: 'DataFrame', dialect: str = "postgres") -> str: ...
    
    @classmethod
    def _truncate_dataframe(cls, df: 'DataFrame') -> pd.DataFrame: ...