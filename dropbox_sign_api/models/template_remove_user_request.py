from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateRemoveUserRequest(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """The id or email address of the Account to remove access to the Template. The account id prevails if both are
    provided."""

    email_address: Optional[EmailStr] = UNSET
    """The id or email address of the Account to remove access to the Template. The account id prevails if both are
    provided."""


class TemplateRemoveUserRequestDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[EmailStr]
