import re
from typing import Any, Dict, Optional, Union

import numpy as np
import pandas as pd

from pandasai.exceptions import InvalidOutputValueMismatch

from .base import BaseResponse
from .chart import ChartResponse
from .dataframe import DataFrameResponse
from .number import NumberResponse
from .string import StringResponse

class ResponseParser:
    def parse(self, result: Dict[str, Any], last_code_executed: Optional[str] = None) -> BaseResponse: ...
    
    def _generate_response(self, result: Dict[str, Any], last_code_executed: Optional[str] = None) -> BaseResponse: ...
    
    def _validate_response(self, result: Dict[str, Any]) -> bool: ...