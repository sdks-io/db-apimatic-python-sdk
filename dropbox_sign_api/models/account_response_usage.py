from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AccountResponseUsage(SdkBaseModel):
    """Details concerning monthly usage"""

    fax_pages_sent: OptionalNullable[int] = UNSET
    """Number of fax pages sent"""


class AccountResponseUsageDict(TypedDict):
    fax_pages_sent: NotRequired[int | None]
