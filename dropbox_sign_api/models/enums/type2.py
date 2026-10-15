from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type2(str, Enum):
    """The type of unclaimed draft to create. Use ``send_document`` to create a claimable file, and
    ``request_signature`` for a claimable signature request. If the type is ``request_signature`` then signers name and
    email_address are not optional."""

    SEND_DOCUMENT = "send_document"
    REQUEST_SIGNATURE = "request_signature"

    __str__ = str.__str__


Type2OrStr: TypeAlias = Annotated[Type2 | str, open_enum_validator(Type2)]
