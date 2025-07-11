import json

class GHuntEncoder(json.JSONEncoder):
    def default(self, o: object) -> dict: ...
