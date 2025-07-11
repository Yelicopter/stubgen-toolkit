from json import JSONEncoder
from typing import Any, Dict, List, Optional, Union

def convert_numpy_types(obj: Any) -> Optional[Union[int, float, List, Dict]]: ...

class CustomJsonEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any: ...
