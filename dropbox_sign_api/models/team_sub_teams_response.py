from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .list_info_response import ListInfoResponse, ListInfoResponseDict
from .sub_team_response import SubTeamResponse, SubTeamResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TeamSubTeamsResponse(SdkBaseModel):
    sub_teams: list[SubTeamResponse]
    """Contains a list with sub teams."""

    list_info: ListInfoResponse
    """Contains pagination information about the data returned."""

    warnings: Optional[list[WarningResponse]] = UNSET


class TeamSubTeamsResponseDict(TypedDict):
    sub_teams: list[SubTeamResponseDict]
    list_info: ListInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
