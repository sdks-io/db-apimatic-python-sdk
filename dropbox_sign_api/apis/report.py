from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.report_create_error import ReportCreateErrorBody, report_create_error_mapper
from ..models.report_create_request import ReportCreateRequest, ReportCreateRequestDict
from ..models.report_create_response import ReportCreateResponse
from ..server.server import Server


class Report:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReportWithRawResponse(client, server, auth)

    def report_create(
        self,
        body: ReportCreateRequest | ReportCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReportCreateResponse:
        """Request the creation of one or more report(s).

        When the report(s) have been generated, you will receive an email (one per requested report type) containing a
        link to download the report as a CSV file. The requested date range may be up to 12 months in duration, and
        ``start_date`` must not be more than 10 years in the past.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.report_create(body, request_options=request_options))

    @property
    def with_raw_response(self) -> ReportWithRawResponse:
        return self._with_raw_response


class AsyncReport:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReportWithRawResponse(client, server, auth)

    async def report_create(
        self,
        body: ReportCreateRequest | ReportCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReportCreateResponse:
        """Request the creation of one or more report(s).

        When the report(s) have been generated, you will receive an email (one per requested report type) containing a
        link to download the report as a CSV file. The requested date range may be up to 12 months in duration, and
        ``start_date`` must not be more than 10 years in the past.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.report_create(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncReportWithRawResponse:
        return self._with_raw_response


class ReportWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def report_create(
        self,
        body: ReportCreateRequest | ReportCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReportCreateResponse, ReportCreateErrorBody]:
        """Request the creation of one or more report(s).

        When the report(s) have been generated, you will receive an email (one per requested report type) containing a
        link to download the report as a CSV file. The requested date range may be up to 12 months in duration, and
        ``start_date`` must not be more than 10 years in the past.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/report/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReportCreateRequest | ReportCreateRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=json_decoder[ReportCreateResponse],
            error_mapper=report_create_error_mapper,
            request_options=request_options,
        )


class AsyncReportWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def report_create(
        self,
        body: ReportCreateRequest | ReportCreateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReportCreateResponse, ReportCreateErrorBody]:
        """Request the creation of one or more report(s).

        When the report(s) have been generated, you will receive an email (one per requested report type) containing a
        link to download the report as a CSV file. The requested date range may be up to 12 months in duration, and
        ``start_date`` must not be more than 10 years in the past.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/report/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReportCreateRequest | ReportCreateRequestDict](body),
            auth_scheme=self._auth.api_key,
            decoder=async_json_decoder[ReportCreateResponse],
            error_mapper=report_create_error_mapper,
            request_options=request_options,
        )
