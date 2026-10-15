from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

ApiAppGetErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _ApiAppGetError:
    def map(self, status_code: int, content: bytes) -> ApiAppGetErrorBody:
        match status_code:
            case code if 400 <= code <= 499:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


api_app_get_error_mapper: Final[ErrorMapper[ApiAppGetErrorBody]] = _ApiAppGetError()
