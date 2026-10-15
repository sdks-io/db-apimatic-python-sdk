from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel
from .sub_oauth import SubOauth, SubOauthDict
from .sub_options import SubOptions, SubOptionsDict
from .sub_white_labeling_options import SubWhiteLabelingOptions, SubWhiteLabelingOptionsDict


class ApiAppCreateRequest(SdkBaseModel):
    callback_url: Optional[str] = UNSET
    """The URL at which the ApiApp should receive event callbacks."""

    custom_logo_file: Optional[FileResponse] = UNSET
    """An image file to use as a custom logo in embedded contexts. (Only applies to some API plans)"""

    domains: list[str]
    """The domain names the ApiApp will be associated with."""

    name: str
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


class ApiAppCreateRequestDict(TypedDict):
    callback_url: NotRequired[str]
    custom_logo_file: NotRequired[FileResponse]
    domains: list[str]
    name: str
    oauth: NotRequired[SubOauthDict]
    options: NotRequired[SubOptionsDict]
    white_labeling_options: NotRequired[SubWhiteLabelingOptionsDict]
