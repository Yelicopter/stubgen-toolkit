from typing import Any, Dict, Optional, Union

import pandas as pd

from .base import BaseResponse

class DataFrameResponse(BaseResponse):
    def __init__(self, value: Any = None, last_code_executed: str = None) -> None: ...
    
    def format_value(self, value: Union[Dict[str, Any], pd.DataFrame]) -> pd.DataFrame: ...