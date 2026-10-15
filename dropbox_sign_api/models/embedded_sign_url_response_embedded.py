from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class EmbeddedSignUrlResponseEmbedded(SdkBaseModel):
    """An object that contains necessary information to set up embedded signing."""

    sign_url: Optional[str] = UNSET
    """A signature url that can be opened in an iFrame."""

    expires_at: Optional[int] = UNSET
    """The specific time that the the ``sign_url`` link expires, in epoch."""


class EmbeddedSignUrlResponseEmbeddedDict(TypedDict):
    sign_url: NotRequired[str]
    expires_at: NotRequired[int]
