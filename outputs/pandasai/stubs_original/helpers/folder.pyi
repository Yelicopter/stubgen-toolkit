from ..helpers.path import find_project_root as find_project_root
from pandasai.constants import DEFAULT_FILE_PERMISSIONS as DEFAULT_FILE_PERMISSIONS
from pydantic import BaseModel

class FolderConfig(BaseModel):
    permissions: str
    exist_ok: bool

class Folder:
    @staticmethod
    def create(path, config: FolderConfig = ...): ...
