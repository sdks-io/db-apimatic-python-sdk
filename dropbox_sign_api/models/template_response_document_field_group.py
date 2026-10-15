from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .template_response_document_field_group_rule import (
    TemplateResponseDocumentFieldGroupRule,
    TemplateResponseDocumentFieldGroupRuleDict,
)


class TemplateResponseDocumentFieldGroup(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the form field group."""

    rule: Optional[TemplateResponseDocumentFieldGroupRule] = UNSET
    """The rule used to validate checkboxes in the form field group. See `checkbox field grouping
    </api/reference/constants/#checkbox-field-grouping>`__."""


class TemplateResponseDocumentFieldGroupDict(TypedDict):
    name: NotRequired[str]
    rule: NotRequired[TemplateResponseDocumentFieldGroupRuleDict]
