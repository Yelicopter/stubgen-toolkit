from typing import Any
from .base import BaseResponse
import pandas as pd

class DataframeResponse(BaseResponse):
    def __init__(self, value: pd.DataFrame, **kwargs: Any) -> None:
        ...
    @property
    def value(self) -> pd.DataFrame:
        ...
    def __str__(self) -> str:
        ...