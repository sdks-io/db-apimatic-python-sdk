from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.type import TypeOrStr


class SubMergeField(SdkBaseModel):
    name: str
    """The name of the merge field. Must be unique."""

    type_: TypeOrStr = Field(alias="type")
    """The type of merge field."""


class SubMergeFieldDict(TypedDict):
    name: str
    type_: TypeOrStr
