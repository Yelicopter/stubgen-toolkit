from contextlib import asynccontextmanager
from typing import AsyncGenerator, ContextManager, TypeVar

import anyio.to_thread
from anyio import CapacityLimiter
from starlette.concurrency import iterate_in_threadpool
from starlette.concurrency import run_in_threadpool
from starlette.concurrency import run_until_first_complete

_T = TypeVar("_T")

async def contextmanager_in_threadpool(
    cm: ContextManager[_T],
) -> AsyncGenerator[_T, None]: ...