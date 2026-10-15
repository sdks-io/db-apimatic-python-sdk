from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .template_response_field_avg_text_length import (
    TemplateResponseFieldAvgTextLength,
    TemplateResponseFieldAvgTextLengthDict,
)


class TemplateResponseDocumentCustomFieldText(SdkBaseModel):
    """All Of TemplateResponseDocumentCustomFieldBase, TemplateResponseDocumentCustomFieldText."""

    api_id: Optional[str] = UNSET
    """The unique ID for this field."""

    name: Optional[str] = UNSET
    """The name of the Custom Field."""

    type_: str = Field(default="text", alias="type")
    """The type of this Custom Field. Only ``text`` and ``checkbox`` are currently supported.

    * Text uses ``TemplateResponseDocumentCustomFieldText``
    * Checkbox uses ``TemplateResponseDocumentCustomFieldCheckbox``"""

    signer: OptionalNullable[str] = UNSET
    """The signer of the Custom Field. Can be ``null`` if field is a merge field (assigned to Sender)."""

    x: Optional[int] = UNSET
    """The horizontal offset in pixels for this form field."""

    y: Optional[int] = UNSET
    """The vertical offset in pixels for this form field."""

    width: Optional[int] = UNSET
    """The width in pixels of this form field."""

    height: Optional[int] = UNSET
    """The height in pixels of this form field."""

    required: Optional[bool] = UNSET
    """Boolean showing whether or not this field is required."""

    group: OptionalNullable[str] = UNSET
    """The name of the group this field is in. If this field is not a group, this defaults to ``null``."""

    avg_text_length: Optional[TemplateResponseFieldAvgTextLength] = UNSET
    """Average text length in this field."""

    is_multiline: Optional[bool] = Field(default=UNSET, alias="isMultiline")
    """Whether this form field is multiline text."""

    original_font_size: Optional[int] = Field(default=UNSET, alias="originalFontSize")
    """Original font size used in this form field's text."""

    font_family: Optional[str] = Field(default=UNSET, alias="fontFamily")
    """Font family used in this form field's text."""


class TemplateResponseDocumentCustomFieldTextDict(TypedDict):
    api_id: NotRequired[str]
    name: NotRequired[str]
    type_: str
    signer: NotRequired[str | None]
    x: NotRequired[int]
    y: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    required: NotRequired[bool]
    group: NotRequired[str | None]
    avg_text_length: NotRequired[TemplateResponseFieldAvgTextLengthDict]
    is_multiline: NotRequired[bool]
    original_font_size: NotRequired[int]
    font_family: NotRequired[str]
