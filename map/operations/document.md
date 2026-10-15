<!-- Generated file — do not edit; regenerated with the SDK. -->

# Document — operations

Accessor: `client.document` · Source: `dropbox_sign_api/apis/document.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.document.document_detect_fields

- **Route**: `POST /document/detect_fields`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def document_detect_fields(detection_mode: DetectionMode | DetectionModeDict, *, file: FileInput | None = None, file_url: str | None = None, page_range: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `detection_mode`
- **Params**: `detection_mode` — multipart field · `file` — multipart file · `file_url` — multipart field · `page_range` — multipart field
- **Returns (parsed)**: `DocumentFieldDetectionResponse`
- **Returns (raw)**: `ApiResult[DocumentFieldDetectionResponse, DocumentDetectFieldsErrorBody]`
- **Error**: `DocumentDetectFieldsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DetectionMode` | `dropbox_sign_api/models/unions/detection_mode.py` |
| `DetectionModeDict` | `dropbox_sign_api/models/unions/detection_mode.py` |
| `DocumentFieldDetectionResponse` | `dropbox_sign_api/models/document_field_detection_response.py` |
| `DocumentDetectFieldsErrorBody` | `dropbox_sign_api/errors/document_detect_fields_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

