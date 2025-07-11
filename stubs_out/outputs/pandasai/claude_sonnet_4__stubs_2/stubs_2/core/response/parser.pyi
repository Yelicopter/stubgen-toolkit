from .base import BaseResponse as BaseResponse
from .chart import ChartResponse as ChartResponse
from .dataframe import DataFrameResponse as DataFrameResponse
from .number import NumberResponse as NumberResponse
from .string import StringResponse as StringResponse
from pandasai.exceptions import InvalidOutputValueMismatch as InvalidOutputValueMismatch
from typing import Any, Optional

class ResponseParser:
    def parse(self, result: Any, last_code_executed: Optional[str] = ...) -> BaseResponse: ...
