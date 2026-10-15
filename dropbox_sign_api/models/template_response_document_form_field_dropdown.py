from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TemplateResponseDocumentFormFieldDropdown(SdkBaseModel):
    """All Of TemplateResponseDocumentFormFieldBase, TemplateResponseDocumentFormFieldDropdown."""

    api_id: Optional[str] = UNSET
    """A unique id for the form field."""

    name: Optional[str] = UNSET
    """The name of the form field."""

    type_: str = Field(default="dropdown", alias="type")
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

    group: OptionalNullable[str] = UNSET
    """The name of the group this field is in. If this field is not a group, this defaults to ``null`` except for Radio
    fields."""

    options: Optional[list[str]] = UNSET
    """The options available for this dropdown form field."""


class TemplateResponseDocumentFormFieldDropdownDict(TypedDict):
    api_id: NotRequired[str]
    name: NotRequired[str]
    type_: str
    signer: NotRequired[str]
    x: NotRequired[int]
    y: NotRequired[int]
    width: NotRequired[int]
    height: NotRequired[int]
    required: NotRequired[bool]
    group: NotRequired[str | None]
    options: NotRequired[list[str]]
