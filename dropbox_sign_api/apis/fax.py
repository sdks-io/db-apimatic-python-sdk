from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    file_part,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.fax_delete_error import FaxDeleteErrorBody, fax_delete_error_mapper
from ..errors.fax_files_error import FaxFilesErrorBody, fax_files_error_mapper
from ..errors.fax_get_error import FaxGetErrorBody, fax_get_error_mapper
from ..errors.fax_list_error import FaxListErrorBody, fax_list_error_mapper
from ..errors.fax_send_error import FaxSendErrorBody, fax_send_error_mapper
from ..models.fax_get_response import FaxGetResponse
from ..models.fax_list_response import FaxListResponse
from ..server.server import Server


class Fax:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FaxWithRawResponse(client, server, auth)

    def fax_delete(self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes the specified Fax from the system

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_delete(fax_id, request_options=request_options))

    def fax_files(self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Downloads files associated with a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_files(fax_id, request_options=request_options))

    def fax_get(self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FaxGetResponse:
        """Returns information about a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_get(fax_id, request_options=request_options))

    def fax_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> FaxListResponse:
        """Returns properties of multiple Faxes

        Args:
            page: Which page number of the Fax List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.fax_list(page=page, page_size=page_size, request_options=request_options))

    def fax_send(
        self,
        recipient: str,
        *,
        sender: str | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        test_mode: bool | None = False,
        cover_page_to: str | None = None,
        cover_page_from: str | None = None,
        cover_page_message: str | None = None,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxGetResponse:
        """Creates and sends a new Fax with the submitted file(s)

        Args:
            recipient: Recipient of the fax Can be a phone number in E.164 format or email address
            sender: Fax Send From Sender (used only with fax number)
            files: Use ``files[]`` to indicate the uploaded file(s) to fax This endpoint requires either **files** or
                **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Fax download the file(s) to fax This endpoint requires either
                **files** or **file_urls[]**, but not both.
            test_mode: API Test Mode Setting
            cover_page_to: Fax cover page recipient information
            cover_page_from: Fax cover page sender information
            cover_page_message: Fax Cover Page Message
            title: Fax Title
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.fax_send(
                recipient,
                sender=sender,
                files=files,
                file_urls=file_urls,
                test_mode=test_mode,
                cover_page_to=cover_page_to,
                cover_page_from=cover_page_from,
                cover_page_message=cover_page_message,
                title=title,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> FaxWithRawResponse:
        return self._with_raw_response


class AsyncFax:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFaxWithRawResponse(client, server, auth)

    async def fax_delete(self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Deletes the specified Fax from the system

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_delete(fax_id, request_options=request_options))

    async def fax_files(self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None:
        """Downloads files associated with a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_files(fax_id, request_options=request_options))

    async def fax_get(self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FaxGetResponse:
        """Returns information about a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.fax_get(fax_id, request_options=request_options))

    async def fax_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> FaxListResponse:
        """Returns properties of multiple Faxes

        Args:
            page: Which page number of the Fax List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.fax_list(page=page, page_size=page_size, request_options=request_options)
        )

    async def fax_send(
        self,
        recipient: str,
        *,
        sender: str | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        test_mode: bool | None = False,
        cover_page_to: str | None = None,
        cover_page_from: str | None = None,
        cover_page_message: str | None = None,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FaxGetResponse:
        """Creates and sends a new Fax with the submitted file(s)

        Args:
            recipient: Recipient of the fax Can be a phone number in E.164 format or email address
            sender: Fax Send From Sender (used only with fax number)
            files: Use ``files[]`` to indicate the uploaded file(s) to fax This endpoint requires either **files** or
                **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Fax download the file(s) to fax This endpoint requires either
                **files** or **file_urls[]**, but not both.
            test_mode: API Test Mode Setting
            cover_page_to: Fax cover page recipient information
            cover_page_from: Fax cover page sender information
            cover_page_message: Fax Cover Page Message
            title: Fax Title
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.fax_send(
                recipient,
                sender=sender,
                files=files,
                file_urls=file_urls,
                test_mode=test_mode,
                cover_page_to=cover_page_to,
                cover_page_from=cover_page_from,
                cover_page_message=cover_page_message,
                title=title,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncFaxWithRawResponse:
        return self._with_raw_response


class FaxWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def fax_delete(
        self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FaxDeleteErrorBody]:
        """Deletes the specified Fax from the system

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/fax/{fax_id}"),
            path_params=[param[str]("fax_id", fax_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key,
            decoder=empty_response,
            error_mapper=fax_delete_error_mapper,
            request_options=request_options,
        )

    def fax_files(
        self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FaxFilesErrorBody]:
        """Downloads files associated with a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax/files/{fax_id}"),
            path_params=[param[str]("fax_id", fax_id)],
            auth_scheme=self._auth.api_key,
            decoder=empty_response,
            error_mapper=fax_files_error_mapper,
            request_options=request_options,
        )

    def fax_get(
        self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FaxGetResponse, FaxGetErrorBody]:
        """Returns information about a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax/{fax_id}"),
            path_params=[param[str]("fax_id", fax_id)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxGetResponse],
            error_mapper=fax_get_error_mapper,
            request_options=request_options,
        )

    def fax_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FaxListResponse, FaxListErrorBody]:
        """Returns properties of multiple Faxes

        Args:
            page: Which page number of the Fax List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax/list"),
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxListResponse],
            error_mapper=fax_list_error_mapper,
            request_options=request_options,
        )

    def fax_send(
        self,
        recipient: str,
        *,
        sender: str | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        test_mode: bool | None = False,
        cover_page_to: str | None = None,
        cover_page_from: str | None = None,
        cover_page_message: str | None = None,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxGetResponse, FaxSendErrorBody]:
        """Creates and sends a new Fax with the submitted file(s)

        Args:
            recipient: Recipient of the fax Can be a phone number in E.164 format or email address
            sender: Fax Send From Sender (used only with fax number)
            files: Use ``files[]`` to indicate the uploaded file(s) to fax This endpoint requires either **files** or
                **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Fax download the file(s) to fax This endpoint requires either
                **files** or **file_urls[]**, but not both.
            test_mode: API Test Mode Setting
            cover_page_to: Fax cover page recipient information
            cover_page_from: Fax cover page sender information
            cover_page_message: Fax Cover Page Message
            title: Fax Title
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/fax/send"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("recipient", recipient),
                param[str | None]("sender", sender),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("cover_page_to", cover_page_to),
                param[str | None]("cover_page_from", cover_page_from),
                param[str | None]("cover_page_message", cover_page_message),
                param[str | None]("title", title),
            ),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[FaxGetResponse],
            error_mapper=fax_send_error_mapper,
            request_options=request_options,
        )


class AsyncFaxWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def fax_delete(
        self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FaxDeleteErrorBody]:
        """Deletes the specified Fax from the system

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/fax/{fax_id}"),
            path_params=[param[str]("fax_id", fax_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.api_key,
            decoder=async_empty_response,
            error_mapper=fax_delete_error_mapper,
            request_options=request_options,
        )

    async def fax_files(
        self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, FaxFilesErrorBody]:
        """Downloads files associated with a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax/files/{fax_id}"),
            path_params=[param[str]("fax_id", fax_id)],
            auth_scheme=self._auth.api_key,
            decoder=async_empty_response,
            error_mapper=fax_files_error_mapper,
            request_options=request_options,
        )

    async def fax_get(
        self, fax_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FaxGetResponse, FaxGetErrorBody]:
        """Returns information about a Fax

        Args:
            fax_id: Fax ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax/{fax_id}"),
            path_params=[param[str]("fax_id", fax_id)],
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxGetResponse],
            error_mapper=fax_get_error_mapper,
            request_options=request_options,
        )

    async def fax_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FaxListResponse, FaxListErrorBody]:
        """Returns properties of multiple Faxes

        Args:
            page: Which page number of the Fax List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/fax/list"),
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxListResponse],
            error_mapper=fax_list_error_mapper,
            request_options=request_options,
        )

    async def fax_send(
        self,
        recipient: str,
        *,
        sender: str | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        test_mode: bool | None = False,
        cover_page_to: str | None = None,
        cover_page_from: str | None = None,
        cover_page_message: str | None = None,
        title: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FaxGetResponse, FaxSendErrorBody]:
        """Creates and sends a new Fax with the submitted file(s)

        Args:
            recipient: Recipient of the fax Can be a phone number in E.164 format or email address
            sender: Fax Send From Sender (used only with fax number)
            files: Use ``files[]`` to indicate the uploaded file(s) to fax This endpoint requires either **files** or
                **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Fax download the file(s) to fax This endpoint requires either
                **files** or **file_urls[]**, but not both.
            test_mode: API Test Mode Setting
            cover_page_to: Fax cover page recipient information
            cover_page_from: Fax cover page sender information
            cover_page_message: Fax Cover Page Message
            title: Fax Title
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/fax/send"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("recipient", recipient),
                param[str | None]("sender", sender),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("cover_page_to", cover_page_to),
                param[str | None]("cover_page_from", cover_page_from),
                param[str | None]("cover_page_message", cover_page_message),
                param[str | None]("title", title),
            ),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[FaxGetResponse],
            error_mapper=fax_send_error_mapper,
            request_options=request_options,
        )
