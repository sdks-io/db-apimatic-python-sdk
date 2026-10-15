from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TemplateCreateResponseTemplate(SdkBaseModel):
    """Template object with parameters: ``template_id``."""

    template_id: Optional[str] = UNSET
    """The id of the Template."""


class TemplateCreateResponseTemplateDict(TypedDict):
    template_id: NotRequired[str]
