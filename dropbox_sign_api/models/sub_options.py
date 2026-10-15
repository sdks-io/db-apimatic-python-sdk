from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SubOptions(SdkBaseModel):
    """Additional options supported by API App."""

    can_insert_everywhere: bool = False
    """Determines if signers can use "Insert Everywhere" when signing a document."""


class SubOptionsDict(TypedDict):
    can_insert_everywhere: NotRequired[bool]
