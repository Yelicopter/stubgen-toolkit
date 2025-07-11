import ast

from pandasai.agent.state import AgentState
from pandasai.exceptions import ExecuteSQLQueryNotUsed

class CodeRequirementValidator:
    class _FunctionCallVisitor(ast.NodeVisitor):
        ...

    def __init__(self, context: AgentState) -> None:
        ...

    def validate(self, code: str) -> bool:
        ...