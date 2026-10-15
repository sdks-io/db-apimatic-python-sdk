from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .team_response import TeamResponse, TeamResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TeamGetResponse(SdkBaseModel):
    team: TeamResponse
    """Contains information about your team and its members"""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TeamGetResponseDict(TypedDict):
    team: TeamResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
