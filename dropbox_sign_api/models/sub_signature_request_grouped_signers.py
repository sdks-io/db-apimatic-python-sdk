from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .sub_signature_request_signer import SubSignatureRequestSigner, SubSignatureRequestSignerDict


class SubSignatureRequestGroupedSigners(SdkBaseModel):
    group: str
    """The name of the group."""

    order: OptionalNullable[int] = UNSET
    """The order the group is required to sign in. Use this instead of Signer-level ``order``."""

    signers: list[SubSignatureRequestSigner]
    """Signers belonging to this Group.

    **NOTE:** Only ``name``, ``email_address``, and ``pin`` are available to Grouped Signers. We will ignore all other
    properties, even though they are listed below."""


class SubSignatureRequestGroupedSignersDict(TypedDict):
    group: str
    order: NotRequired[int | None]
    signers: list[SubSignatureRequestSignerDict]
