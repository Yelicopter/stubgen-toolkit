import datetime
from json import JSONEncoder
from typing import Any
import numpy as np
import pandas as pd

def convert_numpy_types(obj: Any) -> Any: ...

class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any: ...