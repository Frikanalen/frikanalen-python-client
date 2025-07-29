import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVideoRequest")


@_attrs_define
class PatchedVideoRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        header (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        creator (Union[Unset, str]):
        duration (Union[Unset, str]):
        categories (Union[Unset, list[str]]):
        proper_import (Union[Unset, bool]): Has the video been properly imported?
        has_tono_records (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        is_filler (Union[Unset, bool]): You still have the editorial responsibility.  Only affect videos from members.
        ref_url (Union[Unset, str]): URL for reference
        uploaded_time (Union[None, Unset, datetime.datetime]): Time the original video for the program was uploaded
    """

    name: Union[Unset, str] = UNSET
    header: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    creator: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    categories: Union[Unset, list[str]] = UNSET
    proper_import: Union[Unset, bool] = UNSET
    has_tono_records: Union[Unset, bool] = UNSET
    publish_on_web: Union[Unset, bool] = UNSET
    is_filler: Union[Unset, bool] = UNSET
    ref_url: Union[Unset, str] = UNSET
    uploaded_time: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        creator = self.creator

        duration = self.duration

        categories: Union[Unset, list[str]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories

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
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if header is not UNSET:
            field_dict["header"] = header
        if description is not UNSET:
            field_dict["description"] = description
        if creator is not UNSET:
            field_dict["creator"] = creator
        if duration is not UNSET:
            field_dict["duration"] = duration
        if categories is not UNSET:
            field_dict["categories"] = categories
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
        d = dict(src_dict)
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

        creator = d.pop("creator", UNSET)

        duration = d.pop("duration", UNSET)

        categories = cast(list[str], d.pop("categories", UNSET))

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

        patched_video_request = cls(
            name=name,
            header=header,
            description=description,
            creator=creator,
            duration=duration,
            categories=categories,
            proper_import=proper_import,
            has_tono_records=has_tono_records,
            publish_on_web=publish_on_web,
            is_filler=is_filler,
            ref_url=ref_url,
            uploaded_time=uploaded_time,
        )

        patched_video_request.additional_properties = d
        return patched_video_request

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
