from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .embedded_edit_url_response_embedded import EmbeddedEditUrlResponseEmbedded, EmbeddedEditUrlResponseEmbeddedDict
from .warning_response import WarningResponse, WarningResponseDict


class EmbeddedEditUrlResponse(SdkBaseModel):
    embedded: EmbeddedEditUrlResponseEmbedded
    """An embedded template object."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class EmbeddedEditUrlResponseDict(TypedDict):
    embedded: EmbeddedEditUrlResponseEmbeddedDict
    warnings: NotRequired[list[WarningResponseDict]]
