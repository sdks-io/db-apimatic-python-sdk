from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type1 import Type1OrStr


class SubFormFieldRuleAction(SdkBaseModel):
    field_id: Optional[str] = UNSET
    """**field_id** or **group_id** is required, but not both.

    Must reference the ``api_id`` of an existing field defined within ``form_fields_per_document``.

    Cannot use with ``group_id``. Trigger and action fields must belong to the same signer."""

    group_id: Optional[str] = UNSET
    """**group_id** or **field_id** is required, but not both.

    Must reference the ID of an existing group defined within ``form_field_groups``.

    Cannot use with ``field_id``. Trigger and action fields and groups must belong to the same signer."""

    hidden: bool
    """``true`` to hide the target field when rule is satisfied, otherwise ``false``."""

    type_: Type1OrStr = Field(alias="type")


class SubFormFieldRuleActionDict(TypedDict):
    field_id: NotRequired[str]
    group_id: NotRequired[str]
    hidden: bool
    type_: Type1OrStr
