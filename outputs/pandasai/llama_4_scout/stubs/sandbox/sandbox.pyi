import ast


class Sandbox:
    _started: bool

    def __init__(self) -> None:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    def execute(self, code: str, environment: dict) -> None:
        ...

    def _exec_code(self, code: str, environment: dict) -> None:
        ...

    def transfer_file(self, csv_data: str, filename: str = "file.csv") -> None:
        ...

    def _extract_sql_queries_from_code(self, code: str) -> List[str]:
        ...

    def _compile_code(self, code: str) -> ast.Module:
        ...

    def _compile_code(self, code: str) -> ast.Module:
        ...