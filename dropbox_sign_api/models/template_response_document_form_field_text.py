from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.validation_type1 import ValidationType1OrStr
from .template_response_field_avg_text_length import (
    TemplateResponseFieldAvgTextLength,
    TemplateResponseFieldAvgTextLengthDict,
)


class TemplateResponseDocumentFormFieldText(SdkBaseModel):
    """All Of TemplateResponseDocumentFormFieldBase, TemplateResponseDocumentFormFieldText."""

    api_id: Optional[str] = UNSET
    """A unique id for the form field."""

    name: Optional[str] = UNSET
    """The name of the form field."""

    type_: str = Field(default="text", alias="type")
    """The type of this form field. See `field types </api/reference/constants/#field-types>`__.

    * Text Field uses ``TemplateResponseDocumentFormFieldText``
    * Dropdown Field uses ``TemplateResponseDocumentFormFieldDropdown``
    * Hyperlink Field uses ``TemplateResponseDocumentFormFieldHyperlink``
    * Checkbox Field uses ``TemplateResponseDocumentFormFieldCheckbox``
    * Radio Field uses ``TemplateResponseDocumentFormFieldRadio``
    * Signature Field uses ``TemplateResponseDocumentFormFieldSignature``
    * Date Signed Field uses ``TemplateResponseDocumentFormFieldDateSigned``
    * Initials Field uses ``TemplateResponseDocumentFormFieldInitials``"""

    signer: Optional[str] = UNSET
    """The signer of the Form Field."""

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

    avg_text_length: Optional[TemplateResponseFieldAvgTextLength] = UNSET
    """Average text length in this field."""

    is_multiline: Optional[bool] = Field(default=UNSET, alias="isMultiline")
    """Whether this form field is multiline text."""

    original_font_size: Optional[int] = Field(default=UNSET, alias="originalFontSize")
    """Original font size used in this form field's text."""

    font_family: Optional[str] = Field(default=UNSET, alias="fontFamily")
    """Font family used in this form field's text."""

    validation_type: OptionalNullable[ValidationType1OrStr] = UNSET
    """Each text field may contain a ``validation_type`` parameter. Check out the list of `validation types
    <https://faq.hellosign.com/hc/en-us/articles/217115577>`__ to learn more about the possible values."""

    validation_custom_regex: OptionalNullable[str] = UNSET
    """When ``validation_type`` is set to ``custom_regex``, this specifies the custom regular expression pattern that
    will be used to validate the text field."""

    validation_custom_regex_format_label: OptionalNullable[str] = UNSET
    """When ``validation_type`` is set to ``custom_regex``, this specifies the error message displayed to the signer
    when the text does not match the provided regex pattern."""

    group: OptionalNullable[str] = UNSET
    """The name of the group this field is in. If this field is not a group, this defaults to ``null`` except for Radio
    fields."""


class TemplateResponseDocumentFormFieldTextDict(TypedDict):
    api_id: NotRequired[str]
    name: NotRequired[str]
    type_: str
    signer: NotRequired[str]
    x: NotRequired[int]
    y: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    required: NotRequired[bool]
    avg_text_length: NotRequired[TemplateResponseFieldAvgTextLengthDict]
    is_multiline: NotRequired[bool]
    original_font_size: NotRequired[int]
    font_family: NotRequired[str]
    validation_type: NotRequired[ValidationType1OrStr | None]
    validation_custom_regex: NotRequired[str | None]
    validation_custom_regex_format_label: NotRequired[str | None]
    group: NotRequired[str | None]
