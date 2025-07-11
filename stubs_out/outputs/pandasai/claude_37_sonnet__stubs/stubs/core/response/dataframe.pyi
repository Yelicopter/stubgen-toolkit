import pandas as pd
from .base import BaseResponse as BaseResponse
from typing import Any, Dict, Union

class DataFrameResponse(BaseResponse):
    def __init__(self, value: Any = ..., last_code_executed: str = ...) -> None: ...
    def format_value(self, value: Union[Dict[str, Any], pd.DataFrame]) -> pd.DataFrame: ...
