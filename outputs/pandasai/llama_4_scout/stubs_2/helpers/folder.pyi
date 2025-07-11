import os

from pydantic import BaseModel

from pandasai.constants import DEFAULT_FILE_PERMISSIONS

from ..helpers.path import find_project_root


class FolderConfig(BaseModel):
    permissions: int = DEFAULT_FILE_PERMISSIONS
    exist_ok: bool = True


class Folder:
    @staticmethod
    def create(path: str, config: FolderConfig = FolderConfig()) -> None:
        ...