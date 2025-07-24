import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUserRequest")


@_attrs_define
class PatchedUserRequest:
    """
    Attributes:
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        date_of_birth (Union[None, Unset, datetime.date]):
        phone_number (Union[Unset, str]): Phone number at which this user can be reached
        password (Union[Unset, str]):
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    date_of_birth: Union[None, Unset, datetime.date] = UNSET
    phone_number: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        date_of_birth: Union[None, Unset, str]
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        phone_number = self.phone_number

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        def _parse_date_of_birth(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_of_birth_type_0 = isoparse(data).date()

                return date_of_birth_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_of_birth = _parse_date_of_birth(d.pop("dateOfBirth", UNSET))

        phone_number = d.pop("phoneNumber", UNSET)

        password = d.pop("password", UNSET)

        patched_user_request = cls(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            password=password,
        )

        patched_user_request.additional_properties = d
        return patched_user_request

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
