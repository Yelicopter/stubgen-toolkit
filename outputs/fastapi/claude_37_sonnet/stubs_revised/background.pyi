from typing import Any, Callable, ParamSpec

from starlette.background import BackgroundTasks as StarletteBackgroundTasks
from typing_extensions import Annotated, Doc

P = ParamSpec("P")

class BackgroundTasks(StarletteBackgroundTasks):
    def add_task(
        self,
        func: Callable[P, Any],
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> None: ...