from ghunt.objects.apis import Parser
from ghunt.objects.base import Position
from typing import *

class GeolocationResponse(Parser):
    def __init__(self) -> None: ...
    accuracy: int
    location: Position
    
    def _scrape(self, base_model_data: Dict[str, Any]) -> None: ...