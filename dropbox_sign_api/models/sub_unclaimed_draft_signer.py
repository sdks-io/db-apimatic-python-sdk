from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SubUnclaimedDraftSigner(SdkBaseModel):
    email_address: EmailStr
    """The email address of the signer."""

    name: str
    """The name of the signer."""

    order: OptionalNullable[int] = UNSET
    """The order the signer is required to sign in."""


class SubUnclaimedDraftSignerDict(TypedDict):
    email_address: EmailStr
    name: str
    order: NotRequired[int | None]
