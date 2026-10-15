from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, FileResponse, Optional, SdkBaseModel


class TemplateUpdateFilesRequest(SdkBaseModel):
    client_id: Optional[str] = UNSET
    """Client id of the app you're using to update this template."""

    files: Optional[FileResponse] = UNSET
    """Use ``files[]`` to indicate the uploaded file(s) to use for the template.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    file_urls: Optional[list[str]] = UNSET
    """Use ``file_urls[]`` to have Dropbox Sign download the file(s) to use for the template.

    This endpoint requires either **files** or **file_urls[]**, but not both."""

    message: Optional[str] = UNSET
    """The new default template email message."""

    subject: Optional[str] = UNSET
    """The new default template email subject."""

    test_mode: bool = False
    """Whether this is a test, the signature request created from this draft will not be legally binding if set to
    ``true``. Defaults to ``false``."""


class TemplateUpdateFilesRequestDict(TypedDict):
    client_id: NotRequired[str]
    files: NotRequired[FileResponse]
    file_urls: NotRequired[list[str]]
    message: NotRequired[str]
    subject: NotRequired[str]
    test_mode: NotRequired[bool]
