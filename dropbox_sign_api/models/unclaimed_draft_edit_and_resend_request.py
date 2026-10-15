from __future__ import annotations

from pydantic import EmailStr
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sub_editor_options import SubEditorOptions, SubEditorOptionsDict


class UnclaimedDraftEditAndResendRequest(SdkBaseModel):
    client_id: str
    """Client id of the app used to create the draft. Used to apply the branding and callback url defined for the
    app."""

    editor_options: Optional[SubEditorOptions] = UNSET
    """This allows the requester to specify editor options when a preparing a document"""

    is_for_embedded_signing: Optional[bool] = UNSET
    """The request created from this draft will also be signable in embedded mode if set to ``true``."""

    requester_email_address: Optional[EmailStr] = UNSET
    """The email address of the user that should be designated as the requester of this draft. If not set, original
    requester's email address will be used."""

    requesting_redirect_url: Optional[str] = UNSET
    """The URL you want signers redirected to after they successfully request a signature."""

    show_progress_stepper: bool = True
    """When only one step remains in the signature request process and this parameter is set to ``false`` then the
    progress stepper will be hidden."""

    signing_redirect_url: Optional[str] = UNSET
    """The URL you want signers redirected to after they successfully sign."""

    test_mode: bool = False
    """Whether this is a test, the signature request created from this draft will not be legally binding if set to
    ``true``. Defaults to ``false``."""


class UnclaimedDraftEditAndResendRequestDict(TypedDict):
    client_id: str
    editor_options: NotRequired[SubEditorOptionsDict]
    is_for_embedded_signing: NotRequired[bool]
    requester_email_address: NotRequired[EmailStr]
    requesting_redirect_url: NotRequired[str]
    show_progress_stepper: NotRequired[bool]
    signing_redirect_url: NotRequired[str]
    test_mode: NotRequired[bool]
