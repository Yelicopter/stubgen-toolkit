from typing import Any
from ghunt.objects.apis import Parser
from ghunt.objects.base import Position

class GeolocationResponse(Parser):
    accuracy: int
    location: Position
    def __init__(self) -> None: ...
    def _scrape(self, base_model_data: Any) -> None: ...