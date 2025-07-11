import pandas as pd
from .base import BaseResponse as BaseResponse
from typing import Any

class DataframeResponse(BaseResponse):
    def __init__(self, value: pd.DataFrame, **kwargs: Any) -> None: ...
    @property
    def value(self) -> pd.DataFrame: ...
