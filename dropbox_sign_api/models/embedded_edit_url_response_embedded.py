from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EmbeddedEditUrlResponseEmbedded(SdkBaseModel):
    """An embedded template object."""

    edit_url: Optional[str] = UNSET
    """A template url that can be opened in an iFrame."""

    expires_at: Optional[int] = UNSET
    """The specific time that the the ``edit_url`` link expires, in epoch."""


class EmbeddedEditUrlResponseEmbeddedDict(TypedDict):
    edit_url: NotRequired[str]
    expires_at: NotRequired[int]
