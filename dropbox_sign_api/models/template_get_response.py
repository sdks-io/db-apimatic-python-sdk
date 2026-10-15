from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .template_response import TemplateResponse, TemplateResponseDict
from .warning_response import WarningResponse, WarningResponseDict


class TemplateGetResponse(SdkBaseModel):
    template: TemplateResponse
    """Contains information about the templates you and your team have created."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TemplateGetResponseDict(TypedDict):
    template: TemplateResponseDict
    warnings: NotRequired[list[WarningResponseDict]]
