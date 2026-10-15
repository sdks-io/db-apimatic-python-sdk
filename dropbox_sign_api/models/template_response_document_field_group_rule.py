from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateResponseDocumentFieldGroupRule(SdkBaseModel):
    """The rule used to validate checkboxes in the form field group. See `checkbox field grouping
    </api/reference/constants/#checkbox-field-grouping>`__."""

    requirement: Optional[str] = UNSET
    """Examples: ``require_0-1`` ``require_1`` ``require_1-ormore``

    - Check out the list of /api/reference/constants/#checkbox-field-grouping.
    - Check out the list of /api/reference/constants/#radio-field-grouping.
    - Radio groups require **at least** two fields per group."""

    group_label: Optional[str] = Field(default=UNSET, alias="groupLabel")
    """Name of the group"""


class TemplateResponseDocumentFieldGroupRuleDict(TypedDict):
    requirement: NotRequired[str]
    group_label: NotRequired[str]
