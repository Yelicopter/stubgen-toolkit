from typing import Any
from json import JSONEncoder

def convert_numpy_types(obj: Any) -> Any: ...

class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any: ...