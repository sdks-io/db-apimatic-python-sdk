from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .event import Event, EventDict


class CallbackTestEvent(SdkBaseModel):
    event: Event


class CallbackTestEventDict(TypedDict):
    event: EventDict
