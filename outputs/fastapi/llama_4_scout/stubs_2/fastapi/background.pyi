from typing import Any, Callable

from starlette.background import BackgroundTasks as StarletteBackgroundTasks
from typing_extensions import Annotated, ParamSpec

P = ParamSpec("P")

class BackgroundTasks(StarletteBackgroundTasks):
    def add_task(
        self,
        func: Callable[P, Any],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        ...