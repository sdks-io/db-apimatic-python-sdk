from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Operator(str, Enum):
    """Different field types allow different ``operator`` values:
    - Field type of **text**:
      - **is**: exact match
      - **not**: not exact match
      - **match**: regular expression, without /. Example:
        - OK ``[a-zA-Z0-9]``
        - Not OK ``/[a-zA-Z0-9]/``
    - Field type of **dropdown**:
      - **is**: exact match, single value
      - **not**: not exact match, single value
      - **any**: exact match, array of values.
      - **none**: not exact match, array of values.
    - Field type of **checkbox**:
      - **is**: exact match, single value
      - **not**: not exact match, single value
    - Field type of **radio**:
      - **is**: exact match, single value
      - **not**: not exact match, single value"""

    ANY = "any"
    IS = "is"
    MATCH = "match"
    NONE = "none"
    NOT = "not"

    __str__ = str.__str__


OperatorOrStr: TypeAlias = Annotated[Operator | str, open_enum_validator(Operator)]
