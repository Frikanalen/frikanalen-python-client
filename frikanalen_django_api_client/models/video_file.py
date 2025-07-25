import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.format_enum import FormatEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video import Video


T = TypeVar("T", bound="VideoFile")


@_attrs_define
class VideoFile:
    """
    Attributes:
        id (int):
        video (Video):
        created_time (Union[None, datetime.datetime]): Time the video file was created
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

    id: int
    video: "Video"
    created_time: Union[None, datetime.datetime]
    format_: FormatEnum
    filename: str
    integrated_lufs: Union[None, Unset, float] = UNSET
    truepeak_lufs: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        video = self.video.to_dict()

        created_time: Union[None, str]
        if isinstance(self.created_time, datetime.datetime):
            created_time = self.created_time.isoformat()
        else:
            created_time = self.created_time

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
                "id": id,
                "video": video,
                "createdTime": created_time,
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
        from ..models.video import Video

        d = dict(src_dict)
        id = d.pop("id")

        video = Video.from_dict(d.pop("video"))

        def _parse_created_time(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_time_type_0 = isoparse(data)

                return created_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        created_time = _parse_created_time(d.pop("createdTime"))

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

        video_file = cls(
            id=id,
            video=video,
            created_time=created_time,
            format_=format_,
            filename=filename,
            integrated_lufs=integrated_lufs,
            truepeak_lufs=truepeak_lufs,
        )

        video_file.additional_properties = d
        return video_file

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
