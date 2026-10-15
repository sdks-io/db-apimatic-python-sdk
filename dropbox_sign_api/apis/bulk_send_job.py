from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.bulk_send_job_get_error import BulkSendJobGetErrorBody, bulk_send_job_get_error_mapper
from ..errors.bulk_send_job_list_error import BulkSendJobListErrorBody, bulk_send_job_list_error_mapper
from ..models.bulk_send_job_get_response import BulkSendJobGetResponse
from ..models.bulk_send_job_list_response import BulkSendJobListResponse
from ..server.server import Server


class BulkSendJob:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BulkSendJobWithRawResponse(client, server, auth)

    def bulk_send_job_get(
        self,
        bulk_send_job_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSendJobGetResponse:
        """Returns the status of the BulkSendJob and its SignatureRequests specified by the ``bulk_send_job_id``
        parameter.

        Args:
            bulk_send_job_id: The id of the BulkSendJob to retrieve.
            page: Which page number of the BulkSendJob list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_send_job_get(
                bulk_send_job_id, page=page, page_size=page_size, request_options=request_options
            ),
        )

    def bulk_send_job_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> BulkSendJobListResponse:
        """Returns a list of BulkSendJob that you can access.

        Args:
            page: Which page number of the BulkSendJob List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.bulk_send_job_list(page=page, page_size=page_size, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> BulkSendJobWithRawResponse:
        return self._with_raw_response


class AsyncBulkSendJob:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBulkSendJobWithRawResponse(client, server, auth)

    async def bulk_send_job_get(
        self,
        bulk_send_job_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSendJobGetResponse:
        """Returns the status of the BulkSendJob and its SignatureRequests specified by the ``bulk_send_job_id``
        parameter.

        Args:
            bulk_send_job_id: The id of the BulkSendJob to retrieve.
            page: Which page number of the BulkSendJob list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_send_job_get(
                bulk_send_job_id, page=page, page_size=page_size, request_options=request_options
            ),
        )

    async def bulk_send_job_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> BulkSendJobListResponse:
        """Returns a list of BulkSendJob that you can access.

        Args:
            page: Which page number of the BulkSendJob List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.bulk_send_job_list(
                page=page, page_size=page_size, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncBulkSendJobWithRawResponse:
        return self._with_raw_response


class BulkSendJobWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_send_job_get(
        self,
        bulk_send_job_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSendJobGetResponse, BulkSendJobGetErrorBody]:
        """Returns the status of the BulkSendJob and its SignatureRequests specified by the ``bulk_send_job_id``
        parameter.

        Args:
            bulk_send_job_id: The id of the BulkSendJob to retrieve.
            page: Which page number of the BulkSendJob list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bulk_send_job/{bulk_send_job_id}"),
            path_params=[param[str]("bulk_send_job_id", bulk_send_job_id)],
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[BulkSendJobGetResponse],
            error_mapper=bulk_send_job_get_error_mapper,
            request_options=request_options,
        )

    def bulk_send_job_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BulkSendJobListResponse, BulkSendJobListErrorBody]:
        """Returns a list of BulkSendJob that you can access.

        Args:
            page: Which page number of the BulkSendJob List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bulk_send_job/list"),
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[BulkSendJobListResponse],
            error_mapper=bulk_send_job_list_error_mapper,
            request_options=request_options,
        )


class AsyncBulkSendJobWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_send_job_get(
        self,
        bulk_send_job_id: str,
        *,
        page: int | None = 1,
        page_size: int | None = 20,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSendJobGetResponse, BulkSendJobGetErrorBody]:
        """Returns the status of the BulkSendJob and its SignatureRequests specified by the ``bulk_send_job_id``
        parameter.

        Args:
            bulk_send_job_id: The id of the BulkSendJob to retrieve.
            page: Which page number of the BulkSendJob list to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bulk_send_job/{bulk_send_job_id}"),
            path_params=[param[str]("bulk_send_job_id", bulk_send_job_id)],
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[BulkSendJobGetResponse],
            error_mapper=bulk_send_job_get_error_mapper,
            request_options=request_options,
        )

    async def bulk_send_job_list(
        self, *, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BulkSendJobListResponse, BulkSendJobListErrorBody]:
        """Returns a list of BulkSendJob that you can access.

        Args:
            page: Which page number of the BulkSendJob List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is 20.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/bulk_send_job/list"),
            query_params=[param[int | None]("page", page), param[int | None]("page_size", page_size)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[BulkSendJobListResponse],
            error_mapper=bulk_send_job_list_error_mapper,
            request_options=request_options,
        )
