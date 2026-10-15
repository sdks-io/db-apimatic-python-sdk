from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubBulkSignerListCustomField(SdkBaseModel):
    name: str
    """The name of the custom field. Must be the field's ``name`` or ``api_id``."""

    value: str
    """The value of the custom field."""


class SubBulkSignerListCustomFieldDict(TypedDict):
    name: str
    value: str
