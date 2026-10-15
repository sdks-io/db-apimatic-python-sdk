from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.new_role import NewRoleOrStr


class TeamRemoveMemberRequest(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """**account_id** or **email_address** is required. If both are provided, the account id prevails.

    Account id to remove from your Team."""

    email_address: Optional[EmailStr] = UNSET
    """**account_id** or **email_address** is required. If both are provided, the account id prevails.

    Email address of the Account to remove from your Team."""

    new_owner_email_address: Optional[EmailStr] = UNSET
    """The email address of an Account on this Team to receive all documents, templates, and API apps (if applicable)
    from the removed Account. If not provided, and on an Enterprise plan, this data will remain with the removed
    Account.

    **NOTE:** Only available for Enterprise plans."""

    new_team_id: Optional[str] = UNSET
    """Id of the new Team."""

    new_role: Optional[NewRoleOrStr] = UNSET
    """A new role member will take in a new Team.

    **NOTE:** This parameter is used only if ``new_team_id`` is provided."""


class TeamRemoveMemberRequestDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[EmailStr]
    new_owner_email_address: NotRequired[EmailStr]
    new_team_id: NotRequired[str]
    new_role: NotRequired[NewRoleOrStr]
