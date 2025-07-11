import pandas as pd
from .base import BaseResponse as BaseResponse
from typing import Any, Optional

class DataFrameResponse(BaseResponse):
    def __init__(self, value: Any = ..., last_code_executed: Optional[str] = ...) -> None: ...
    def format_value(self, value: Any) -> pd.DataFrame: ...
