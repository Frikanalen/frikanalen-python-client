import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="NewUser")


@_attrs_define
class NewUser:
    """
    Attributes:
        id (int):
        email (str):
        first_name (str):
        last_name (str):
        date_of_birth (datetime.date):
        password (str):
    """

    id: int
    email: str
    first_name: str
    last_name: str
    date_of_birth: datetime.date
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        date_of_birth = self.date_of_birth.isoformat()

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "firstName": first_name,
                "lastName": last_name,
                "dateOfBirth": date_of_birth,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        date_of_birth = isoparse(d.pop("dateOfBirth")).date()

        password = d.pop("password")

        new_user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            password=password,
        )

        new_user.additional_properties = d
        return new_user

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
