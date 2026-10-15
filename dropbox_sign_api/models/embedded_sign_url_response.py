from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embedded_sign_url_response_embedded import EmbeddedSignUrlResponseEmbedded, EmbeddedSignUrlResponseEmbeddedDict
from .warning_response import WarningResponse, WarningResponseDict


class EmbeddedSignUrlResponse(SdkBaseModel):
    embedded: EmbeddedSignUrlResponseEmbedded
    """An object that contains necessary information to set up embedded signing."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class EmbeddedSignUrlResponseDict(TypedDict):
    embedded: EmbeddedSignUrlResponseEmbeddedDict
    warnings: NotRequired[list[WarningResponseDict]]
