from contextlib import asynccontextmanager
from typing import (
    Any,
    AsyncGenerator,
    ContextManager,
    TypeVar,
)

import anyio.to_thread
from anyio import CapacityLimiter
from starlette.concurrency import (
    iterate_in_threadpool as iterate_in_threadpool, 
    run_in_threadpool as run_in_threadpool, 
    run_until_first_complete as run_until_first_complete, 
)

_T = TypeVar("_T")

@asynccontextmanager
async def contextmanager_in_threadpool(
    cm: ContextManager[Any],
) -> AsyncGenerator[None, None]:
    yield