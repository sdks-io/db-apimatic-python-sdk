from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_response import ErrorResponse

EmbeddedSignUrlErrorBody: TypeAlias = ErrorResponse | RawError


@dataclass(frozen=True, slots=True)
class _EmbeddedSignUrlError:
    def map(self, status_code: int, content: bytes) -> EmbeddedSignUrlErrorBody:
        match status_code:
            case code if 400 <= code <= 499:
                return decode_json[ErrorResponse](content)
            case _:
                return RawError(status_code, content)


embedded_sign_url_error_mapper: Final[ErrorMapper[EmbeddedSignUrlErrorBody]] = _EmbeddedSignUrlError()
