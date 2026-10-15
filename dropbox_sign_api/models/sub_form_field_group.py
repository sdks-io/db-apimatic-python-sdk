from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SubFormFieldGroup(SdkBaseModel):
    group_id: str
    """ID of group. Use this to reference a specific group from the ``group`` value in ``form_fields_per_document``."""

    group_label: str
    """Name of the group"""

    requirement: str
    """Examples: ``require_0-1`` ``require_1`` ``require_1-ormore``

    - Check out the list of /api/reference/constants/#checkbox-field-grouping.
    - Check out the list of /api/reference/constants/#radio-field-grouping.
    - Radio groups require **at least** two fields per group."""


class SubFormFieldGroupDict(TypedDict):
    group_id: str
    group_label: str
    requirement: str
