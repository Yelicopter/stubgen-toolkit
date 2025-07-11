from anyio import CapacityLimiter as CapacityLimiter
from starlette.concurrency import iterate_in_threadpool as iterate_in_threadpool, run_in_threadpool as run_in_threadpool, run_until_first_complete as run_until_first_complete
from typing import AsyncGenerator, ContextManager

async def contextmanager_in_threadpool(cm: ContextManager[_T]) -> AsyncGenerator[_T, None]: ...
