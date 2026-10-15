from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AccountVerifyRequest(SdkBaseModel):
    email_address: EmailStr
    """Email address to run the verification for."""


class AccountVerifyRequestDict(TypedDict):
    email_address: EmailStr
