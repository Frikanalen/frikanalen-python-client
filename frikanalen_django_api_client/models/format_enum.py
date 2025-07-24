from enum import Enum


class FormatEnum(str, Enum):
    BROADCAST = "broadcast"
    CLOUDFLARE_ID = "cloudflare_id"
    LARGE_THUMB = "large_thumb"
    MED_THUMB = "med_thumb"
    ORIGINAL = "original"
    SMALL_THUMB = "small_thumb"
    SRT = "srt"
    THEORA = "theora"
    VC1 = "vc1"

    def __str__(self) -> str:
        return str(self.value)
