from typing import List, Optional, Protocol, Sequence

class Edge(Protocol):
    size: Optional[int]
    ratio: int
    minimum_size: int

def ratio_resolve(total: int, edges: Sequence[Edge]) -> List[int]:
    ...

def ratio_reduce(total: int, ratios: Sequence[int], maximums: Sequence[int], values: Sequence[int]) -> List[int]:
    ...

def ratio_distribute(total: int, ratios: Sequence[int], minimums: Optional[Sequence[int]] = None) -> List[int]:
    ...