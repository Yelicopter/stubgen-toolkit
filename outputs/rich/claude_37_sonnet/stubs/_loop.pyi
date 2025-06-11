from typing import Iterable, Tuple, TypeVar

T = TypeVar('T')

def loop_first(values: Iterable[T]) -> Iterable[Tuple[bool, T]]:
    ...

def loop_last(values: Iterable[T]) -> Iterable[Tuple[bool, T]]:
    ...

def loop_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
    ...