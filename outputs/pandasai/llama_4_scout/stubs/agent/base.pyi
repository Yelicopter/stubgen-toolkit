import traceback
import warnings
from typing import Any, List, Optional, Union

class Agent:
    def __init__(
        self,
        dfs: Union[Union[DataFrame, VirtualDataFrame], List[Union[DataFrame, VirtualDataFrame]]],
        config: Optional[Union[Config, dict]] = None,
        memory_size: Optional[int] = 10,
        vectorstore: Optional[VectorStore] = None,
        description: Optional[str] = None,
        sandbox: Optional[Sandbox] = None,
    ) -> None:
        ...

    def chat(self, query: str, output_type: Optional[str] = None) -> Any:
        ...

    def follow_up(self, query: str, output_type: Optional[str] = None) -> Any:
        ...

    def generate_code(self, query: str) -> str:
        ...

    def execute_code(self, code: str) -> Any:
        ...

    def _execute_sql_query(self, query: str) -> pd.DataFrame:
        ...

    def generate_code_with_retries(self, query: str) -> str:
        ...

    def execute_with_retries(self, code: str) -> Any:
        ...

    def train(
        self,
        queries: Optional[str] = None,
        codes: Optional[str] = None,
        docs: Optional[List[str]] = None,
    ) -> None:
        ...

    def clear_memory(self) -> None:
        ...

    def add_message(self, message: str, is_user: bool = False) -> None:
        ...

    def start_new_conversation(self) -> None:
        ...

    def _process_query(self, query: str, output_type: Optional[str] = None) -> Any:
        ...

    def _regenerate_code_after_error(self, code: str, error: Exception) -> str:
        ...

    def _handle_exception(self, code: str) -> ErrorResponse:
        ...