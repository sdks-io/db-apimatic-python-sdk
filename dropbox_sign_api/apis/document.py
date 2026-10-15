from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    file_part,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.document_detect_fields_error import DocumentDetectFieldsErrorBody, document_detect_fields_error_mapper
from ..models.document_field_detection_response import DocumentFieldDetectionResponse
from ..models.unions.detection_mode import DetectionMode, DetectionModeDict
from ..server.server import Server


class Document:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DocumentWithRawResponse(client, server, auth)

    def document_detect_fields(
        self,
        detection_mode: DetectionMode | DetectionModeDict,
        *,
        file: FileInput | None = None,
        file_url: str | None = None,
        page_range: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DocumentFieldDetectionResponse:
        """Detects form fields in a PDF document using either PDF form annotations or Dropbox Sign text tags.

        Args:
            detection_mode: The field detection method to use. Set to ``annotations`` to detect PDF form annotations or
                ``text_tags`` to detect Dropbox Sign text tags.
            file: The PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but not both.
            file_url: The URL of the PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but
                not both.
            page_range: The zero-based page indexes to analyze. Accepts ``all``, individual pages, inclusive ranges, or
                comma-separated combinations, such as ``0-2,5,7-9``. Defaults to ``all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.document_detect_fields(
                detection_mode, file=file, file_url=file_url, page_range=page_range, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> DocumentWithRawResponse:
        return self._with_raw_response


class AsyncDocument:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDocumentWithRawResponse(client, server, auth)

    async def document_detect_fields(
        self,
        detection_mode: DetectionMode | DetectionModeDict,
        *,
        file: AsyncFileInput | None = None,
        file_url: str | None = None,
        page_range: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DocumentFieldDetectionResponse:
        """Detects form fields in a PDF document using either PDF form annotations or Dropbox Sign text tags.

        Args:
            detection_mode: The field detection method to use. Set to ``annotations`` to detect PDF form annotations or
                ``text_tags`` to detect Dropbox Sign text tags.
            file: The PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but not both.
            file_url: The URL of the PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but
                not both.
            page_range: The zero-based page indexes to analyze. Accepts ``all``, individual pages, inclusive ranges, or
                comma-separated combinations, such as ``0-2,5,7-9``. Defaults to ``all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.document_detect_fields(
                detection_mode, file=file, file_url=file_url, page_range=page_range, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncDocumentWithRawResponse:
        return self._with_raw_response


class DocumentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def document_detect_fields(
        self,
        detection_mode: DetectionMode | DetectionModeDict,
        *,
        file: FileInput | None = None,
        file_url: str | None = None,
        page_range: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DocumentFieldDetectionResponse, DocumentDetectFieldsErrorBody]:
        """Detects form fields in a PDF document using either PDF form annotations or Dropbox Sign text tags.

        Args:
            detection_mode: The field detection method to use. Set to ``annotations`` to detect PDF form annotations or
                ``text_tags`` to detect Dropbox Sign text tags.
            file: The PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but not both.
            file_url: The URL of the PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but
                not both.
            page_range: The zero-based page indexes to analyze. Accepts ``all``, individual pages, inclusive ranges, or
                comma-separated combinations, such as ``0-2,5,7-9``. Defaults to ``all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/document/detect_fields"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[DetectionMode | DetectionModeDict]("detection_mode", detection_mode),
                file_part("file", file) if file is not None else None,
                param[str | None]("file_url", file_url),
                param[str | None]("page_range", page_range),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[DocumentFieldDetectionResponse],
            error_mapper=document_detect_fields_error_mapper,
            request_options=request_options,
        )


class AsyncDocumentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def document_detect_fields(
        self,
        detection_mode: DetectionMode | DetectionModeDict,
        *,
        file: AsyncFileInput | None = None,
        file_url: str | None = None,
        page_range: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DocumentFieldDetectionResponse, DocumentDetectFieldsErrorBody]:
        """Detects form fields in a PDF document using either PDF form annotations or Dropbox Sign text tags.

        Args:
            detection_mode: The field detection method to use. Set to ``annotations`` to detect PDF form annotations or
                ``text_tags`` to detect Dropbox Sign text tags.
            file: The PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but not both.
            file_url: The URL of the PDF file to analyze. This endpoint requires either ``file`` or ``file_url``, but
                not both.
            page_range: The zero-based page indexes to analyze. Accepts ``all``, individual pages, inclusive ranges, or
                comma-separated combinations, such as ``0-2,5,7-9``. Defaults to ``all``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/document/detect_fields"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[DetectionMode | DetectionModeDict]("detection_mode", detection_mode),
                file_part("file", file) if file is not None else None,
                param[str | None]("file_url", file_url),
                param[str | None]("page_range", page_range),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[DocumentFieldDetectionResponse],
            error_mapper=document_detect_fields_error_mapper,
            request_options=request_options,
        )
