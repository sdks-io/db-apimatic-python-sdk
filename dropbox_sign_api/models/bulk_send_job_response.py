from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class BulkSendJobResponse(SdkBaseModel):
    """Contains information about the BulkSendJob such as when it was created and how many signature requests are
    queued."""

    bulk_send_job_id: OptionalNullable[str] = UNSET
    """The id of the BulkSendJob."""

    total: Optional[int] = UNSET
    """The total amount of Signature Requests queued for sending."""

    is_creator: Optional[bool] = UNSET
    """True if you are the owner of this BulkSendJob, false if it's been shared with you by a team member."""

    created_at: Optional[int] = UNSET
    """Time that the BulkSendJob was created."""


class BulkSendJobResponseDict(TypedDict):
    bulk_send_job_id: NotRequired[str | None]
    total: NotRequired[int]
    is_creator: NotRequired[bool]
    created_at: NotRequired[int]
