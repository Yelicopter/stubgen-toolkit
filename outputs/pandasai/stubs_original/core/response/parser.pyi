from .base import BaseResponse as BaseResponse
from .chart import ChartResponse as ChartResponse
from .dataframe import DataFrameResponse as DataFrameResponse
from .number import NumberResponse as NumberResponse
from .string import StringResponse as StringResponse
from pandasai.exceptions import InvalidOutputValueMismatch as InvalidOutputValueMismatch

class ResponseParser:
    def parse(self, result: dict, last_code_executed: str = ...) -> BaseResponse: ...
