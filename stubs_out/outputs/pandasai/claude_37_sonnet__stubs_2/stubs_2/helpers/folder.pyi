from ..helpers.path import find_project_root as find_project_root
from pydantic import BaseModel
from typing import Optional

class FolderConfig(BaseModel):
    permissions: int
    exist_ok: bool

class Folder:
    @staticmethod
    def create(path, config: Optional[FolderConfig] = ...) -> None: ...
