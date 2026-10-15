from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .team_info_response import TeamInfoResponse, TeamInfoResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TeamGetInfoResponse(SdkBaseModel):
    team: TeamInfoResponse
    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TeamGetInfoResponseDict(TypedDict):
    team: TeamInfoResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
