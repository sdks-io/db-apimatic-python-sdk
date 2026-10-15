from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AccountCreateRequest(SdkBaseModel):
    client_id: Optional[str] = UNSET
    """Used when creating a new account with OAuth authorization.

    See `OAuth 2.0 Authorization <https://app.hellosign.com/api/oauthWalkthrough#OAuthAuthorization>`__"""

    client_secret: Optional[str] = UNSET
    """Used when creating a new account with OAuth authorization.

    See `OAuth 2.0 Authorization <https://app.hellosign.com/api/oauthWalkthrough#OAuthAuthorization>`__"""

    email_address: EmailStr
    """The email address which will be associated with the new Account."""

    locale: Optional[str] = UNSET
    """The locale used in this Account. Check out the list of `supported locales
    </api/reference/constants/#supported-locales>`__ to learn more about the possible values."""


class AccountCreateRequestDict(TypedDict):
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    email_address: EmailStr
    locale: NotRequired[str]
