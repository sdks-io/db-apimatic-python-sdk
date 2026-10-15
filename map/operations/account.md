<!-- Generated file — do not edit; regenerated with the SDK. -->

# Account — operations

Accessor: `client.account` · Source: `dropbox_sign_api/apis/account.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account.account_create

- **Route**: `POST /account/create`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def account_create(body: AccountCreateRequest | AccountCreateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountCreateResponse`
- **Returns (raw)**: `ApiResult[AccountCreateResponse, AccountCreateErrorBody]`
- **Error**: `AccountCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountCreateRequest` | `dropbox_sign_api/models/account_create_request.py` |
| `AccountCreateRequestDict` | `dropbox_sign_api/models/account_create_request.py` |
| `AccountCreateResponse` | `dropbox_sign_api/models/account_create_response.py` |
| `AccountCreateErrorBody` | `dropbox_sign_api/errors/account_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.account.account_get

- **Route**: `GET /account`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def account_get(*, account_id: str | None = None, email_address: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `account_id` — query · `email_address` — query
- **Returns (parsed)**: `AccountGetResponse`
- **Returns (raw)**: `ApiResult[AccountGetResponse, AccountGetErrorBody]`
- **Error**: `AccountGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountGetResponse` | `dropbox_sign_api/models/account_get_response.py` |
| `AccountGetErrorBody` | `dropbox_sign_api/errors/account_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.account.account_update

- **Route**: `PUT /account`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def account_update(body: AccountUpdateRequest | AccountUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountGetResponse`
- **Returns (raw)**: `ApiResult[AccountGetResponse, AccountUpdateErrorBody]`
- **Error**: `AccountUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountUpdateRequest` | `dropbox_sign_api/models/account_update_request.py` |
| `AccountUpdateRequestDict` | `dropbox_sign_api/models/account_update_request.py` |
| `AccountGetResponse` | `dropbox_sign_api/models/account_get_response.py` |
| `AccountUpdateErrorBody` | `dropbox_sign_api/errors/account_update_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.account.account_verify

- **Route**: `POST /account/verify`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def account_verify(body: AccountVerifyRequest | AccountVerifyRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `AccountVerifyResponse`
- **Returns (raw)**: `ApiResult[AccountVerifyResponse, AccountVerifyErrorBody]`
- **Error**: `AccountVerifyErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AccountVerifyRequest` | `dropbox_sign_api/models/account_verify_request.py` |
| `AccountVerifyRequestDict` | `dropbox_sign_api/models/account_verify_request.py` |
| `AccountVerifyResponse` | `dropbox_sign_api/models/account_verify_response.py` |
| `AccountVerifyErrorBody` | `dropbox_sign_api/errors/account_verify_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

