from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .event import Event, EventDict
from .template_response import TemplateResponse, TemplateResponseDict


class TemplateErrorEvent(SdkBaseModel):
    event: Event
    template: Optional[TemplateResponse] = UNSET
    """Contains information about the templates you and your team have created."""


class TemplateErrorEventDict(TypedDict):
    event: EventDict
    template: NotRequired[TemplateResponseDict]
