from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .template_update_files_response_template import (
    TemplateUpdateFilesResponseTemplate,
    TemplateUpdateFilesResponseTemplateDict,
)


class TemplateUpdateFilesResponse(SdkBaseModel):
    template: TemplateUpdateFilesResponseTemplate
    """Contains template id"""


class TemplateUpdateFilesResponseDict(TypedDict):
    template: TemplateUpdateFilesResponseTemplateDict
