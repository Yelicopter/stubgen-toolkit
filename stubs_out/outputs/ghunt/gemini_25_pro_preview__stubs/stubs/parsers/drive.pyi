from datetime import datetime
from ghunt.objects.apis import Parser
from typing import Any, List, Optional

class DrivePicture(Parser):
    url: str
    def __init__(self) -> None: ...

class DriveUser(Parser):
    kind: str
    id: str
    permission_id: str
    email_address_from_account: str
    display_name: str
    picture: DrivePicture
    is_authenticated_user: bool
    email_address: str
    def __init__(self) -> None: ...

class DriveCapabilities(Parser):
    can_add_children: bool
    can_add_my_drive_parent: bool
    can_block_owner: bool
    can_change_security_update_enabled: bool
    can_copy: bool
    can_delete: bool
    can_download: bool
    can_edit: bool
    can_edit_category_metadata: bool
    can_request_approval: bool
    can_move_children_within_drive: bool
    can_move_item_into_team_drive: bool
    can_move_item_within_drive: bool
    can_read: bool
    can_read_category_metadata: bool
    can_remove_children: bool
    can_remove_my_drive_parent: bool
    can_rename: bool
    can_share: bool
    can_share_child_files: bool
    can_share_child_folders: bool
    can_trash: bool
    can_untrash: bool
    can_comment: bool
    can_move_item_out_of_drive: bool
    can_add_as_owner: bool
    can_add_as_organizer: bool
    can_add_as_file_organizer: bool
    can_add_as_writer: bool
    can_add_as_commenter: bool
    can_add_as_reader: bool
    can_change_to_owner: bool
    can_change_to_organizer: bool
    can_change_to_file_organizer: bool
    can_change_to_writer: bool
    can_change_to_commenter: bool
    can_change_to_reader: bool
    can_change_to_reader_on_published_view: bool
    can_remove: bool
    can_accept_ownership: bool
    can_add_encrypted_children: bool
    can_change_copy_requires_writer_permission: bool
    can_change_permission_expiration: bool
    can_change_restricted_download: bool
    can_change_writers_can_share: bool
    can_create_decrypted_copy: bool
    can_create_encrypted_copy: bool
    can_list_children: bool
    can_manage_members: bool
    can_manage_visitors: bool
    can_modify_content: bool
    can_modify_content_restriction: bool
    can_modify_labels: bool
    can_print: bool
    can_read_all_permissions: bool
    can_read_labels: bool
    can_read_revisions: bool
    can_set_missing_required_fields: bool
    can_share_as_commenter: bool
    can_share_as_file_organizer: bool
    can_share_as_organizer: bool
    can_share_as_owner: bool
    can_share_as_reader: bool
    can_share_as_writer: bool
    can_share_published_view_as_reader: bool
    can_share_to_all_users: bool
    can_add_folder_from_another_drive: bool
    can_delete_children: bool
    can_move_item_out_of_team_drive: bool
    can_move_item_within_team_drive: bool
    can_move_team_drive_item: bool
    can_read_team_drive: bool
    can_trash_children: bool
    def __init__(self) -> None: ...

class DrivePermission(Parser):
    kind: str
    id: str
    self_link: str
    role: str
    additional_roles: List[str]
    type: str
    selectable_roles: List[str]
    pending_owner: bool
    with_link: bool
    capabilities: DriveCapabilities
    user_id: str
    name: str
    email_address: str
    domain: str
    photo_link: str
    deleted: bool
    is_collaborator_account: bool
    def __init__(self) -> None: ...

class DriveMiniPermission(Parser):
    permission_id: str
    role: str
    type: str
    with_link: bool
    def __init__(self) -> None: ...

class DrivePermissionsSummary(Parser):
    entry_count: int
    visibility: List[DriveMiniPermission]
    select_permissions: List[DrivePermission]
    def __init__(self) -> None: ...

class DriveLabels(Parser):
    starred: bool
    trashed: bool
    restricted: bool
    viewed: bool
    hidden: bool
    modified: bool
    def __init__(self) -> None: ...

class DriveParentReference(Parser):
    kind: str
    id: str
    self_link: str
    parent_link: str
    is_root: bool
    def __init__(self) -> None: ...

class DriveUserPermission(Parser):
    role: str
    id: str
    type: str
    def __init__(self) -> None: ...

class DriveVideoMediaMetadata(Parser):
    width: int
    height: int
    duration_millis: str
    def __init__(self) -> None: ...

class DriveLabelInfo(Parser):
    label_count: int
    incomplete: bool
    def __init__(self) -> None: ...

class DriveImageMediaMetadata(Parser):
    width: int
    height: int
    rotation: int
    def __init__(self) -> None: ...

