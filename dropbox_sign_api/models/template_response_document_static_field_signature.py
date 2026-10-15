from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class TemplateResponseDocumentStaticFieldSignature(SdkBaseModel):
    """All Of TemplateResponseDocumentStaticFieldBase, TemplateResponseDocumentStaticFieldSignature."""

    api_id: Optional[str] = UNSET
    """A unique id for the static field."""

    name: Optional[str] = UNSET
    """The name of the static field."""

    type_: str = Field(default="signature", alias="type")
    """The type of this static field. See `field types </api/reference/constants/#field-types>`__.

    * Text Field uses ``TemplateResponseDocumentStaticFieldText``
    * Dropdown Field uses ``TemplateResponseDocumentStaticFieldDropdown``
    * Hyperlink Field uses ``TemplateResponseDocumentStaticFieldHyperlink``
    * Checkbox Field uses ``TemplateResponseDocumentStaticFieldCheckbox``
    * Radio Field uses ``TemplateResponseDocumentStaticFieldRadio``
    * Signature Field uses ``TemplateResponseDocumentStaticFieldSignature``
    * Date Signed Field uses ``TemplateResponseDocumentStaticFieldDateSigned``
    * Initials Field uses ``TemplateResponseDocumentStaticFieldInitials``"""

    signer: str = "me_now"
    """The signer of the Static Field."""

    x: Optional[int] = UNSET
    """The horizontal offset in pixels for this static field."""

    y: Optional[int] = UNSET
    """The vertical offset in pixels for this static field."""

    width: Optional[int] = UNSET
    """The width in pixels of this static field."""

    height: Optional[int] = UNSET
    """The height in pixels of this static field."""

    required: Optional[bool] = UNSET
    """Boolean showing whether or not this field is required."""

    group: OptionalNullable[str] = UNSET
    """The name of the group this field is in. If this field is not a group, this defaults to ``null``."""


class TemplateResponseDocumentStaticFieldSignatureDict(TypedDict):
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
