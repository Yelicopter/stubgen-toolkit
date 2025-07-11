from _typeshed import Incomplete
from ghunt.objects.apis import Parser

class GeolocationResponse(Parser):
    accuracy: int
    location: Incomplete
    def __init__(self) -> None: ...
