from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TeamInviteResponse(SdkBaseModel):
    email_address: Optional[str] = UNSET
    """Email address of the user invited to this team."""

    team_id: Optional[str] = UNSET
    """Id of the team."""

    role: Optional[str] = UNSET
    """Role of the user invited to this team."""

    sent_at: Optional[int] = UNSET
    """Timestamp when the invitation was sent."""

    redeemed_at: Optional[int] = UNSET
    """Timestamp when the invitation was redeemed."""

    expires_at: Optional[int] = UNSET
    """Timestamp when the invitation is expiring."""


class TeamInviteResponseDict(TypedDict):
    email_address: NotRequired[str]
    team_id: NotRequired[str]
    role: NotRequired[str]
    sent_at: NotRequired[int]
    redeemed_at: NotRequired[int]
    expires_at: NotRequired[int]
