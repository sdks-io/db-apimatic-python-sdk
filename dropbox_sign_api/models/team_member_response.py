from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TeamMemberResponse(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """Account id of the team member."""

    email_address: Optional[str] = UNSET
    """Email address of the team member."""

    role: Optional[str] = UNSET
    """The specific role a member has on the team."""


class TeamMemberResponseDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[str]
    role: NotRequired[str]
