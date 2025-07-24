from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleitemVideoRequest")


@_attrs_define
class ScheduleitemVideoRequest:
    """
    Attributes:
        name (str):
        categories (list[str]):
        header (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        creator (Union[Unset, str]):
        duration (Union[Unset, str]):
    """

    name: str
    categories: list[str]
    header: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    creator: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        categories = self.categories

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "categories": categories,
            }
        )
        if header is not UNSET:
            field_dict["header"] = header
        if description is not UNSET:
            field_dict["description"] = description
        if creator is not UNSET:
            field_dict["creator"] = creator
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        categories = cast(list[str], d.pop("categories"))

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

        scheduleitem_video_request = cls(
            name=name,
            categories=categories,
            header=header,
            description=description,
            creator=creator,
            duration=duration,
        )

        scheduleitem_video_request.additional_properties = d
        return scheduleitem_video_request

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
