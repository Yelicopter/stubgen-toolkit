from typing import *
from ghunt.parsers.drive import DriveComment, DriveCommentList, DriveCommentReply, DriveFile
from ghunt.objects.base import DriveExtractedUser
from ghunt.helpers.utils import oprint

def get_users_from_file(file: DriveFile) -> List[DriveExtractedUser]: ...
def get_comments_from_file(comments: DriveCommentList) -> List[Tuple[str, Dict[str, Any]]]: ...