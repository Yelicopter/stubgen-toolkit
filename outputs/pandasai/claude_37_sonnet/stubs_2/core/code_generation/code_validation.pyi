import ast
from typing import List

from pandasai.agent.state import AgentState
from pandasai.exceptions import ExecuteSQLQueryNotUsed

class CodeRequirementValidator:
    class _FunctionCallVisitor(ast.NodeVisitor):
        function_calls: List[str]
        
        def __init__(self) -> None: ...
        
        def visit_Call(self, node: ast.Call) -> None: ...
    
    def __init__(self, context: AgentState) -> None: ...
    
    def validate(self, code: str) -> bool: ...