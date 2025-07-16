import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.schedulereason_enum import SchedulereasonEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleitemModify")


@_attrs_define
class ScheduleitemModify:
    """
    Attributes:
        id (int):
        starttime (datetime.datetime):
        endtime (datetime.datetime):
        duration (str):
        video (Union[None, Unset, int]):
        schedulereason (Union[Unset, SchedulereasonEnum]): * `1` - Legacy
            * `2` - Administrative
            * `3` - User
            * `4` - Automatic
            * `5` - Jukebox
    """

    id: int
    starttime: datetime.datetime
    endtime: datetime.datetime
    duration: str
    video: Union[None, Unset, int] = UNSET
    schedulereason: Union[Unset, SchedulereasonEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        starttime = self.starttime.isoformat()

        endtime = self.endtime.isoformat()

        duration = self.duration

        video: Union[None, Unset, int]
        if isinstance(self.video, Unset):
            video = UNSET
        else:
            video = self.video

        schedulereason: Union[Unset, int] = UNSET
        if not isinstance(self.schedulereason, Unset):
            schedulereason = self.schedulereason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "starttime": starttime,
                "endtime": endtime,
                "duration": duration,
            }
        )
        if video is not UNSET:
            field_dict["video"] = video
        if schedulereason is not UNSET:
            field_dict["schedulereason"] = schedulereason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        starttime = isoparse(d.pop("starttime"))

        endtime = isoparse(d.pop("endtime"))

        duration = d.pop("duration")

        def _parse_video(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        video = _parse_video(d.pop("video", UNSET))

        _schedulereason = d.pop("schedulereason", UNSET)
        schedulereason: Union[Unset, SchedulereasonEnum]
        if isinstance(_schedulereason, Unset):
            schedulereason = UNSET
        else:
            schedulereason = SchedulereasonEnum(_schedulereason)

        scheduleitem_modify = cls(
            id=id,
            starttime=starttime,
            endtime=endtime,
            duration=duration,
            video=video,
            schedulereason=schedulereason,
        )

        scheduleitem_modify.additional_properties = d
        return scheduleitem_modify

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
