import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedBulletin")


@_attrs_define
class PatchedBulletin:
    """
    Attributes:
        id (Union[Unset, int]):
        heading (Union[Unset, str]):
        text (Union[Unset, str]):
        created (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, int] = UNSET
    heading: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        heading = self.heading

        text = self.text

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if heading is not UNSET:
            field_dict["heading"] = heading
        if text is not UNSET:
            field_dict["text"] = text
        if created is not UNSET:
            field_dict["created"] = created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        heading = d.pop("heading", UNSET)

        text = d.pop("text", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        patched_bulletin = cls(
            id=id,
            heading=heading,
            text=text,
            created=created,
        )

        patched_bulletin.additional_properties = d
        return patched_bulletin

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
