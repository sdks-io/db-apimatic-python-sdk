from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class OauthTokenResponse(SdkBaseModel):
    access_token: Optional[str] = UNSET
    token_type: Optional[str] = UNSET
    refresh_token: Optional[str] = UNSET
    expires_in: Optional[int] = UNSET
    """Number of seconds until the ``access_token`` expires. Uses epoch time."""

    state: OptionalNullable[str] = UNSET


class OauthTokenResponseDict(TypedDict):
    access_token: NotRequired[str]
    token_type: NotRequired[str]
    refresh_token: NotRequired[str]
    expires_in: NotRequired[int]
    state: NotRequired[str | None]
