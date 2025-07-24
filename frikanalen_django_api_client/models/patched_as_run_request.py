import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedAsRunRequest")


@_attrs_define
class PatchedAsRunRequest:
    """
    Attributes:
        video (Union[None, Unset, int]): Points to the Video which was played if there is one. Can be empty if something
            other than a video was played. The field is mutually exclusive with `programName`.
        program_name (Union[Unset, str]): A free form text input saying what was played. If `video` is set, this field
            should not be set. Examples of where you'd use this field is e.g. when broadcasting live. Defaults to the empty
            string.
        playout (Union[Unset, str]): The playout this entry corresponds with. This will almost always be 'main' which it
            defaults to.
        played_at (Union[Unset, datetime.datetime]): Time when the playout started. Defaults to now.
        in_ms (Union[Unset, int]): The inpoint where the video/stream was started at. In milliseconds. Normally 0 which
            it defaults to.
        out_ms (Union[None, Unset, int]): The outpoint where the video/stream stopped. This would often be the duration
            of the video, or how long we live streamed a particular URL. Can be null (None) if this is 'currently
            happening'.
    """

    video: Union[None, Unset, int] = UNSET
    program_name: Union[Unset, str] = UNSET
    playout: Union[Unset, str] = UNSET
    played_at: Union[Unset, datetime.datetime] = UNSET
    in_ms: Union[Unset, int] = UNSET
    out_ms: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video: Union[None, Unset, int]
        if isinstance(self.video, Unset):
            video = UNSET
        else:
            video = self.video

        program_name = self.program_name

        playout = self.playout

        played_at: Union[Unset, str] = UNSET
        if not isinstance(self.played_at, Unset):
            played_at = self.played_at.isoformat()

        in_ms = self.in_ms

        out_ms: Union[None, Unset, int]
        if isinstance(self.out_ms, Unset):
            out_ms = UNSET
        else:
            out_ms = self.out_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video is not UNSET:
            field_dict["video"] = video
        if program_name is not UNSET:
            field_dict["programName"] = program_name
        if playout is not UNSET:
            field_dict["playout"] = playout
        if played_at is not UNSET:
            field_dict["playedAt"] = played_at
        if in_ms is not UNSET:
            field_dict["inMs"] = in_ms
        if out_ms is not UNSET:
            field_dict["outMs"] = out_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_video(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        video = _parse_video(d.pop("video", UNSET))

        program_name = d.pop("programName", UNSET)

        playout = d.pop("playout", UNSET)

        _played_at = d.pop("playedAt", UNSET)
        played_at: Union[Unset, datetime.datetime]
        if isinstance(_played_at, Unset):
            played_at = UNSET
        else:
            played_at = isoparse(_played_at)

        in_ms = d.pop("inMs", UNSET)

        def _parse_out_ms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        out_ms = _parse_out_ms(d.pop("outMs", UNSET))

        patched_as_run_request = cls(
            video=video,
            program_name=program_name,
            playout=playout,
            played_at=played_at,
            in_ms=in_ms,
            out_ms=out_ms,
        )

        patched_as_run_request.additional_properties = d
        return patched_as_run_request

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
