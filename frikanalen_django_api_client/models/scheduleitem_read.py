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


T = TypeVar("T", bound="ScheduleitemRead")


@_attrs_define
class ScheduleitemRead:
    """
    Attributes:
        id (int):
        video (ScheduleitemVideo):
        starttime (datetime.datetime):
        endtime (datetime.datetime):
        duration (str):
        schedulereason (Union[Unset, SchedulereasonEnum]): * `1` - Legacy
            * `2` - Administrative
            * `3` - User
            * `4` - Automatic
            * `5` - Jukebox
    """

    id: int
    video: "ScheduleitemVideo"
    starttime: datetime.datetime
    endtime: datetime.datetime
    duration: str
    schedulereason: Union[Unset, SchedulereasonEnum] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        video = self.video.to_dict()

        starttime = self.starttime.isoformat()

        endtime = self.endtime.isoformat()

        duration = self.duration

        schedulereason: Union[Unset, int] = UNSET
        if not isinstance(self.schedulereason, Unset):
            schedulereason = self.schedulereason.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "video": video,
                "starttime": starttime,
                "endtime": endtime,
                "duration": duration,
            }
        )
        if schedulereason is not UNSET:
            field_dict["schedulereason"] = schedulereason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scheduleitem_video import ScheduleitemVideo

        d = dict(src_dict)
        id = d.pop("id")

        video = ScheduleitemVideo.from_dict(d.pop("video"))

        starttime = isoparse(d.pop("starttime"))

        endtime = isoparse(d.pop("endtime"))

        duration = d.pop("duration")

        _schedulereason = d.pop("schedulereason", UNSET)
        schedulereason: Union[Unset, SchedulereasonEnum]
        if isinstance(_schedulereason, Unset):
            schedulereason = UNSET
        else:
            schedulereason = SchedulereasonEnum(_schedulereason)

        scheduleitem_read = cls(
            id=id,
            video=video,
            starttime=starttime,
            endtime=endtime,
            duration=duration,
            schedulereason=schedulereason,
        )

        scheduleitem_read.additional_properties = d
        return scheduleitem_read

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
