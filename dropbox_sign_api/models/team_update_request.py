from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TeamUpdateRequest(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of your Team."""


class TeamUpdateRequestDict(TypedDict):
    name: NotRequired[str]
