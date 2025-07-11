from typing import Sequence, Optional, Set, List, Any, NamedTuple

BUILTIN_TYPES: dict[str, str]

class Call(NamedTuple):
    name: str
    line: int
    column: int

class Visitor:
    builtin_type_calls: List[Call]
    ignore: Set[str]
    allow_dict_kwargs: bool
    def __init__(
        self,
        ignore: Optional[Set[str]] = ...,
        allow_dict_kwargs: bool = ...,
    ) -> None: ...
    def _check_dict_call(self, node: Any) -> bool: ...
    def visit_Call(self, node: Any) -> None: ...

def check_file(
    filename: str,
    ignore: Optional[Set[str]] = ...,
    allow_dict_kwargs: bool = ...,
) -> List[Call]: ...
def parse_ignore(value: str) -> Set[str]: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...