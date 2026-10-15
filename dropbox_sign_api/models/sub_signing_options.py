from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.default_type import DefaultTypeOrStr


class SubSigningOptions(SdkBaseModel):
    """This allows the requester to specify the types allowed for creating a signature and specify another signing
    options.

    **NOTE:** If ``signing_options`` are not defined in the request, the allowed types will default to those specified
    in the account settings.

    **NOTE:** If ``force_advanced_signature_details`` is set, allowed types has to be defined too."""

    default_type: DefaultTypeOrStr
    """The default type shown (limited to the listed types)"""

    draw: bool = False
    """Allows drawing the signature"""

    phone: bool = False
    """Allows using a smartphone to email the signature"""

    type_: bool = Field(default=False, alias="type")
    """Allows typing the signature"""

    upload: bool = False
    """Allows uploading the signature"""

    force_advanced_signature_details: bool = False
    """Turning on advanced signature details for the signature request"""


class SubSigningOptionsDict(TypedDict):
    default_type: DefaultTypeOrStr
    draw: NotRequired[bool]
    phone: NotRequired[bool]
    type_: NotRequired[bool]
    upload: NotRequired[bool]
    force_advanced_signature_details: NotRequired[bool]
