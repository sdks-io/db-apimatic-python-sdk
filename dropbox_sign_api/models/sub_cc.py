from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubCc(SdkBaseModel):
    role: str
    """Must match an existing CC role in chosen Template(s). Multiple CC recipients cannot share the same CC role."""

    email_address: EmailStr
    """The email address of the CC recipient."""


class SubCcDict(TypedDict):
    role: str
    email_address: EmailStr
