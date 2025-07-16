import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedUser")


@_attrs_define
class PatchedUser:
    """
    Attributes:
        id (Union[Unset, int]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        date_joined (Union[Unset, datetime.datetime]):
        is_staff (Union[Unset, str]):
        date_of_birth (Union[None, Unset, datetime.date]):
        phone_number (Union[Unset, str]): Phone number at which this user can be reached
        organization_roles (Union[Unset, str]):
        password (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    is_staff: Union[Unset, str] = UNSET
    date_of_birth: Union[None, Unset, datetime.date] = UNSET
    phone_number: Union[Unset, str] = UNSET
    organization_roles: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        date_joined: Union[Unset, str] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        is_staff = self.is_staff

        date_of_birth: Union[None, Unset, str]
        if isinstance(self.date_of_birth, Unset):
            date_of_birth = UNSET
        elif isinstance(self.date_of_birth, datetime.date):
            date_of_birth = self.date_of_birth.isoformat()
        else:
            date_of_birth = self.date_of_birth

        phone_number = self.phone_number

        organization_roles = self.organization_roles

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if date_joined is not UNSET:
            field_dict["dateJoined"] = date_joined
        if is_staff is not UNSET:
            field_dict["isStaff"] = is_staff
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if organization_roles is not UNSET:
            field_dict["organizationRoles"] = organization_roles
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        email = d.pop("email", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        _date_joined = d.pop("dateJoined", UNSET)
        date_joined: Union[Unset, datetime.datetime]
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        is_staff = d.pop("isStaff", UNSET)

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

        organization_roles = d.pop("organizationRoles", UNSET)

        password = d.pop("password", UNSET)

        patched_user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            date_joined=date_joined,
            is_staff=is_staff,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            organization_roles=organization_roles,
            password=password,
        )

        patched_user.additional_properties = d
        return patched_user

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
