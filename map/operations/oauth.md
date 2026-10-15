<!-- Generated file — do not edit; regenerated with the SDK. -->

# Oauth — operations

Accessor: `client.oauth` · Source: `dropbox_sign_api/apis/oauth.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.oauth.oauth_token_generate

- **Route**: `POST /oauth/token`
- **Signature**: `def oauth_token_generate(body: OauthTokenGenerateRequest | OauthTokenGenerateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OauthTokenResponse`
- **Returns (raw)**: `ApiResult[OauthTokenResponse, OauthTokenGenerateErrorBody]`
- **Error**: `OauthTokenGenerateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OauthTokenGenerateRequest` | `dropbox_sign_api/models/oauth_token_generate_request.py` |
| `OauthTokenGenerateRequestDict` | `dropbox_sign_api/models/oauth_token_generate_request.py` |
| `OauthTokenResponse` | `dropbox_sign_api/models/oauth_token_response.py` |
| `OauthTokenGenerateErrorBody` | `dropbox_sign_api/errors/oauth_token_generate_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.oauth.oauth_token_refresh

- **Route**: `POST /oauth/token?refresh`
- **Signature**: `def oauth_token_refresh(body: OauthTokenRefreshRequest | OauthTokenRefreshRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OauthTokenResponse`
- **Returns (raw)**: `ApiResult[OauthTokenResponse, OauthTokenRefreshErrorBody]`
- **Error**: `OauthTokenRefreshErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OauthTokenRefreshRequest` | `dropbox_sign_api/models/oauth_token_refresh_request.py` |
| `OauthTokenRefreshRequestDict` | `dropbox_sign_api/models/oauth_token_refresh_request.py` |
| `OauthTokenResponse` | `dropbox_sign_api/models/oauth_token_response.py` |
| `OauthTokenRefreshErrorBody` | `dropbox_sign_api/errors/oauth_token_refresh_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

