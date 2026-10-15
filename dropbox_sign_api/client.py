from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account import Account
from .apis.api_app import ApiApp
from .apis.bulk_send_job import BulkSendJob
from .apis.document import Document
from .apis.embedded import Embedded
from .apis.fax import Fax
from .apis.fax_line import FaxLine
from .apis.oauth import Oauth
from .apis.report import Report
from .apis.signature_request import SignatureRequest
from .apis.team import Team
from .apis.template import Template
from .apis.unclaimed_draft import UnclaimedDraft
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseDropboxSignApiClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    BearerAuthScheme,
    HttpClient,
    Httpx2Client,
    LoggingOptionsOrDict,
    RawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)
from .server.environment import Environment


class DropboxSignApiClient(BaseDropboxSignApiClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
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
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
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
        self._auth = AuthSchemes(
            api_key=BasicAuthScheme(BasicAuthCredentials.coerce(api_key)) if api_key is not None else no_auth,
            oauth2=BearerAuthScheme(oauth2) if oauth2 is not None else no_auth,
        )

    @cached_property
    def account(self) -> Account:
        return Account(self._raw_client, self._server, self._auth)

    @cached_property
    def api_app(self) -> ApiApp:
        return ApiApp(self._raw_client, self._server, self._auth)

    @cached_property
    def bulk_send_job(self) -> BulkSendJob:
        return BulkSendJob(self._raw_client, self._server, self._auth)

    @cached_property
    def document(self) -> Document:
        return Document(self._raw_client, self._server, self._auth)

    @cached_property
    def embedded(self) -> Embedded:
        return Embedded(self._raw_client, self._server, self._auth)

    @cached_property
    def fax(self) -> Fax:
        return Fax(self._raw_client, self._server, self._auth)

    @cached_property
    def fax_line(self) -> FaxLine:
        return FaxLine(self._raw_client, self._server, self._auth)

    @cached_property
    def oauth(self) -> Oauth:
        return Oauth(self._raw_client, self._server)

    @cached_property
    def report(self) -> Report:
        return Report(self._raw_client, self._server, self._auth)

    @cached_property
    def signature_request(self) -> SignatureRequest:
        return SignatureRequest(self._raw_client, self._server, self._auth)

    @cached_property
    def team(self) -> Team:
        return Team(self._raw_client, self._server, self._auth)

    @cached_property
    def template(self) -> Template:
        return Template(self._raw_client, self._server, self._auth)

    @cached_property
    def unclaimed_draft(self) -> UnclaimedDraft:
        return UnclaimedDraft(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = DropboxSignApiClient
