from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class OauthTokenGenerateRequest(SdkBaseModel):
    client_id: str
    """The client id of the app requesting authorization."""

    client_secret: str
    """The secret token of your app."""

    code: str
    """The code passed to your callback when the user granted access."""

    grant_type: str = "authorization_code"
    """When generating a new token use ``authorization_code``."""

    state: str
    """Same as the state you specified earlier."""


class OauthTokenGenerateRequestDict(TypedDict):
    client_id: str
    client_secret: str
    code: str
    grant_type: str
    state: str
