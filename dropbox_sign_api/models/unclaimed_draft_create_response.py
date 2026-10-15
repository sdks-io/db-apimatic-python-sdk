from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unclaimed_draft_response import UnclaimedDraftResponse, UnclaimedDraftResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class UnclaimedDraftCreateResponse(SdkBaseModel):
    unclaimed_draft: UnclaimedDraftResponse
    """A group of documents that a user can take ownership of via the claim URL."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class UnclaimedDraftCreateResponseDict(TypedDict):
    unclaimed_draft: UnclaimedDraftResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
