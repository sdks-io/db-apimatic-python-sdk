<!-- Generated file — do not edit; regenerated with the SDK. -->

# Embedded — operations

Accessor: `client.embedded` · Source: `dropbox_sign_api/apis/embedded.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.embedded.embedded_edit_url

- **Route**: `POST /embedded/edit_url/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def embedded_edit_url(template_id: str, body: EmbeddedEditUrlRequest | EmbeddedEditUrlRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`, `body`
- **Params**: `template_id` — path · `body` — JSON body
- **Returns (parsed)**: `EmbeddedEditUrlResponse`
- **Returns (raw)**: `ApiResult[EmbeddedEditUrlResponse, EmbeddedEditUrlErrorBody]`
- **Error**: `EmbeddedEditUrlErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EmbeddedEditUrlRequest` | `dropbox_sign_api/models/embedded_edit_url_request.py` |
| `EmbeddedEditUrlRequestDict` | `dropbox_sign_api/models/embedded_edit_url_request.py` |
| `EmbeddedEditUrlResponse` | `dropbox_sign_api/models/embedded_edit_url_response.py` |
| `EmbeddedEditUrlErrorBody` | `dropbox_sign_api/errors/embedded_edit_url_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.embedded.embedded_sign_url

- **Route**: `GET /embedded/sign_url/{signature_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def embedded_sign_url(signature_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_id`
- **Params**: `signature_id` — path
- **Returns (parsed)**: `EmbeddedSignUrlResponse`
- **Returns (raw)**: `ApiResult[EmbeddedSignUrlResponse, EmbeddedSignUrlErrorBody]`
- **Error**: `EmbeddedSignUrlErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EmbeddedSignUrlResponse` | `dropbox_sign_api/models/embedded_sign_url_response.py` |
| `EmbeddedSignUrlErrorBody` | `dropbox_sign_api/errors/embedded_sign_url_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

