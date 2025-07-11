from anyio import CapacityLimiter as CapacityLimiter
from typing import Any, AsyncGenerator, ContextManager

async def contextmanager_in_threadpool(cm: ContextManager[Any]) -> AsyncGenerator[_T, None]: ...
