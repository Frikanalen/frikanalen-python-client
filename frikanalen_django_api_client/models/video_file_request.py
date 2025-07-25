from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.format_enum import FormatEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoFileRequest")


@_attrs_define
class VideoFileRequest:
    """
    Attributes:
        video_id (int):
        format_ (FormatEnum): * `large_thumb` - large_thumb
            * `broadcast` - broadcast
            * `vc1` - vc1
            * `med_thumb` - med_thumb
            * `small_thumb` - small_thumb
            * `original` - original
            * `theora` - theora
            * `srt` - srt
            * `cloudflare_id` - cloudflare_id
        filename (str):
        integrated_lufs (Union[None, Unset, float]):
        truepeak_lufs (Union[None, Unset, float]):
    """

    video_id: int
    format_: FormatEnum
    filename: str
    integrated_lufs: Union[None, Unset, float] = UNSET
    truepeak_lufs: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video_id = self.video_id

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
        field_dict.update(
            {
                "videoId": video_id,
                "format": format_,
                "filename": filename,
            }
        )
        if integrated_lufs is not UNSET:
            field_dict["integratedLufs"] = integrated_lufs
        if truepeak_lufs is not UNSET:
            field_dict["truepeakLufs"] = truepeak_lufs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        video_id = d.pop("videoId")

        format_ = FormatEnum(d.pop("format"))

        filename = d.pop("filename")

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

        video_file_request = cls(
            video_id=video_id,
            format_=format_,
            filename=filename,
            integrated_lufs=integrated_lufs,
            truepeak_lufs=truepeak_lufs,
        )

        video_file_request.additional_properties = d
        return video_file_request

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
