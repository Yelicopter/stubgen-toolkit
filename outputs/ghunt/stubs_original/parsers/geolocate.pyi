from typing import *
from _typeshed import Incomplete
from ghunt.objects.apis import Parser as Parser
from ghunt.objects.base import Position as Position

class GeolocationResponse(Parser):
    accuracy: int
    location: Incomplete
    def __init__(self) -> None: ...
