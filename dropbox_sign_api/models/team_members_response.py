from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .team_member_response import TeamMemberResponse, TeamMemberResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TeamMembersResponse(SdkBaseModel):
    team_members: list[TeamMemberResponse]
    """Contains a list of team members and their roles for a specific team."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    warnings: Optional[list[WarningResponse]] = UNSET


class TeamMembersResponseDict(TypedDict):
    team_members: list[TeamMemberResponseDict]
    list_info: ListInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
