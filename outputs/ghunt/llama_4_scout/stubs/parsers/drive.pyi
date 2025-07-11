from datetime import datetime
from typing import List, Dict

from ghunt.helpers.utils import get_datetime_utc
from ghunt.objects.apis import Parser

class DriveFile(Parser):
    def __init__(self) -> None:
        self.kind: str = ""
        self.id: str = ""
        self.thumbnail_version: str = ""
        self.title: str = ""
        self.mime_type: str = ""
        self.labels: DriveLabels = DriveLabels()
        self.created_date: datetime = None
        self.modified_date: datetime = None
        self.last_viewed_by_me_date: datetime = None
        self.marked_viewed_by_me_date: datetime = None
        self.shared_with_me_date: datetime = None
        self.recency: datetime = None
        self.recency_reason: str = ""
        self.version: str = ""
        self.parents: List[Dict] = []
        self.user_permission: DriveUserPermission = DriveUserPermission()
        self.file_extension: str = ""
        self.file_size: str = ""
        self.quota_bytes_used: str = ""
        self.owners: List[DriveUser] = []
        self.last_modifying_user: DriveUser = DriveUser()
        self.capabilities: DriveCapabilities = DriveCapabilities()
        self.copyable: bool = False
        self.shared: bool = False
        self.explicitly_trashed: bool = False
        self.authorized_app_ids: List[str] = []
        self.primary_sync_parent_id: str = ""
        self.subscribed: bool = False
        self.passively_subscribed: bool = False
        self.flagged_for_abuse: bool = False
        self.abuse_is_appealable: bool = False
        self.source_app_id: str = ""
        self.spaces: List[str] = []
        self.has_thumbnail: bool = False
        self.contains_unsubscribed_children: bool = False
        self.alternate_link: str = ""
        self.icon_link: str = ""
        self.copy_requires_writer_permission: bool = False
        self.permissions: List[DrivePermission] = []
        self.head_revision_id: str = ""
        self.video_media_metadata: DriveVideoMediaMetadata = DriveVideoMediaMetadata()
        self.has_legacy_blob_comments: bool = False
        self.label_info: DriveLabelInfo = DriveLabelInfo()
        self.web_content_link: str = ""
        self.thumbnail_link: str = ""
        self.description: str = ""
        self.original_filename: str = ""
        self.permissions_summary: DrivePermissionsSummary = DrivePermissionsSummary()
        self.full_file_extension: str = ""
        self.md5_checksum: str = ""
        self.owned_by_me: bool = False
        self.writers_can_share: bool = False
        self.image_media_metadata: DriveImageMediaMetadata = DriveImageMediaMetadata()
        self.is_app_authorized: bool = False
        self.link_share_metadata: DriveLinkShareMetadata = DriveLinkShareMetadata()
        self.etag: str = ""
        self.self_link: str = ""
        self.embed_link: str = ""
        self.open_with_links: DriveOpenWithLinks = DriveOpenWithLinks()
        self.default_open_with_link: str = ""
        self.has_child_folders: bool = False
        self.owner_names: List[str] = []
        self.last_modifying_user_name: str = ""
        self.editable: bool = False
        self.app_data_contents: bool = False
        self.drive_source: DriveSource = DriveSource()
        self.source: DriveSource = DriveSource()
        self.descendant_of_root: bool = False
        self.folder_color: str = ""
        self.folder_properties: DriveFolderProperties = DriveFolderProperties()
        self.resource_key: str = ""
        self.has_augmented_permissions: bool = False
        self.ancestor_has_augmented_permissions: bool = False
        self.has_visitor_permissions: bool = False
        self.primary_domain_name: str = ""
        self.organization_display_name: str = ""
        self.customer_id: str = ""
        self.team_drive_id: str = ""
        self.folder_color_rgb: str = ""

    def _scrape(self, file_data: Dict) -> None:
        ...

class DriveLabels(Parser):
    def __init__(self) -> None:
        self.starred: bool = False
        self.trashed: bool = False
        self.restricted: bool = False
        self.viewed: bool = False
        self.hidden: bool = False
        self.modified: bool = False

    def _scrape(self, labels_data: Dict) -> None:
        ...