from __future__ import annotations

from typing import TYPE_CHECKING

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


def get_chat_prompt_for_sql(context: dict) -> GeneratePythonCodeWithSQLPrompt:
    ...


def get_correct_error_prompt_for_sql(
    context: dict, code: str, traceback_error: str
) -> CorrectExecuteSQLQueryUsageErrorPrompt:
    ...


def get_correct_output_type_error_prompt(
    context: dict, code: str, traceback_error: str
) -> CorrectOutputTypeErrorPrompt:
    ...


__all__ = [
    "BasePrompt",
    "CorrectErrorPrompt",
    "GeneratePythonCodePrompt",
    "GeneratePythonCodeWithSQLPrompt",
]