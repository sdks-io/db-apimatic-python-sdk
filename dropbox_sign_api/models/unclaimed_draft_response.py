from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class UnclaimedDraftResponse(SdkBaseModel):
    """A group of documents that a user can take ownership of via the claim URL."""

    signature_request_id: OptionalNullable[str] = UNSET
    """The ID of the signature request that is represented by this UnclaimedDraft."""

    claim_url: Optional[str] = UNSET
    """The URL to be used to claim this UnclaimedDraft."""

    signing_redirect_url: OptionalNullable[str] = UNSET
    """The URL you want signers redirected to after they successfully sign."""

    requesting_redirect_url: OptionalNullable[str] = UNSET
    """The URL you want signers redirected to after they successfully request a signature (Will only be returned in the
    response if it is applicable to the request.)."""

    expires_at: OptionalNullable[int] = UNSET
    """When the link expires."""

    test_mode: Optional[bool] = UNSET
    """Whether this is a test draft. Signature requests made from test drafts have no legal value."""


class UnclaimedDraftResponseDict(TypedDict):
    signature_request_id: NotRequired[str | None]
    claim_url: NotRequired[str]
    signing_redirect_url: NotRequired[str | None]
    requesting_redirect_url: NotRequired[str | None]
    expires_at: NotRequired[int | None]
    test_mode: NotRequired[bool]
