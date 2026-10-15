from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignatureRequestRemindRequest(SdkBaseModel):
    email_address: EmailStr
    """The email address of the signer to send a reminder to."""

    name: Optional[str] = UNSET
    """The name of the signer to send a reminder to. Include if two or more signers share an email address."""


class SignatureRequestRemindRequestDict(TypedDict):
    email_address: EmailStr
    name: NotRequired[str]
