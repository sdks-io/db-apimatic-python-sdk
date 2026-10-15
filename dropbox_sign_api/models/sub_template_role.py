from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class SubTemplateRole(SdkBaseModel):
    name: Optional[str] = UNSET
    """The role name of the signer that will be displayed when the template is used to create a signature request."""

    order: OptionalNullable[int] = UNSET
    """The order in which this signer role is required to sign."""


class SubTemplateRoleDict(TypedDict):
    name: NotRequired[str]
    order: NotRequired[int | None]
