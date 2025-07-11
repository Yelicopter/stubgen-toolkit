from _typeshed import Incomplete
from starlette.background import BackgroundTasks as StarletteBackgroundTasks
from typing import Any, Callable
from typing_extensions import Annotated

P: Incomplete

class BackgroundTasks(StarletteBackgroundTasks):
    def add_task(self, func: Annotated[Callable[P, Any], None], *args: P.args, **kwargs: P.kwargs) -> None: ...
