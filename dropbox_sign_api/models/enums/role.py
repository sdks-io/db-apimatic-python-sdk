from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Role(str, Enum):
    """A role member will take in a new Team.

    **NOTE:** This parameter is used only if ``team_id`` is provided."""

    MEMBER = "Member"
    DEVELOPER = "Developer"
    TEAM_MANAGER = "Team Manager"
    ADMIN = "Admin"

    __str__ = str.__str__


RoleOrStr: TypeAlias = Annotated[Role | str, open_enum_validator(Role)]
