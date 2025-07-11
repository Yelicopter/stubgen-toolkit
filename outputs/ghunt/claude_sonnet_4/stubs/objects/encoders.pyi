import json
from datetime import datetime

class GHuntEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any: ...