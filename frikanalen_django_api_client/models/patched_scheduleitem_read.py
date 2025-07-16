import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schedulereason_enum import SchedulereasonEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.scheduleitem_video import ScheduleitemVideo


T = TypeVar("T", bound="PatchedScheduleitemRead")


@_attrs_define
class PatchedScheduleitemRead:
    """
    Attributes:
        id (Union[Unset, int]):
        video (Union[Unset, ScheduleitemVideo]):
        schedulereason (Union[Unset, SchedulereasonEnum]): * `1` - Legacy
            * `2` - Administrative
            * `3` - User
            * `4` - Automatic
            * `5` - Jukebox
        starttime (Union[Unset, datetime.datetime]):
        endtime (Union[Unset, datetime.datetime]):
        duration (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    video: Union[Unset, "ScheduleitemVideo"] = UNSET
    schedulereason: Union[Unset, SchedulereasonEnum] = UNSET
    starttime: Union[Unset, datetime.datetime] = UNSET
    endtime: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        video: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.video, Unset):
            video = self.video.to_dict()

        schedulereason: Union[Unset, int] = UNSET
        if not isinstance(self.schedulereason, Unset):
            schedulereason = self.schedulereason.value

        starttime: Union[Unset, str] = UNSET
        if not isinstance(self.starttime, Unset):
            starttime = self.starttime.isoformat()

        endtime: Union[Unset, str] = UNSET
        if not isinstance(self.endtime, Unset):
            endtime = self.endtime.isoformat()

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if video is not UNSET:
            field_dict["video"] = video
        if schedulereason is not UNSET:
            field_dict["schedulereason"] = schedulereason
        if starttime is not UNSET:
            field_dict["starttime"] = starttime
        if endtime is not UNSET:
            field_dict["endtime"] = endtime
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scheduleitem_video import ScheduleitemVideo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _video = d.pop("video", UNSET)
        video: Union[Unset, ScheduleitemVideo]
        if isinstance(_video, Unset):
            video = UNSET
        else:
            video = ScheduleitemVideo.from_dict(_video)

        _schedulereason = d.pop("schedulereason", UNSET)
        schedulereason: Union[Unset, SchedulereasonEnum]
        if isinstance(_schedulereason, Unset):
            schedulereason = UNSET
        else:
            schedulereason = SchedulereasonEnum(_schedulereason)

        _starttime = d.pop("starttime", UNSET)
        starttime: Union[Unset, datetime.datetime]
        if isinstance(_starttime, Unset):
            starttime = UNSET
        else:
            starttime = isoparse(_starttime)

        _endtime = d.pop("endtime", UNSET)
        endtime: Union[Unset, datetime.datetime]
        if isinstance(_endtime, Unset):
            endtime = UNSET
        else:
            endtime = isoparse(_endtime)

        duration = d.pop("duration", UNSET)

        patched_scheduleitem_read = cls(
            id=id,
            video=video,
            schedulereason=schedulereason,
            starttime=starttime,
            endtime=endtime,
            duration=duration,
        )

        patched_scheduleitem_read.additional_properties = d
        return patched_scheduleitem_read

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
