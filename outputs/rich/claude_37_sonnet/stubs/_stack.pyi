from typing import List, TypeVar

T = TypeVar('T')

class Stack(List[T]):
    @property
    def top(self) -> T:
        ...

    def push(self, item: T) -> None:
        ...