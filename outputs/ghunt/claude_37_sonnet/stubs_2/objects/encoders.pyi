import json
from datetime import datetime
from typing import Any

class GHuntEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...