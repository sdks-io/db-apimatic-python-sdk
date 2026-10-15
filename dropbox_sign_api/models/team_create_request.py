from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class TeamCreateRequest(SdkBaseModel):
    name: str = "Untitled Team"
    """The name of your Team."""


class TeamCreateRequestDict(TypedDict):
    name: NotRequired[str]
