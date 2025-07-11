from _typeshed import Incomplete
from starlette.background import BackgroundTasks as StarletteBackgroundTasks
from typing import Any, Callable

P: Incomplete

class BackgroundTasks(StarletteBackgroundTasks):
    def add_task(self, func: Callable[P, Any], *args: Any, **kwargs: Any) -> None: ...
