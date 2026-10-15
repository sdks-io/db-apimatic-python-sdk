from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ApiAppResponseOauth(SdkBaseModel):
    """An object describing the app's OAuth properties, or null if OAuth is not configured for the app."""

    callback_url: Optional[str] = UNSET
    """The app's OAuth callback URL."""

    secret: OptionalNullable[str] = UNSET
    """The app's OAuth secret, or null if the app does not belong to user."""

    scopes: Optional[list[str]] = UNSET
    """Array of OAuth scopes used by the app."""

    charges_users: Optional[bool] = UNSET
    """Boolean indicating whether the app owner or the account granting permission is billed for OAuth requests."""


class ApiAppResponseOauthDict(TypedDict):
    callback_url: NotRequired[str]
    secret: NotRequired[str | None]
    scopes: NotRequired[list[str]]
    charges_users: NotRequired[bool]
