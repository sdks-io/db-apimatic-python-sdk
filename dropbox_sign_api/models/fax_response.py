from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .fax_response_transmission import FaxResponseTransmission, FaxResponseTransmissionDict


class FaxResponse(SdkBaseModel):
    fax_id: str
    """Fax ID"""

    title: str
    """Fax Title"""

    original_title: str
    """Fax Original Title"""

    subject: OptionalNullable[str] = UNSET
    """Fax Subject"""

    message: OptionalNullable[str] = UNSET
    """Fax Message"""

    metadata: dict[str, Any]
    """Fax Metadata"""

    created_at: int
    """Fax Created At Timestamp"""

    sender: str
    """Fax Sender Email"""

    files_url: str
    """Fax Files URL"""

    final_copy_uri: OptionalNullable[str] = UNSET
    """The path where the completed document can be downloaded"""

    transmissions: list[FaxResponseTransmission]
    """Fax Transmissions List"""

    test_mode: bool = False
    """Whether this is a test fax. Test faxes are not delivered to the recipient. Defaults to ``false``."""


class FaxResponseDict(TypedDict):
    fax_id: str
    title: str
    original_title: str
    subject: NotRequired[str | None]
    message: NotRequired[str | None]
    metadata: dict[str, Any]
    created_at: int
    sender: str
    files_url: str
    final_copy_uri: NotRequired[str | None]
    transmissions: list[FaxResponseTransmissionDict]
    test_mode: bool
