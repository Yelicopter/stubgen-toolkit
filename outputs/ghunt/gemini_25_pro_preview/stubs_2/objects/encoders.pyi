import json
from typing import Any

class GHuntEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...