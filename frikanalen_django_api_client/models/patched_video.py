import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization import Organization


T = TypeVar("T", bound="PatchedVideo")


@_attrs_define
class PatchedVideo:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        header (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        files (Union[Unset, str]):
        creator (Union[Unset, str]):
        organization (Union[Unset, Organization]):
        duration (Union[Unset, str]):
        categories (Union[Unset, list[str]]):
        framerate (Union[Unset, int]): Framerate of master video in thousands / second
        proper_import (Union[Unset, bool]):
        has_tono_records (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        is_filler (Union[Unset, bool]): You still have the editorial responsibility.  Only affect videos from members.
        ref_url (Union[Unset, str]): URL for reference
        created_time (Union[None, Unset, datetime.datetime]): Time the program record was created
        updated_time (Union[None, Unset, datetime.datetime]): Time the program record has been updated
        uploaded_time (Union[None, Unset, datetime.datetime]): Time the original video for the program was uploaded
        ogv_url (Union[Unset, str]):
        large_thumbnail_url (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    header: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    files: Union[Unset, str] = UNSET
    creator: Union[Unset, str] = UNSET
    organization: Union[Unset, "Organization"] = UNSET
    duration: Union[Unset, str] = UNSET
    categories: Union[Unset, list[str]] = UNSET
    framerate: Union[Unset, int] = UNSET
    proper_import: Union[Unset, bool] = UNSET
    has_tono_records: Union[Unset, bool] = UNSET
    publish_on_web: Union[Unset, bool] = UNSET
    is_filler: Union[Unset, bool] = UNSET
    ref_url: Union[Unset, str] = UNSET
    created_time: Union[None, Unset, datetime.datetime] = UNSET
    updated_time: Union[None, Unset, datetime.datetime] = UNSET
    uploaded_time: Union[None, Unset, datetime.datetime] = UNSET
    ogv_url: Union[Unset, str] = UNSET
    large_thumbnail_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

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

        files = self.files

        creator = self.creator

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        duration = self.duration

        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

        framerate = self.framerate

        proper_import = self.proper_import

        has_tono_records = self.has_tono_records

        publish_on_web = self.publish_on_web

        is_filler = self.is_filler

        ref_url = self.ref_url

        created_time: Union[None, Unset, str]
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

        updated_time: Union[None, Unset, str]
        if isinstance(self.updated_time, Unset):
            updated_time = UNSET
        elif isinstance(self.updated_time, datetime.datetime):
            updated_time = self.updated_time.isoformat()
        else:
            updated_time = self.updated_time

        uploaded_time: Union[None, Unset, str]
        if isinstance(self.uploaded_time, Unset):
            uploaded_time = UNSET
        elif isinstance(self.uploaded_time, datetime.datetime):
            uploaded_time = self.uploaded_time.isoformat()
        else:
            uploaded_time = self.uploaded_time

        ogv_url = self.ogv_url

        large_thumbnail_url = self.large_thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if header is not UNSET:
            field_dict["header"] = header
        if description is not UNSET:
            field_dict["description"] = description
        if files is not UNSET:
            field_dict["files"] = files
        if creator is not UNSET:
            field_dict["creator"] = creator
        if organization is not UNSET:
            field_dict["organization"] = organization
        if duration is not UNSET:
            field_dict["duration"] = duration
        if categories is not UNSET:
            field_dict["categories"] = categories
        if framerate is not UNSET:
            field_dict["framerate"] = framerate
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
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if uploaded_time is not UNSET:
            field_dict["uploadedTime"] = uploaded_time
        if ogv_url is not UNSET:
            field_dict["ogvUrl"] = ogv_url
        if large_thumbnail_url is not UNSET:
            field_dict["largeThumbnailUrl"] = large_thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization import Organization

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

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

        files = d.pop("files", UNSET)

        creator = d.pop("creator", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        duration = d.pop("duration", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

        framerate = d.pop("framerate", UNSET)

        proper_import = d.pop("properImport", UNSET)

        has_tono_records = d.pop("hasTonoRecords", UNSET)

        publish_on_web = d.pop("publishOnWeb", UNSET)

        is_filler = d.pop("isFiller", UNSET)

        ref_url = d.pop("refUrl", UNSET)

        def _parse_created_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = isoparse(data)

                return created_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_time = _parse_created_time(d.pop("createdTime", UNSET))

        def _parse_updated_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_time_type_0 = isoparse(data)

                return updated_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        updated_time = _parse_updated_time(d.pop("updatedTime", UNSET))

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

        ogv_url = d.pop("ogvUrl", UNSET)

        large_thumbnail_url = d.pop("largeThumbnailUrl", UNSET)

        patched_video = cls(
            id=id,
            name=name,
            header=header,
            description=description,
            files=files,
            creator=creator,
            organization=organization,
            duration=duration,
            categories=categories,
            framerate=framerate,
            proper_import=proper_import,
            has_tono_records=has_tono_records,
            publish_on_web=publish_on_web,
            is_filler=is_filler,
            ref_url=ref_url,
            created_time=created_time,
            updated_time=updated_time,
            uploaded_time=uploaded_time,
            ogv_url=ogv_url,
            large_thumbnail_url=large_thumbnail_url,
        )

        patched_video.additional_properties = d
        return patched_video

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