class DriveLinkShareMetadata(Parser):
    security_update_eligible: bool
    security_update_enabled: bool
    security_update_change_disabled_reason: str
    security_update_explicitly_set: bool
    def __init__(self) -> None: ...

class DriveOpenWithLinks(Parser):
    digitsfield: str
    def __init__(self) -> None: ...

class DriveSource(Parser):
    client_service_id: str
    value: str
    def __init__(self) -> None: ...

class DriveFolderProperties(Parser):
    psyncho_root: bool
    psyncho_folder: bool
    machine_root: bool
    arbitrary_sync_folder: bool
    external_media: bool
    photos_and_videos_only: bool
    def __init__(self) -> None: ...

class DriveFile(Parser):
    kind: str
    id: str
    thumbnail_version: str
    title: str
    mime_type: str
    labels: DriveLabels
    created_date: Optional[datetime]
    modified_date: Optional[datetime]
    last_viewed_by_me_date: Optional[datetime]
    marked_viewed_by_me_date: Optional[datetime]
    shared_with_me_date: Optional[datetime]
    recency: Optional[datetime]
    recency_reason: str
    version: str
    parents: List[DriveParentReference]
    user_permission: DriveUserPermission
    file_extension: str
    file_size: str
    quota_bytes_used: str
    owners: List[DriveUser]
    last_modifying_user: DriveUser
    capabilities: DriveCapabilities
    copyable: bool
    shared: bool
    explicitly_trashed: bool
    authorized_app_ids: List[Any]
    primary_sync_parent_id: str
    subscribed: bool
    passively_subscribed: bool
    flagged_for_abuse: bool
    abuse_is_appealable: bool
    source_app_id: str
    spaces: List[Any]
    has_thumbnail: bool
    contains_unsubscribed_children: bool
    alternate_link: str
    icon_link: str
    copy_requires_writer_permission: bool
    permissions: List[DrivePermission]
    head_revision_id: str
    video_media_metadata: DriveVideoMediaMetadata
    has_legacy_blob_comments: bool
    label_info: DriveLabelInfo
    web_content_link: str
    thumbnail_link: str
    description: str
    original_filename: str
    permissions_summary: DrivePermissionsSummary
    full_file_extension: str
    md5_checksum: str
    owned_by_me: bool
    writers_can_share: bool
    image_media_metadata: DriveImageMediaMetadata
    is_app_authorized: bool
    link_share_metadata: DriveLinkShareMetadata
    etag: str
    self_link: str
    embed_link: str
    open_with_links: DriveOpenWithLinks
    default_open_with_link: str
    has_child_folders: bool
    owner_names: List[Any]
    last_modifying_user_name: str
    editable: bool
    app_data_contents: bool
    drive_source: DriveSource
    source: DriveSource
    descendant_of_root: bool
    folder_color: str
    folder_properties: DriveFolderProperties
    resource_key: str
    has_augmented_permissions: bool
    ancestor_has_augmented_permissions: bool
    has_visitor_permissions: bool
    primary_domain_name: str
    organization_display_name: str
    customer_id: str
    team_drive_id: str
    folder_color_rgb: str
    def __init__(self) -> None: ...

class DriveChildReference(Parser):
    id: str
    self_link: str
    kind: str
    child_link: str
    def __init__(self) -> None: ...

class DriveChildList(Parser):
    kind: str
    etag: str
    self_link: str
    items: List[DriveChildReference]
    def __init__(self) -> None: ...

class DriveApp(Parser):
    kind: str
    id: str
    name: str
    type: str
    short_description: str
    long_description: str
    supports_create: bool
    supports_import: bool
    supports_multi_open: bool
    supports_offline_create: bool
    supports_mobile_browser: bool
    installed: bool
    authorized: bool
    drive_branded_app: bool
    drive_branded: bool
    hidden: bool
    removable: bool
    has_drive_wide_scope: bool
    use_by_default: bool
    primary_mime_types: List[Any]
    requires_authorization_before_open_with: bool
    supports_team_drives: bool
    supports_all_drives: bool
    def __init__(self) -> None: ...

class DriveCommentContext(Parser):
    type: str
    value: str
    def __init__(self) -> None: ...

class DriveCommentReply(Parser):
    reply_id: str
    kind: str
    created_date: str
    modified_date: str
    author: DriveUser
    deleted: bool
    html_content: str
    content: str
    def __init__(self) -> None: ...

class DriveComment(Parser):
    comment_id: str
    kind: str
    created_date: str
    modified_date: str
    file_id: str
    status: str
    anchor: str
    replies: List[DriveCommentReply]
    author: DriveUser
    deleted: bool
    html_content: str
    content: str
    context: DriveCommentContext
    file_title: str
    def __init__(self) -> None: ...

class DriveCommentList(Parser):
    kind: str
    self_link: str
    items: List[DriveComment]
    def __init__(self) -> None: ...
