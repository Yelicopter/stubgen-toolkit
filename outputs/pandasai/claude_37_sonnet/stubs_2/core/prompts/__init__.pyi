from __future__ import annotations
from typing import TYPE_CHECKING, Any, List

from pandasai.core.prompts.correct_execute_sql_query_usage_error_prompt import (
    CorrectExecuteSQLQueryUsageErrorPrompt,
)
from pandasai.core.prompts.correct_output_type_error_prompt import (
    CorrectOutputTypeErrorPrompt,
)

from .base import BasePrompt
from .generate_python_code_with_sql import GeneratePythonCodeWithSQLPrompt

if TYPE_CHECKING:
    from pandasai.agent.state import AgentState

def get_chat_prompt_for_sql(context: AgentState) -> BasePrompt: ...

def get_correct_error_prompt_for_sql(
    context: AgentState, code: str, traceback_error: str
) -> BasePrompt: ...

def get_correct_output_type_error_prompt(
    context: AgentState, code: str, traceback_error: str
) -> BasePrompt: ...

__all__: List[str]