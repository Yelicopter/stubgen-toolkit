from typing import Any, Optional
import pandas as pd
from .base import BaseResponse

class DataFrameResponse(BaseResponse):
    def __init__(self, value: Any = None, last_code_executed: Optional[str] = None): ...
    def format_value(self, value: Any) -> pd.DataFrame: ...