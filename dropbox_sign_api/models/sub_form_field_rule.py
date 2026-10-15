from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .sub_form_field_rule_action import SubFormFieldRuleAction, SubFormFieldRuleActionDict
from .sub_form_field_rule_trigger import SubFormFieldRuleTrigger, SubFormFieldRuleTriggerDict


class SubFormFieldRule(SdkBaseModel):
    id: str
    """Must be unique across all defined rules."""

    trigger_operator: str = "AND"
    """Currently only ``AND`` is supported. Support for ``OR`` is being worked on."""

    triggers: list[SubFormFieldRuleTrigger]
    """An array of trigger definitions, the "if this" part of "**if this**, then that". Currently only a single trigger
    per rule is allowed."""

    actions: list[SubFormFieldRuleAction]
    """An array of action definitions, the "then that" part of "if this, **then that**". Any number of actions may be
    attached to a single rule."""


class SubFormFieldRuleDict(TypedDict):
    id: str
    trigger_operator: str
    triggers: list[SubFormFieldRuleTriggerDict]
    actions: list[SubFormFieldRuleActionDict]
