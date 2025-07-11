from ghunt.objects.apis import Parser
from ghunt.objects.base import Position
from typing import *

class GeolocationResponse(Parser):
    accuracy: int
    location: Position
    
    def __init__(self) -> None: ...
    def _scrape(self, base_model_data: Dict[str, Any]) -> None: ...