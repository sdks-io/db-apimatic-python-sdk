from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .team_parent_response import TeamParentResponse, TeamParentResponseDict


class TeamInfoResponse(SdkBaseModel):
    team_id: Optional[str] = UNSET
    """The id of a team"""

    team_parent: OptionalNullable[TeamParentResponse] = UNSET
    """Information about the parent team if a team has one, set to ``null`` otherwise."""

    name: Optional[str] = UNSET
    """The name of a team"""

    num_members: Optional[int] = UNSET
    """Number of members within a team"""

    num_sub_teams: Optional[int] = UNSET
    """Number of sub teams within a team"""


class TeamInfoResponseDict(TypedDict):
    team_id: NotRequired[str]
    team_parent: NotRequired[TeamParentResponseDict | None]
    name: NotRequired[str]
    num_members: NotRequired[int]
    num_sub_teams: NotRequired[int]
