from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.font_family import FontFamilyOrStr


class SubFormFieldsPerDocumentHyperlink(SdkBaseModel):
    """All Of SubFormFieldsPerDocumentBase, SubFormFieldsPerDocumentHyperlink."""

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

    type_: str = Field(default="hyperlink", alias="type")
    """A hyperlink field. Use the ``SubFormFieldsPerDocumentHyperlink`` class."""

    width: int
    """Size of the field in pixels."""

    x: int
    """Location coordinates of the field in pixels."""

    y: int
    """Location coordinates of the field in pixels."""

    content: str
    """Link Text."""

    content_url: str
    """Link URL."""

    font_family: Optional[FontFamilyOrStr] = UNSET
    """Font family for the field."""

    font_size: int = 12
    """The initial px font size for the field contents. Can be any integer value between ``7`` and ``49``.

    **NOTE:** Font size may be reduced during processing in order to fit the contents within the dimensions of the
    field."""


class SubFormFieldsPerDocumentHyperlinkDict(TypedDict):
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
    content: str
    content_url: str
    font_family: NotRequired[FontFamilyOrStr]
    font_size: NotRequired[int]
