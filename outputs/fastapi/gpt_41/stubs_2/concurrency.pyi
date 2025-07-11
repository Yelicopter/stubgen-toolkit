from typing import AsyncGenerator, ContextManager, TypeVar, Any, AsyncIterator
from contextlib import asynccontextmanager as asynccontextmanager

_T = TypeVar("_T")

@asynccontextmanager
async def contextmanager_in_threadpool(
    cm: ContextManager[_T],
) -> AsyncGenerator[_T, None]: ...