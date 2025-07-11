from ghunt.parsers.drive import DriveComment, DriveCommentList, DriveCommentReply, DriveFile
from ghunt.objects.base import DriveExtractedUser
from typing import Any

def get_users_from_file(file: DriveFile) -> list[DriveExtractedUser]:
    ...

def get_comments_from_file(comments: DriveCommentList) -> list[Any]:
    ...