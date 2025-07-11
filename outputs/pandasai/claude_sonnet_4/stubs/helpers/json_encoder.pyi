import datetime
from json import JSONEncoder
import numpy as np
import pandas as pd

def convert_numpy_types(obj: any) -> any: ...

class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: any) -> any: ...