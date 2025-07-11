from pathlib import Path

def _absolute_or_from_project_root(path: str) -> Path: ...

models_path: Path
models_cache_path: Path
docs_path: Path
local_data_path: Path