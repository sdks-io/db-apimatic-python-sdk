from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class OauthTokenRefreshRequest(SdkBaseModel):
    grant_type: str = "refresh_token"
    """When refreshing an existing token use ``refresh_token``."""

    refresh_token: str
    """The token provided when you got the expired access token."""

    client_id: Optional[str] = UNSET
    """The client ID for your API app. Required for new API apps. To enhance security, we recommend making it required
    for existing apps in your app settings."""

    client_secret: Optional[str] = UNSET
    """The client secret for your API app. Required for new API apps. To enhance security, we recommend making it
    required for existing apps in your app settings."""


class OauthTokenRefreshRequestDict(TypedDict):
    grant_type: str
    refresh_token: str
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
