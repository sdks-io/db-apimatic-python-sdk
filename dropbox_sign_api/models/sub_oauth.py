from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.scope import ScopeOrStr


class SubOauth(SdkBaseModel):
    """OAuth related parameters."""

    callback_url: Optional[str] = UNSET
    """The callback URL to be used for OAuth flows. (Required if ``oauth[scopes]`` is provided)"""

    scopes: Optional[list[ScopeOrStr]] = UNSET
    """A list of `OAuth scopes </api/reference/tag/OAuth>`__ to be granted to the app. (Required if
    ``oauth[callback_url]`` is provided)."""


class SubOauthDict(TypedDict):
    callback_url: NotRequired[str]
    scopes: NotRequired[list[ScopeOrStr]]
