import ast
import os.path
import re
import uuid
from pathlib import Path

import astor

from pandasai.agent.state import AgentState
from pandasai.constants import DEFAULT_CHART_DIRECTORY
from pandasai.core.code_execution.code_executor import CodeExecutor
from pandasai.query_builders.sql_parser import SQLParser

class CodeCleaner:
    def __init__(self, context: AgentState) -> None:
        ...

    def _check_direct_sql_func_def_exists(self, node: ast.FunctionDef) -> bool:
        ...

    def _replace_table_names(
        self,
        sql_query: str,
        table_names: List[str],
        allowed_table_names: Dict[str, str],
    ) -> str:
        ...

    def _clean_sql_query(self, sql_query: str) -> str:
        ...

    def _validate_and_make_table_name_case_sensitive(self, node: ast.AST) -> ast.AST:
        ...

    def get_target_names(self, targets: List[ast.AST]) -> tuple[List[str], bool, ast.AST]:
        ...

    def check_is_df_declaration(self, node: ast.AST) -> bool:
        ...

    def clean_code(self, code: str) -> str:
        ...

    def _replace_output_filenames_with_temp_chart(self, code: str) -> str:
        ...
