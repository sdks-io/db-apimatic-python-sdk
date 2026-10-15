from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .api_app_response_oauth import ApiAppResponseOauth, ApiAppResponseOauthDict
from .api_app_response_options import ApiAppResponseOptions, ApiAppResponseOptionsDict
from .api_app_response_owner_account import ApiAppResponseOwnerAccount, ApiAppResponseOwnerAccountDict
from .api_app_response_white_labeling_options import (
    ApiAppResponseWhiteLabelingOptions,
    ApiAppResponseWhiteLabelingOptionsDict,
)


class ApiAppResponse(SdkBaseModel):
    """Contains information about an API App."""

    callback_url: OptionalNullable[str] = UNSET
    """The app's callback URL (for events)"""

    client_id: Optional[str] = UNSET
    """The app's client id"""

    created_at: Optional[int] = UNSET
    """The time that the app was created"""

    domains: Optional[list[str]] = UNSET
    """The domain name(s) associated with the app"""

    name: Optional[str] = UNSET
    """The name of the app"""

    is_approved: Optional[bool] = UNSET
    """Boolean to indicate if the app has been approved"""

    oauth: OptionalNullable[ApiAppResponseOauth] = UNSET
    """An object describing the app's OAuth properties, or null if OAuth is not configured for the app."""

    options: OptionalNullable[ApiAppResponseOptions] = UNSET
    """An object with options that override account settings."""

    owner_account: Optional[ApiAppResponseOwnerAccount] = UNSET
    """An object describing the app's owner"""

    white_labeling_options: OptionalNullable[ApiAppResponseWhiteLabelingOptions] = UNSET
    """An object with options to customize the app's signer page"""


class ApiAppResponseDict(TypedDict):
    callback_url: NotRequired[str | None]
    client_id: NotRequired[str]
    created_at: NotRequired[int]
    domains: NotRequired[list[str]]
    name: NotRequired[str]
    is_approved: NotRequired[bool]
    oauth: NotRequired[ApiAppResponseOauthDict | None]
    options: NotRequired[ApiAppResponseOptionsDict | None]
    owner_account: NotRequired[ApiAppResponseOwnerAccountDict]
    white_labeling_options: NotRequired[ApiAppResponseWhiteLabelingOptionsDict | None]
