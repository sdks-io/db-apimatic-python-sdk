from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .sub_editor_options import SubEditorOptions, SubEditorOptionsDict
from .sub_merge_field import SubMergeField, SubMergeFieldDict


class EmbeddedEditUrlRequest(SdkBaseModel):
    allow_edit_ccs: bool = False
    """This allows the requester to enable/disable to add or change CC roles when editing the template."""

    cc_roles: Optional[list[str]] = UNSET
    """The CC roles that must be assigned when using the template to send a signature request. To remove all CC roles,
    pass in a single role with no name. For use in a POST request."""

    editor_options: Optional[SubEditorOptions] = UNSET
    """This allows the requester to specify editor options when a preparing a document"""

    force_signer_roles: bool = False
    """Provide users the ability to review/edit the template signer roles."""

    force_subject_message: bool = False
    """Provide users the ability to review/edit the template subject and message."""

    merge_fields: Optional[list[SubMergeField]] = UNSET
    """Add additional merge fields to the template, which can be used used to pre-fill data by passing values into
    signature requests made with that template.

    Remove all merge fields on the template by passing an empty array ``[]``."""

    preview_only: bool = False
    """This allows the requester to enable the preview experience (i.e. does not allow the requester's end user to add
    any additional fields via the editor).

    **NOTE:** This parameter overwrites ``show_preview=true`` (if set)."""

    show_preview: bool = False
    """This allows the requester to enable the editor/preview experience."""

    show_progress_stepper: bool = True
    """When only one step remains in the signature request process and this parameter is set to ``false`` then the
    progress stepper will be hidden."""

    test_mode: bool = False
    """Whether this is a test, locked templates will only be available for editing if this is set to ``true``. Defaults
    to ``false``."""


class EmbeddedEditUrlRequestDict(TypedDict):
    allow_edit_ccs: NotRequired[bool]
    cc_roles: NotRequired[list[str]]
    editor_options: NotRequired[SubEditorOptionsDict]
    force_signer_roles: NotRequired[bool]
    force_subject_message: NotRequired[bool]
    merge_fields: NotRequired[list[SubMergeFieldDict]]
    preview_only: NotRequired[bool]
    show_preview: NotRequired[bool]
    show_progress_stepper: NotRequired[bool]
    test_mode: NotRequired[bool]
