from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedOrganizationRequest")


@_attrs_define
class PatchedOrganizationRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        homepage (Union[None, Unset, str]):
        description (Union[Unset, str]):
        postal_address (Union[None, Unset, str]):
        street_address (Union[None, Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    homepage: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    postal_address: Union[None, Unset, str] = UNSET
    street_address: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        homepage: Union[None, Unset, str]
        if isinstance(self.homepage, Unset):
            homepage = UNSET
        else:
            homepage = self.homepage

        description = self.description

        postal_address: Union[None, Unset, str]
        if isinstance(self.postal_address, Unset):
            postal_address = UNSET
        else:
            postal_address = self.postal_address

        street_address: Union[None, Unset, str]
        if isinstance(self.street_address, Unset):
            street_address = UNSET
        else:
            street_address = self.street_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if homepage is not UNSET:
            field_dict["homepage"] = homepage
        if description is not UNSET:
            field_dict["description"] = description
        if postal_address is not UNSET:
            field_dict["postalAddress"] = postal_address
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        def _parse_homepage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        homepage = _parse_homepage(d.pop("homepage", UNSET))

        description = d.pop("description", UNSET)

        def _parse_postal_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postal_address = _parse_postal_address(d.pop("postalAddress", UNSET))

        def _parse_street_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_address = _parse_street_address(d.pop("streetAddress", UNSET))

        patched_organization_request = cls(
            name=name,
            homepage=homepage,
            description=description,
            postal_address=postal_address,
            street_address=street_address,
        )

        patched_organization_request.additional_properties = d
        return patched_organization_request

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
