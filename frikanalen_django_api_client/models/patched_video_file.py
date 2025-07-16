import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedVideoFile")


@_attrs_define
class PatchedVideoFile:
    """
    Attributes:
        id (Union[Unset, int]):
        video (Union[Unset, int]):
        format_ (Union[Unset, int]):
        filename (Union[Unset, str]):
        created_time (Union[None, Unset, datetime.datetime]): Time the video file was created
        integrated_lufs (Union[None, Unset, float]):
        truepeak_lufs (Union[None, Unset, float]):
    """

    id: Union[Unset, int] = UNSET
    video: Union[Unset, int] = UNSET
    format_: Union[Unset, int] = UNSET
    filename: Union[Unset, str] = UNSET
    created_time: Union[None, Unset, datetime.datetime] = UNSET
    integrated_lufs: Union[None, Unset, float] = UNSET
    truepeak_lufs: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        video = self.video

        format_ = self.format_

        filename = self.filename

        created_time: Union[None, Unset, str]
        if isinstance(self.created_time, Unset):
            created_time = UNSET
        elif isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

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
        if id is not UNSET:
            field_dict["id"] = id
        if video is not UNSET:
            field_dict["video"] = video
        if format_ is not UNSET:
            field_dict["format"] = format_
        if filename is not UNSET:
            field_dict["filename"] = filename
        if created_time is not UNSET:
            field_dict["createdTime"] = created_time
        if integrated_lufs is not UNSET:
            field_dict["integratedLufs"] = integrated_lufs
        if truepeak_lufs is not UNSET:
            field_dict["truepeakLufs"] = truepeak_lufs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        video = d.pop("video", UNSET)

        format_ = d.pop("format", UNSET)

        filename = d.pop("filename", UNSET)

        def _parse_created_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = isoparse(data)

                return created_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_time = _parse_created_time(d.pop("createdTime", UNSET))

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

        patched_video_file = cls(
            id=id,
            video=video,
            format_=format_,
            filename=filename,
            created_time=created_time,
            integrated_lufs=integrated_lufs,
            truepeak_lufs=truepeak_lufs,
        )

        patched_video_file.additional_properties = d
        return patched_video_file

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
