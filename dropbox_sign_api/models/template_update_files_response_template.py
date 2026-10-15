from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .warning_response import WarningResponse, WarningResponseDict


class TemplateUpdateFilesResponseTemplate(SdkBaseModel):
    """Contains template id"""

    template_id: Optional[str] = UNSET
    """The id of the Template."""

    warnings: Optional[list[WarningResponse]] = UNSET
    """A list of warnings."""


class TemplateUpdateFilesResponseTemplateDict(TypedDict):
    template_id: NotRequired[str]
    warnings: NotRequired[list[WarningResponseDict]]
