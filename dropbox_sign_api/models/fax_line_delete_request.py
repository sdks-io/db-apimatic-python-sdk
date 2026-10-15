from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FaxLineDeleteRequest(SdkBaseModel):
    number: str
    """The Fax Line number"""


class FaxLineDeleteRequestDict(TypedDict):
    number: str
