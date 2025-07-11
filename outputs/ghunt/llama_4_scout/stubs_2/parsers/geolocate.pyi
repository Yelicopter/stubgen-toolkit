from typing import Dict

class GeolocationResponse:
    def __init__(self) -> None:
        self.accuracy: int = 0
        self.location: Position = Position()

    def _scrape(self, base_model_data: Dict) -> None:
        ...