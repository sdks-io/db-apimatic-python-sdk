from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

TemplateDeleteErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _TemplateDeleteError:
    def map(self, status_code: int, content: bytes) -> TemplateDeleteErrorBody:
        match status_code:
            case code if 400 <= code <= 499:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


template_delete_error_mapper: Final[ErrorMapper[TemplateDeleteErrorBody]] = _TemplateDeleteError()
