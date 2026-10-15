<!-- Generated file — do not edit; regenerated with the SDK. -->

# Fax — operations

Accessor: `client.fax` · Source: `dropbox_sign_api/apis/fax.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.fax.fax_delete

- **Route**: `DELETE /fax/{fax_id}`
- **Auth**: `api_key`
- **Signature**: `def fax_delete(fax_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `fax_id`
- **Params**: `fax_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FaxDeleteErrorBody]`
- **Error**: `FaxDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxDeleteErrorBody` | `dropbox_sign_api/errors/fax_delete_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax.fax_files

- **Route**: `GET /fax/files/{fax_id}`
- **Auth**: `api_key`
- **Signature**: `def fax_files(fax_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `fax_id`
- **Params**: `fax_id` — path
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, FaxFilesErrorBody]`
- **Error**: `FaxFilesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxFilesErrorBody` | `dropbox_sign_api/errors/fax_files_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax.fax_get

- **Route**: `GET /fax/{fax_id}`
- **Auth**: `api_key`
- **Signature**: `def fax_get(fax_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `fax_id`
- **Params**: `fax_id` — path
- **Returns (parsed)**: `FaxGetResponse`
- **Returns (raw)**: `ApiResult[FaxGetResponse, FaxGetErrorBody]`
- **Error**: `FaxGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxGetResponse` | `dropbox_sign_api/models/fax_get_response.py` |
| `FaxGetErrorBody` | `dropbox_sign_api/errors/fax_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax.fax_list

- **Route**: `GET /fax/list`
- **Auth**: `api_key`
- **Signature**: `def fax_list(*, page: int | None = 1, page_size: int | None = 20, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page` — query · `page_size` — query
- **Returns (parsed)**: `FaxListResponse`
- **Returns (raw)**: `ApiResult[FaxListResponse, FaxListErrorBody]`
- **Error**: `FaxListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxListResponse` | `dropbox_sign_api/models/fax_list_response.py` |
| `FaxListErrorBody` | `dropbox_sign_api/errors/fax_list_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.fax.fax_send

- **Route**: `POST /fax/send`
- **Auth**: `api_key`
- **Signature**: `def fax_send(recipient: str, *, sender: str | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, test_mode: bool | None = False, cover_page_to: str | None = None, cover_page_from: str | None = None, cover_page_message: str | None = None, title: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `recipient`
- **Params**: `recipient` — multipart field · `sender` — multipart field · `files` — multipart file · `file_urls` — multipart field · `test_mode` — multipart field · `cover_page_to` — multipart field · `cover_page_from` — multipart field · `cover_page_message` — multipart field · `title` — multipart field
- **Returns (parsed)**: `FaxGetResponse`
- **Returns (raw)**: `ApiResult[FaxGetResponse, FaxSendErrorBody]`
- **Error**: `FaxSendErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FaxGetResponse` | `dropbox_sign_api/models/fax_get_response.py` |
| `FaxSendErrorBody` | `dropbox_sign_api/errors/fax_send_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

