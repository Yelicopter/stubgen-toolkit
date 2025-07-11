from __future__ import annotations

from typing import TYPE_CHECKING

from .base import BasePrompt
from .correct_execute_sql_query_usage_error_prompt import (
    CorrectExecuteSQLQueryUsageErrorPrompt,
)
from .correct_output_type_error_prompt import CorrectOutputTypeErrorPrompt
from .generate_python_code_with_sql import GeneratePythonCodeWithSQLPrompt

if TYPE_CHECKING:
    from pandasai.agent.state import AgentState

def get_chat_prompt_for_sql(context: AgentState) -> GeneratePythonCodeWithSQLPrompt: ...
def get_correct_error_prompt_for_sql(
    context: AgentState, code: str, traceback_error: str
) -> CorrectExecuteSQLQueryUsageErrorPrompt: ...
def get_correct_output_type_error_prompt(
    context: AgentState, code: str, traceback_error: str
) -> CorrectOutputTypeErrorPrompt: ...

__all__: list[str]