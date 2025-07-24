from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.format_enum import FormatEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVideoFileRequest")


@_attrs_define
class PatchedVideoFileRequest:
    """
    Attributes:
        video_id (Union[Unset, int]):
        format_ (Union[Unset, FormatEnum]):
        filename (Union[Unset, str]):
        integrated_lufs (Union[None, Unset, float]):
        truepeak_lufs (Union[None, Unset, float]):
    """

    video_id: Union[Unset, int] = UNSET
    format_: Union[Unset, FormatEnum] = UNSET
    filename: Union[Unset, str] = UNSET
    integrated_lufs: Union[None, Unset, float] = UNSET
    truepeak_lufs: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video_id = self.video_id

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        filename = self.filename

        integrated_lufs: Union[None, Unset, float]
        if isinstance(self.integrated_lufs, Unset):
            integrated_lufs = UNSET
        else:
            integrated_lufs = self.integrated_lufs

        truepeak_lufs: Union[None, Unset, float]
        if isinstance(self.truepeak_lufs, Unset):
            truepeak_lufs = UNSET
        else:
            truepeak_lufs = self.truepeak_lufs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_id is not UNSET:
            field_dict["videoId"] = video_id
        if format_ is not UNSET:
            field_dict["format"] = format_
        if filename is not UNSET:
            field_dict["filename"] = filename
        if integrated_lufs is not UNSET:
            field_dict["integratedLufs"] = integrated_lufs
        if truepeak_lufs is not UNSET:
            field_dict["truepeakLufs"] = truepeak_lufs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        video_id = d.pop("videoId", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, FormatEnum]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = FormatEnum(_format_)

        filename = d.pop("filename", UNSET)

        def _parse_integrated_lufs(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        integrated_lufs = _parse_integrated_lufs(d.pop("integratedLufs", UNSET))

        def _parse_truepeak_lufs(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        truepeak_lufs = _parse_truepeak_lufs(d.pop("truepeakLufs", UNSET))

        patched_video_file_request = cls(
            video_id=video_id,
            format_=format_,
            filename=filename,
            integrated_lufs=integrated_lufs,
            truepeak_lufs=truepeak_lufs,
        )

        patched_video_file_request.additional_properties = d
        return patched_video_file_request

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
