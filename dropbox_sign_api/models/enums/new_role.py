from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class NewRole(str, Enum):
    """A new role member will take in a new Team.

    **NOTE:** This parameter is used only if ``new_team_id`` is provided."""

    MEMBER = "Member"
    DEVELOPER = "Developer"
    TEAM_MANAGER = "Team Manager"
    ADMIN = "Admin"

    __str__ = str.__str__


NewRoleOrStr: TypeAlias = Annotated[NewRole | str, open_enum_validator(NewRole)]
