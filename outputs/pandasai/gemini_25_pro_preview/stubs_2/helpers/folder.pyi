from pydantic import BaseModel

class FolderConfig(BaseModel):
    permissions: int
    exist_ok: bool

class Folder:
    @staticmethod
    def create(path: str, config: FolderConfig = ...) -> None: ...