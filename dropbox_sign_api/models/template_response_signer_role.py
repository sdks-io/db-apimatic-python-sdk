from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateResponseSignerRole(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the Role."""

    order: Optional[int] = UNSET
    """If signer order is assigned this is the 0-based index for this role."""


class TemplateResponseSignerRoleDict(TypedDict):
    name: NotRequired[str]
    order: NotRequired[int]
