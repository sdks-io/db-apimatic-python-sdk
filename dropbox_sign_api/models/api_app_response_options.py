from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiAppResponseOptions(SdkBaseModel):
    """An object with options that override account settings."""

    can_insert_everywhere: Optional[bool] = UNSET
    """Boolean denoting if signers can "Insert Everywhere" in one click while signing a document"""


class ApiAppResponseOptionsDict(TypedDict):
    can_insert_everywhere: NotRequired[bool]
