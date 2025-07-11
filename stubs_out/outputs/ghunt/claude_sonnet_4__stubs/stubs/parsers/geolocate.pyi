from typing import *
from ghunt.objects.apis import Parser
from ghunt.objects.base import Position as Position

class GeolocationResponse(Parser):
    def __init__(self) -> None: ...
    accuracy: int
    location: Position
