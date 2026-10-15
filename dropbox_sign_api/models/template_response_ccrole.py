from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateResponseCcrole(SdkBaseModel):
    name: Optional[str] = UNSET
    """The name of the Role."""


class TemplateResponseCcroleDict(TypedDict):
    name: NotRequired[str]
