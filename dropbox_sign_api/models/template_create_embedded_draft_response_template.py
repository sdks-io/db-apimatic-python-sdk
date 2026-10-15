from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .warning_response import WarningResponse, WarningResponseDict


class TemplateCreateEmbeddedDraftResponseTemplate(SdkBaseModel):
    """Template object with parameters: ``template_id``, ``edit_url``, ``expires_at``."""

    template_id: Optional[str] = UNSET
    """The id of the Template."""

    edit_url: Optional[str] = UNSET
    """Link to edit the template."""

    expires_at: Optional[int] = UNSET
    """When the link expires."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TemplateCreateEmbeddedDraftResponseTemplateDict(TypedDict):
    template_id: NotRequired[str]
    edit_url: NotRequired[str]
    expires_at: NotRequired[int]
    warnings: NotRequired[list[WarningResponseDict]]
