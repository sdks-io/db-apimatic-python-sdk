from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.font_family import FontFamilyOrStr
from .enums.validation_type import ValidationTypeOrStr


class SubFormFieldsPerDocumentText(SdkBaseModel):
    """All Of SubFormFieldsPerDocumentBase, SubFormFieldsPerDocumentText."""

    document_index: int
    """Represents the integer index of the ``file`` or ``file_url`` document the field should be attached to."""

    api_id: str
    """An identifier for the field that is unique across all documents in the request."""

    height: int
    """Size of the field in pixels."""

    name: Optional[str] = UNSET
    """Display name for the field."""

    page: OptionalNullable[int] = UNSET
    """Page in the document where the field should be placed (requires documents be PDF files).

    - When the page number parameter is supplied, the API will use the new coordinate system.
    - Check out the differences between both `coordinate systems
        <https://faq.hellosign.com/hc/en-us/articles/217115577>`__ and how to use them."""

    required: bool
    """Whether this field is required."""

    signer: str
    """Signer index identified by the offset in the signers parameter (0-based indexing), indicating which signer should
    fill out the field.

    **NOTE:** To set the value of the field as the preparer you must set this to ``me_now``

    **NOTE:** If type is ``text-merge`` or ``checkbox-merge``, you must set this to sender in order to use pre-filled
    data."""

    type_: str = Field(default="text", alias="type")
    """A text input field. Use the ``SubFormFieldsPerDocumentText`` class."""

    width: int
    """Size of the field in pixels."""

    x: int
    """Location coordinates of the field in pixels."""

    y: int
    """Location coordinates of the field in pixels."""

    placeholder: Optional[str] = UNSET
    """Placeholder value for text field."""

    auto_fill_type: Optional[str] = UNSET
    """Auto fill type for populating fields automatically. Check out the list of `auto fill types
    </api/reference/constants/#auto-fill-types>`__ to learn more about the possible values."""

    link_id: Optional[str] = UNSET
    """Link two or more text fields. Enter data into one linked text field, which automatically fill all other linked
    text fields."""

    masked: Optional[bool] = UNSET
    """Masks entered data. For more information see `Masking sensitive information
    <https://faq.hellosign.com/hc/en-us/articles/360040742811-Masking-sensitive-information>`__. ``true`` for masking
    the data in a text field, otherwise ``false``."""

    validation_type: Optional[ValidationTypeOrStr] = UNSET
    """Each text field may contain a ``validation_type`` parameter. Check out the list of `validation types
    <https://faq.hellosign.com/hc/en-us/articles/217115577>`__ to learn more about the possible values.

    **NOTE:** When using ``custom_regex`` you are required to pass a second parameter ``validation_custom_regex`` and
    you can optionally provide ``validation_custom_regex_format_label`` for the error message the user will see in case
    of an invalid value."""

    validation_custom_regex: Optional[str] = UNSET
    validation_custom_regex_format_label: Optional[str] = UNSET
    content: Optional[str] = UNSET
    """Content of a ``me_now`` text field"""

    font_family: Optional[FontFamilyOrStr] = UNSET
    """Font family for the field."""

    font_size: int = 12
    """The initial px font size for the field contents. Can be any integer value between ``7`` and ``49``.

    **NOTE:** Font size may be reduced during processing in order to fit the contents within the dimensions of the
    field."""


class SubFormFieldsPerDocumentTextDict(TypedDict):
    document_index: int
    api_id: str
    height: int
    name: NotRequired[str]
    page: NotRequired[int | None]
    required: bool
    signer: str
    type_: str
    width: int
    x: int
    y: int
    placeholder: NotRequired[str]
    auto_fill_type: NotRequired[str]
    link_id: NotRequired[str]
    masked: NotRequired[bool]
    validation_type: NotRequired[ValidationTypeOrStr]
    validation_custom_regex: NotRequired[str]
    validation_custom_regex_format_label: NotRequired[str]
    content: NotRequired[str]
    font_family: NotRequired[FontFamilyOrStr]
    font_size: NotRequired[int]
