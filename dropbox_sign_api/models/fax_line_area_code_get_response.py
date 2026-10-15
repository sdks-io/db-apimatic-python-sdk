from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FaxLineAreaCodeGetResponse(SdkBaseModel):
    area_codes: list[int]


class FaxLineAreaCodeGetResponseDict(TypedDict):
    area_codes: list[int]
