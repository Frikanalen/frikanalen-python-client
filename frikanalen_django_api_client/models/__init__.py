"""Contains all the data models used in inputs/outputs"""

from .as_run import AsRun
from .as_run_request import AsRunRequest
from .auth_token import AuthToken
from .auth_token_request import AuthTokenRequest
from .bulletin import Bulletin
from .bulletin_request import BulletinRequest
from .category import Category
from .category_request import CategoryRequest
from .new_user import NewUser
from .new_user_request import NewUserRequest
from .organization import Organization
from .organization_request import OrganizationRequest
from .paginated_as_run_list import PaginatedAsRunList
from .paginated_category_list import PaginatedCategoryList
from .paginated_organization_list import PaginatedOrganizationList
from .paginated_scheduleitem_read_list import PaginatedScheduleitemReadList
from .paginated_video_file_list import PaginatedVideoFileList
from .paginated_video_list import PaginatedVideoList
from .patched_as_run_request import PatchedAsRunRequest
from .patched_bulletin_request import PatchedBulletinRequest
from .patched_category_request import PatchedCategoryRequest
from .patched_organization_request import PatchedOrganizationRequest
from .patched_scheduleitem_read_request import PatchedScheduleitemReadRequest
from .patched_user_request import PatchedUserRequest
from .patched_video_file_request import PatchedVideoFileRequest
from .patched_video_request import PatchedVideoRequest
from .scheduleitem_modify import ScheduleitemModify
from .scheduleitem_modify_request import ScheduleitemModifyRequest
from .scheduleitem_read import ScheduleitemRead
from .scheduleitem_video import ScheduleitemVideo
from .scheduleitem_video_request import ScheduleitemVideoRequest
from .schedulereason_enum import SchedulereasonEnum
from .schema_retrieve_format import SchemaRetrieveFormat
from .schema_retrieve_lang import SchemaRetrieveLang
from .schema_retrieve_response_200 import SchemaRetrieveResponse200
from .user import User
from .user_request import UserRequest
from .video import Video
from .video_create import VideoCreate
from .video_create_files import VideoCreateFiles
from .video_create_request import VideoCreateRequest
from .video_file import VideoFile
from .video_file_request import VideoFileRequest
from .video_files import VideoFiles
from .video_request import VideoRequest
from .video_upload_token import VideoUploadToken
from .videofiles_list_format_fsname import VideofilesListFormatFsname

__all__ = (
    "AsRun",
    "AsRunRequest",
    "AuthToken",
    "AuthTokenRequest",
    "Bulletin",
    "BulletinRequest",
    "Category",
    "CategoryRequest",
    "NewUser",
    "NewUserRequest",
    "Organization",
    "OrganizationRequest",
    "PaginatedAsRunList",
    "PaginatedCategoryList",
    "PaginatedOrganizationList",
    "PaginatedScheduleitemReadList",
    "PaginatedVideoFileList",
    "PaginatedVideoList",
    "PatchedAsRunRequest",
    "PatchedBulletinRequest",
    "PatchedCategoryRequest",
    "PatchedOrganizationRequest",
    "PatchedScheduleitemReadRequest",
    "PatchedUserRequest",
    "PatchedVideoFileRequest",
    "PatchedVideoRequest",
    "ScheduleitemModify",
    "ScheduleitemModifyRequest",
    "ScheduleitemRead",
    "ScheduleitemVideo",
    "ScheduleitemVideoRequest",
    "SchedulereasonEnum",
    "SchemaRetrieveFormat",
    "SchemaRetrieveLang",
    "SchemaRetrieveResponse200",
    "User",
    "UserRequest",
    "Video",
    "VideoCreate",
    "VideoCreateFiles",
    "VideoCreateRequest",
    "VideoFile",
    "VideoFileRequest",
    "VideoFiles",
    "VideofilesListFormatFsname",
    "VideoRequest",
    "VideoUploadToken",
)
