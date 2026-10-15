from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SubTeamResponse(SdkBaseModel):
    team_id: Optional[str] = UNSET
    """The id of a team"""

    name: Optional[str] = UNSET
    """The name of a team"""


class SubTeamResponseDict(TypedDict):
    team_id: NotRequired[str]
    name: NotRequired[str]
