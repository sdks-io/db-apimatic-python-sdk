from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubUnclaimedDraftTemplateSigner(SdkBaseModel):
    role: str
    """Must match an existing role in chosen Template(s)."""

    name: str
    """The name of the signer filling the role of ``role``."""

    email_address: EmailStr
    """The email address of the signer filling the role of ``role``."""


class SubUnclaimedDraftTemplateSignerDict(TypedDict):
    role: str
    name: str
    email_address: EmailStr
