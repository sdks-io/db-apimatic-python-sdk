from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .template_create_response_template import TemplateCreateResponseTemplate, TemplateCreateResponseTemplateDict
from .warning_response import WarningResponse, WarningResponseDict


class TemplateCreateResponse(SdkBaseModel):
    template: TemplateCreateResponseTemplate
    """Template object with parameters: ``template_id``."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TemplateCreateResponseDict(TypedDict):
    template: TemplateCreateResponseTemplateDict
    warnings: NotRequired[list[WarningResponseDict]]
