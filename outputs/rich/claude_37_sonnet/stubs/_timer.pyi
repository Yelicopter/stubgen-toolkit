from typing import Generator, Any
import contextlib

@contextlib.contextmanager
def timer(subject: str = 'time') -> Generator[None, None, None]:
    ...