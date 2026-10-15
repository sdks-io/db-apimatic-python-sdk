from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.legal_version import LegalVersion, LegalVersionOrStr


class SubWhiteLabelingOptions(SdkBaseModel):
    """An array of elements and values serialized to a string, to be used to customize the app's signer page. (Only
    applies to some API plans)

    Take a look at our `white labeling guide <https://developers.hellosign.com/api/reference/premium-branding/>`__ to
    learn more."""

    header_background_color: str = "#1a1a1a"
    legal_version: LegalVersionOrStr = LegalVersion.TERMS1
    link_color: str = "#0061FE"
    page_background_color: str = "#f7f8f9"
    primary_button_color: str = "#0061FE"
    primary_button_color_hover: str = "#0061FE"
    primary_button_text_color: str = "#ffffff"
    primary_button_text_color_hover: str = "#ffffff"
    secondary_button_color: str = "#ffffff"
    secondary_button_color_hover: str = "#ffffff"
    secondary_button_text_color: str = "#0061FE"
    secondary_button_text_color_hover: str = "#0061FE"
    text_color1: str = "#808080"
    text_color2: str = "#ffffff"
    reset_to_default: Optional[bool] = UNSET
    """Resets white labeling options to defaults. Only useful when updating an API App."""


class SubWhiteLabelingOptionsDict(TypedDict):
    header_background_color: NotRequired[str]
    legal_version: NotRequired[LegalVersionOrStr]
    link_color: NotRequired[str]
    page_background_color: NotRequired[str]
    primary_button_color: NotRequired[str]
    primary_button_color_hover: NotRequired[str]
    primary_button_text_color: NotRequired[str]
    primary_button_text_color_hover: NotRequired[str]
    secondary_button_color: NotRequired[str]
    secondary_button_color_hover: NotRequired[str]
    secondary_button_text_color: NotRequired[str]
    secondary_button_text_color_hover: NotRequired[str]
    text_color1: NotRequired[str]
    text_color2: NotRequired[str]
    reset_to_default: NotRequired[bool]
