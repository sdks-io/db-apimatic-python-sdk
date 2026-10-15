from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.operator import OperatorOrStr


class SubFormFieldRuleTrigger(SdkBaseModel):
    id: str
    """Must reference the ``api_id`` of an existing field defined within ``form_fields_per_document``. Trigger and
    action fields and groups must belong to the same signer."""

    operator: OperatorOrStr
    """Different field types allow different ``operator`` values:
    - Field type of **text**:
      - **is**: exact match
      - **not**: not exact match
      - **match**: regular expression, without /. Example:
        - OK ``[a-zA-Z0-9]``
        - Not OK ``/[a-zA-Z0-9]/``
    - Field type of **dropdown**:
      - **is**: exact match, single value
      - **not**: not exact match, single value
      - **any**: exact match, array of values.
      - **none**: not exact match, array of values.
    - Field type of **checkbox**:
      - **is**: exact match, single value
      - **not**: not exact match, single value
    - Field type of **radio**:
      - **is**: exact match, single value
      - **not**: not exact match, single value"""

    value: Optional[str] = UNSET
    """**value** or **values** is required, but not both.

    The value to match against **operator**.

    - When **operator** is one of the following, **value** must be ``String``:
      - ``is``
      - ``not``
      - ``match``

    Otherwise,
    - **checkbox**: When **type** of trigger is **checkbox**, **value** must be ``0`` or ``1``
    - **radio**: When **type** of trigger is **radio**, **value** must be ``1``"""

    values: Optional[list[str]] = UNSET
    """**values** or **value** is required, but not both.

    The values to match against **operator** when it is one of the following:

    - ``any``
    - ``none``"""


class SubFormFieldRuleTriggerDict(TypedDict):
    id: str
    operator: OperatorOrStr
    value: NotRequired[str]
    values: NotRequired[list[str]]
