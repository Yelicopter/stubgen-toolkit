from contextlib import asynccontextmanager as asynccontextmanager
from typing import AsyncGenerator, ContextManager, TypeVar

from starlette.concurrency import iterate_in_threadpool as iterate_in_threadpool
from starlette.concurrency import run_in_threadpool as run_in_threadpool
from starlette.concurrency import (
    run_until_first_complete as run_until_first_complete,
)

_T = TypeVar("_T")

@asynccontextmanager
async def contextmanager_in_threadpool(
    cm: ContextManager[_T],
) -> AsyncGenerator[_T, None]: ...