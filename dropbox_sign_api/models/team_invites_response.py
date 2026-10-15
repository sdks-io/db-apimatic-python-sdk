from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .team_invite_response import TeamInviteResponse, TeamInviteResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TeamInvitesResponse(SdkBaseModel):
    team_invites: list[TeamInviteResponse]
    """Contains a list of team invites and their roles."""

    warnings: Optional[list[WarningResponse]] = UNSET


class TeamInvitesResponseDict(TypedDict):
    team_invites: list[TeamInviteResponseDict]
    warnings: NotRequired[list[WarningResponseDict]]
