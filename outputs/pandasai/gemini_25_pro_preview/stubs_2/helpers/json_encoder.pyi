from json import JSONEncoder
from typing import Any

def convert_numpy_types(obj: Any) -> Any: ...

class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any: ...