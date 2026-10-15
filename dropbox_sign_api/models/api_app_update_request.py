from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel
from .sub_oauth import SubOauth, SubOauthDict
from .sub_options import SubOptions, SubOptionsDict
from .sub_white_labeling_options import SubWhiteLabelingOptions, SubWhiteLabelingOptionsDict


class ApiAppUpdateRequest(SdkBaseModel):
    callback_url: Optional[str] = UNSET
    """The URL at which the API App should receive event callbacks."""

    custom_logo_file: Optional[FileResponse] = UNSET
    """An image file to use as a custom logo in embedded contexts. (Only applies to some API plans)"""

    domains: Optional[list[str]] = UNSET
    """The domain names the ApiApp will be associated with."""

    name: Optional[str] = UNSET
    """The name you want to assign to the ApiApp."""

    oauth: Optional[SubOauth] = UNSET
    """OAuth related parameters."""

    options: Optional[SubOptions] = UNSET
    """Additional options supported by API App."""

    white_labeling_options: Optional[SubWhiteLabelingOptions] = UNSET
    """An array of elements and values serialized to a string, to be used to customize the app's signer page. (Only
    applies to some API plans)

    Take a look at our `white labeling guide <https://developers.hellosign.com/api/reference/premium-branding/>`__ to
    learn more."""


class ApiAppUpdateRequestDict(TypedDict):
    callback_url: NotRequired[str]
    custom_logo_file: NotRequired[FileResponse]
    domains: NotRequired[list[str]]
    name: NotRequired[str]
    oauth: NotRequired[SubOauthDict]
    options: NotRequired[SubOptionsDict]
    white_labeling_options: NotRequired[SubWhiteLabelingOptionsDict]
