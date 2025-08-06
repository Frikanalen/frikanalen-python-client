from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduleitem_organization import ScheduleitemOrganization


T = TypeVar("T", bound="ScheduleitemVideo")


@_attrs_define
class ScheduleitemVideo:
    """
    Attributes:
        id (int):
        name (str):
        organization (ScheduleitemOrganization):
        categories (list[str]):
        header (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
    """

    id: int
    name: str
    organization: "ScheduleitemOrganization"
    categories: list[str]
    header: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        organization = self.organization.to_dict()

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
                "categories": categories,
            }
        )
        if header is not UNSET:
            field_dict["header"] = header
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scheduleitem_organization import ScheduleitemOrganization

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        organization = ScheduleitemOrganization.from_dict(d.pop("organization"))

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

        scheduleitem_video = cls(
            id=id,
            name=name,
            organization=organization,
            categories=categories,
            header=header,
            description=description,
        )

        scheduleitem_video.additional_properties = d
        return scheduleitem_video

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
