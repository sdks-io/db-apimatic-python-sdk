from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account import AsyncAccount
from .apis.api_app import AsyncApiApp
from .apis.bulk_send_job import AsyncBulkSendJob
from .apis.document import AsyncDocument
from .apis.embedded import AsyncEmbedded
from .apis.fax import AsyncFax
from .apis.fax_line import AsyncFaxLine
from .apis.oauth import AsyncOauth
from .apis.report import AsyncReport
from .apis.signature_request import AsyncSignatureRequest
from .apis.team import AsyncTeam
from .apis.template import AsyncTemplate
from .apis.unclaimed_draft import AsyncUnclaimedDraft
from .auth import AsyncAuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseDropboxSignApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncRawClient,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    BearerAuthScheme,
    LoggingOptionsOrDict,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment


class AsyncDropboxSignApiClient(BaseDropboxSignApiClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        api_key: BasicAuthCredentialsOrDict | None = None,
        oauth2: str | None = None,
    ) -> None:
        super().__init__(
            environment=environment,
            base_url=base_url,
            timeout=timeout,
            retry_options=retry_options,
            logging_options=logging_options,
        )
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            logging_options=self._logging_options,
            global_headers=[
                param[str]("User-Agent", "DropboxSignApiClient/3.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "3.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            api_key=BasicAuthScheme(BasicAuthCredentials.coerce(api_key)) if api_key is not None else no_auth,
            oauth2=BearerAuthScheme(oauth2) if oauth2 is not None else no_auth,
        )

    @cached_property
    def account(self) -> AsyncAccount:
        return AsyncAccount(self._raw_client, self._server, self._auth)

    @cached_property
    def api_app(self) -> AsyncApiApp:
        return AsyncApiApp(self._raw_client, self._server, self._auth)

    @cached_property
    def bulk_send_job(self) -> AsyncBulkSendJob:
        return AsyncBulkSendJob(self._raw_client, self._server, self._auth)

    @cached_property
    def document(self) -> AsyncDocument:
        return AsyncDocument(self._raw_client, self._server, self._auth)

    @cached_property
    def embedded(self) -> AsyncEmbedded:
        return AsyncEmbedded(self._raw_client, self._server, self._auth)

    @cached_property
    def fax(self) -> AsyncFax:
        return AsyncFax(self._raw_client, self._server, self._auth)

    @cached_property
    def fax_line(self) -> AsyncFaxLine:
        return AsyncFaxLine(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> AsyncOauth:
        return AsyncOauth(self._raw_client, self._server)

    @cached_property
    def report(self) -> AsyncReport:
        return AsyncReport(self._raw_client, self._server, self._auth)

    @cached_property
    def signature_request(self) -> AsyncSignatureRequest:
        return AsyncSignatureRequest(self._raw_client, self._server, self._auth)

    @cached_property
    def team(self) -> AsyncTeam:
        return AsyncTeam(self._raw_client, self._server, self._auth)

    @cached_property
    def template(self) -> AsyncTemplate:
        return AsyncTemplate(self._raw_client, self._server, self._auth)

    @cached_property
    def unclaimed_draft(self) -> AsyncUnclaimedDraft:
        return AsyncUnclaimedDraft(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncDropboxSignApiClient
