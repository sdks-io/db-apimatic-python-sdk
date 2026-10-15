from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .template_create_embedded_draft_response_template import (
    TemplateCreateEmbeddedDraftResponseTemplate,
    TemplateCreateEmbeddedDraftResponseTemplateDict,
)
from .warning_response import WarningResponse, WarningResponseDict


class TemplateCreateEmbeddedDraftResponse(SdkBaseModel):
    template: TemplateCreateEmbeddedDraftResponseTemplate
    """Template object with parameters: ``template_id``, ``edit_url``, ``expires_at``."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TemplateCreateEmbeddedDraftResponseDict(TypedDict):
    template: TemplateCreateEmbeddedDraftResponseTemplateDict
    warnings: NotRequired[list[WarningResponseDict]]
