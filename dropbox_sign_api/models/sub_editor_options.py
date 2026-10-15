from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SubEditorOptions(SdkBaseModel):
    """This allows the requester to specify editor options when a preparing a document"""

    allow_edit_signers: bool = False
    """Allows requesters to edit the list of signers"""

    allow_edit_documents: bool = False
    """Allows requesters to edit documents, including delete and add"""


class SubEditorOptionsDict(TypedDict):
    allow_edit_signers: NotRequired[bool]
    allow_edit_documents: NotRequired[bool]
