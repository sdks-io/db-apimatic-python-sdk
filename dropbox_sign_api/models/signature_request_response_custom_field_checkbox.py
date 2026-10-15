from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SignatureRequestResponseCustomFieldCheckbox(SdkBaseModel):
    """All Of SignatureRequestResponseCustomFieldBase, SignatureRequestResponseCustomFieldCheckbox."""

    type_: str = Field(default="checkbox", alias="type")
    """The type of this Custom Field. Only 'text' and 'checkbox' are currently supported."""

    name: str
    """The name of the Custom Field."""

    required: Optional[bool] = UNSET
    """A boolean value denoting if this field is required."""

    api_id: Optional[str] = UNSET
    """The unique ID for this field."""

    editor: OptionalNullable[str] = UNSET
    """The name of the Role that is able to edit this field."""

    value: Optional[bool] = UNSET
    """A true/false for checkbox fields"""


class SignatureRequestResponseCustomFieldCheckboxDict(TypedDict):
    type_: str
    name: str
    required: NotRequired[bool]
    api_id: NotRequired[str]
    editor: NotRequired[str | None]
    value: NotRequired[bool]
