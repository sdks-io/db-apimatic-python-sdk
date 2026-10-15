from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.role import RoleOrStr


class TeamAddMemberRequest(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """``account_id`` or ``email_address`` is required. If both are provided, the account id prevails.

    Account id of the user to invite to your Team."""

    email_address: Optional[EmailStr] = UNSET
    """``account_id`` or ``email_address`` is required, If both are provided, the account id prevails.

    Email address of the user to invite to your Team."""

    role: Optional[RoleOrStr] = UNSET
    """A role member will take in a new Team.

    **NOTE:** This parameter is used only if ``team_id`` is provided."""


class TeamAddMemberRequestDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[EmailStr]
    role: NotRequired[RoleOrStr]
