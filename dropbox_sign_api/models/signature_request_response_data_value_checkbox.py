from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SignatureRequestResponseDataValueCheckbox(SdkBaseModel):
    """All Of SignatureRequestResponseDataBase, SignatureRequestResponseDataValueCheckbox."""

    api_id: Optional[str] = UNSET
    """The unique ID for this field."""

    signature_id: Optional[str] = UNSET
    """The ID of the signature to which this response is linked."""

    name: Optional[str] = UNSET
    """The name of the form field."""

    required: Optional[bool] = UNSET
    """A boolean value denoting if this field is required."""

    type_: str = Field(default="checkbox", alias="type")
    """A yes/no checkbox"""

    value: Optional[bool] = UNSET
    """The value of the form field."""


class SignatureRequestResponseDataValueCheckboxDict(TypedDict):
    api_id: NotRequired[str]
    signature_id: NotRequired[str]
    name: NotRequired[str]
    required: NotRequired[bool]
    type_: NotRequired[str]
    value: NotRequired[bool]
