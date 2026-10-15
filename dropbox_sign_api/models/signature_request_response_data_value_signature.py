from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SignatureRequestResponseDataValueSignature(SdkBaseModel):
    """All Of SignatureRequestResponseDataBase, SignatureRequestResponseDataValueSignature."""

    api_id: Optional[str] = UNSET
    """The unique ID for this field."""

    signature_id: Optional[str] = UNSET
    """The ID of the signature to which this response is linked."""

    name: Optional[str] = UNSET
    """The name of the form field."""

    required: Optional[bool] = UNSET
    """A boolean value denoting if this field is required."""

    type_: str = Field(default="signature", alias="type")
    """A signature input field"""

    value: Optional[str] = UNSET
    """The value of the form field."""

    is_signed: OptionalNullable[bool] = UNSET
    """This field contains the boolean true if the field is signed."""


class SignatureRequestResponseDataValueSignatureDict(TypedDict):
    api_id: NotRequired[str]
    signature_id: NotRequired[str]
    name: NotRequired[str]
    required: NotRequired[bool]
    type_: NotRequired[str]
    value: NotRequired[str]
    is_signed: NotRequired[bool | None]
