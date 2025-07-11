import json
from datetime import datetime as datetime
from typing import Any

class GHuntEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...
