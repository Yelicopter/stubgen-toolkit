import datetime
from json import JSONEncoder

import numpy as np
import pandas as pd

def convert_numpy_types(obj: object) -> object | None:
    ...

class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: object) -> object:
        ...