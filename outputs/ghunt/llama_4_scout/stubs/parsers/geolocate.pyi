from typing import Dict

from ghunt.objects.apis import Parser
from ghunt.objects.base import Position

class GeolocationResponse(Parser):
    def __init__(self) -> None:
        self.accuracy: int = 0
        self.location: Position = Position()

    def _scrape(self, base_model_data: Dict) -> None:
        ...