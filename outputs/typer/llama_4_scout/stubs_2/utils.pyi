from typing import Any, Callable, Dict, List, Optional, Tuple, Type, cast

def _param_type_to_user_string(param_type: Any) -> str:
    ...

def get_params_from_function(func: Callable[..., Any]) -> Dict[str, Any]:
    ...

def _split_annotation_from_typer_annotations(
    base_annotation: Any,
) -> Tuple[Any, List[Any]]:
    ...