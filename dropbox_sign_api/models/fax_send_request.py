from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel


class FaxSendRequest(SdkBaseModel):
    recipient: str
    """Recipient of the fax Can be a phone number in E.164 format or email address"""

    sender: Optional[str] = UNSET
    """Fax Send From Sender (used only with fax number)"""

    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to fax

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Fax download the file(s) to fax

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    test_mode: bool = False
    """API Test Mode Setting"""

    cover_page_to: Optional[str] = UNSET
    """Fax cover page recipient information"""

    cover_page_from: Optional[str] = UNSET
    """Fax cover page sender information"""

    cover_page_message: Optional[str] = UNSET
    """Fax Cover Page Message"""

    title: Optional[str] = UNSET
    """Fax Title"""


class FaxSendRequestDict(TypedDict):
    recipient: str
    sender: NotRequired[str]
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    test_mode: NotRequired[bool]
    cover_page_to: NotRequired[str]
    cover_page_from: NotRequired[str]
    cover_page_message: NotRequired[str]
    title: NotRequired[str]
