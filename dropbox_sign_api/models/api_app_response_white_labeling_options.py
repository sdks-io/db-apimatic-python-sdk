from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ApiAppResponseWhiteLabelingOptions(SdkBaseModel):
    """An object with options to customize the app's signer page"""

    header_background_color: Optional[str] = UNSET
    legal_version: Optional[str] = UNSET
    link_color: Optional[str] = UNSET
    page_background_color: Optional[str] = UNSET
    primary_button_color: Optional[str] = UNSET
    primary_button_color_hover: Optional[str] = UNSET
    primary_button_text_color: Optional[str] = UNSET
    primary_button_text_color_hover: Optional[str] = UNSET
    secondary_button_color: Optional[str] = UNSET
    secondary_button_color_hover: Optional[str] = UNSET
    secondary_button_text_color: Optional[str] = UNSET
    secondary_button_text_color_hover: Optional[str] = UNSET
    text_color1: Optional[str] = UNSET
    text_color2: Optional[str] = UNSET


class ApiAppResponseWhiteLabelingOptionsDict(TypedDict):
    header_background_color: NotRequired[str]
    legal_version: NotRequired[str]
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
