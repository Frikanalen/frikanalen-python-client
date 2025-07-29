import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_create_files import VideoCreateFiles


T = TypeVar("T", bound="VideoCreate")


@_attrs_define
class VideoCreate:
    """
    Attributes:
        id (int):
        name (str):
        files (VideoCreateFiles):
        categories (list[str]):
        framerate (int): Framerate of master video in thousands / second
        created_time (Union[None, datetime.datetime]): Time the program record was created
        updated_time (Union[None, datetime.datetime]): Time the program record has been updated
        ogv_url (str):
        large_thumbnail_url (str):
        header (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        creator (Union[Unset, str]):
        organization (Union[Unset, int]):
        duration (Union[Unset, str]):
        proper_import (Union[Unset, bool]): Has the video been properly imported?
        has_tono_records (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        is_filler (Union[Unset, bool]): You still have the editorial responsibility.  Only affect videos from members.
        ref_url (Union[Unset, str]): URL for reference
        uploaded_time (Union[None, Unset, datetime.datetime]): Time the original video for the program was uploaded
    """

    id: int
    name: str
    files: "VideoCreateFiles"
    categories: list[str]
    framerate: int
    created_time: Union[None, datetime.datetime]
    updated_time: Union[None, datetime.datetime]
    ogv_url: str
    large_thumbnail_url: str
    header: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    creator: Union[Unset, str] = UNSET
    organization: Union[Unset, int] = UNSET
    duration: Union[Unset, str] = UNSET
    proper_import: Union[Unset, bool] = UNSET
    has_tono_records: Union[Unset, bool] = UNSET
    publish_on_web: Union[Unset, bool] = UNSET
    is_filler: Union[Unset, bool] = UNSET
    ref_url: Union[Unset, str] = UNSET
    uploaded_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        files = self.files.to_dict()

        categories = self.categories

        framerate = self.framerate

        created_time: Union[None, str]
        if isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        updated_time: Union[None, str]
        if isinstance(self.updated_time, datetime.datetime):
            updated_time = self.updated_time.isoformat()
        else:
            updated_time = self.updated_time

        ogv_url = self.ogv_url

        large_thumbnail_url = self.large_thumbnail_url

        header: Union[None, Unset, str]
        if isinstance(self.header, Unset):
            header = UNSET
        else:
            header = self.header

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        creator = self.creator

        organization = self.organization

        duration = self.duration

        proper_import = self.proper_import

        has_tono_records = self.has_tono_records

        publish_on_web = self.publish_on_web

        is_filler = self.is_filler

        ref_url = self.ref_url

        uploaded_time: Union[None, Unset, str]
        if isinstance(self.uploaded_time, Unset):
            uploaded_time = UNSET
        elif isinstance(self.uploaded_time, datetime.datetime):
            uploaded_time = self.uploaded_time.isoformat()
        else:
            uploaded_time = self.uploaded_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "files": files,
                "categories": categories,
                "framerate": framerate,
                "createdTime": created_time,
                "updatedTime": updated_time,
                "ogvUrl": ogv_url,
                "largeThumbnailUrl": large_thumbnail_url,
            }
        )
        if header is not UNSET:
            field_dict["header"] = header
        if description is not UNSET:
            field_dict["description"] = description
        if creator is not UNSET:
            field_dict["creator"] = creator
        if organization is not UNSET:
            field_dict["organization"] = organization
        if duration is not UNSET:
            field_dict["duration"] = duration
        if proper_import is not UNSET:
            field_dict["properImport"] = proper_import
        if has_tono_records is not UNSET:
            field_dict["hasTonoRecords"] = has_tono_records
        if publish_on_web is not UNSET:
            field_dict["publishOnWeb"] = publish_on_web
        if is_filler is not UNSET:
            field_dict["isFiller"] = is_filler
        if ref_url is not UNSET:
            field_dict["refUrl"] = ref_url
        if uploaded_time is not UNSET:
            field_dict["uploadedTime"] = uploaded_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_create_files import VideoCreateFiles

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        files = VideoCreateFiles.from_dict(d.pop("files"))

        categories = cast(list[str], d.pop("categories"))

        framerate = d.pop("framerate")

        def _parse_created_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = isoparse(data)

                return created_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created_time = _parse_created_time(d.pop("createdTime"))

        def _parse_updated_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_time_type_0 = isoparse(data)

                return updated_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        updated_time = _parse_updated_time(d.pop("updatedTime"))

        ogv_url = d.pop("ogvUrl")

        large_thumbnail_url = d.pop("largeThumbnailUrl")

        def _parse_header(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        header = _parse_header(d.pop("header", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        creator = d.pop("creator", UNSET)

        organization = d.pop("organization", UNSET)

        duration = d.pop("duration", UNSET)

        proper_import = d.pop("properImport", UNSET)

        has_tono_records = d.pop("hasTonoRecords", UNSET)

        publish_on_web = d.pop("publishOnWeb", UNSET)

        is_filler = d.pop("isFiller", UNSET)

        ref_url = d.pop("refUrl", UNSET)

        def _parse_uploaded_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uploaded_time_type_0 = isoparse(data)

                return uploaded_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        uploaded_time = _parse_uploaded_time(d.pop("uploadedTime", UNSET))

        video_create = cls(
            id=id,
            name=name,
            files=files,
            categories=categories,
            framerate=framerate,
            created_time=created_time,
            updated_time=updated_time,
            ogv_url=ogv_url,
            large_thumbnail_url=large_thumbnail_url,
            header=header,
            description=description,
            creator=creator,
            organization=organization,
            duration=duration,
            proper_import=proper_import,
            has_tono_records=has_tono_records,
            publish_on_web=publish_on_web,
            is_filler=is_filler,
            ref_url=ref_url,
            uploaded_time=uploaded_time,
        )

        video_create.additional_properties = d
        return video_create

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
