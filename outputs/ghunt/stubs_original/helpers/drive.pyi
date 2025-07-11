from typing import *
from ghunt.helpers.utils import oprint as oprint
from ghunt.objects.base import DriveExtractedUser as DriveExtractedUser
from ghunt.parsers.drive import DriveComment as DriveComment, DriveCommentList as DriveCommentList, DriveCommentReply as DriveCommentReply, DriveFile as DriveFile

def get_users_from_file(file: DriveFile) -> List[DriveExtractedUser]: ...
def get_comments_from_file(comments: DriveCommentList) -> List[Tuple[str, Dict[str, any]]]: ...
