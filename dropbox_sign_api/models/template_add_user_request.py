from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateAddUserRequest(SdkBaseModel):
    account_id: Optional[str] = UNSET
    """The id of the Account to give access to the Template. **NOTE:** The account id prevails if email address is also
    provided."""

    email_address: Optional[EmailStr] = UNSET
    """The email address of the Account to give access to the Template. **NOTE:** The account id prevails if it is also
    provided."""

    skip_notification: bool = False
    """If set to ``true``, the user does not receive an email notification when a template has been shared with them.
    Defaults to ``false``."""


class TemplateAddUserRequestDict(TypedDict):
    account_id: NotRequired[str]
    email_address: NotRequired[EmailStr]
    skip_notification: NotRequired[bool]
