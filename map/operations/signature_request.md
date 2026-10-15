<!-- Generated file — do not edit; regenerated with the SDK. -->

# SignatureRequest — operations

Accessor: `client.signature_request` · Source: `dropbox_sign_api/apis/signature_request.py` · 20 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.signature_request.signature_request_bulk_create_embedded_with_template

- **Route**: `POST /signature_request/bulk_create_embedded_with_template`
- **Auth**: `api_key`
- **Signature**: `def signature_request_bulk_create_embedded_with_template(template_ids: list[str], client_id: str, *, signer_file: FileInput | None = None, signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_ids`, `client_id`
- **Params**: `template_ids` — multipart field · `client_id` — multipart field · `signer_file` — multipart file · `signer_list` — multipart field · `allow_decline` — multipart field · `ccs` — multipart field · `custom_fields` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `BulkSendJobSendResponse`
- **Returns (raw)**: `ApiResult[BulkSendJobSendResponse, SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody]`
- **Error**: `SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubBulkSignerList` | `dropbox_sign_api/models/sub_bulk_signer_list.py` |
| `SubBulkSignerListDict` | `dropbox_sign_api/models/sub_bulk_signer_list.py` |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `BulkSendJobSendResponse` | `dropbox_sign_api/models/bulk_send_job_send_response.py` |
| `SignatureRequestBulkCreateEmbeddedWithTemplateErrorBody` | `dropbox_sign_api/errors/signature_request_bulk_create_embedded_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_bulk_send_with_template

- **Route**: `POST /signature_request/bulk_send_with_template`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_bulk_send_with_template(template_ids: list[str], *, signer_file: FileInput | None = None, signer_list: list[SubBulkSignerList | SubBulkSignerListDict] | None = None, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_ids`
- **Params**: `template_ids` — multipart field · `signer_file` — multipart file · `signer_list` — multipart field · `allow_decline` — multipart field · `ccs` — multipart field · `client_id` — multipart field · `custom_fields` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `BulkSendJobSendResponse`
- **Returns (raw)**: `ApiResult[BulkSendJobSendResponse, SignatureRequestBulkSendWithTemplateErrorBody]`
- **Error**: `SignatureRequestBulkSendWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubBulkSignerList` | `dropbox_sign_api/models/sub_bulk_signer_list.py` |
| `SubBulkSignerListDict` | `dropbox_sign_api/models/sub_bulk_signer_list.py` |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `BulkSendJobSendResponse` | `dropbox_sign_api/models/bulk_send_job_send_response.py` |
| `SignatureRequestBulkSendWithTemplateErrorBody` | `dropbox_sign_api/errors/signature_request_bulk_send_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_cancel

- **Route**: `POST /signature_request/cancel/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_cancel(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SignatureRequestCancelErrorBody]`
- **Error**: `SignatureRequestCancelErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestCancelErrorBody` | `dropbox_sign_api/errors/signature_request_cancel_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_create_embedded

- **Route**: `POST /signature_request/create_embedded`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_create_embedded(client_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`
- **Params**: `client_id` — multipart field · `files` — multipart file · `file_urls` — multipart field · `signers` — multipart field · `grouped_signers` — multipart field · `allow_decline` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_email_addresses` — multipart field · `custom_fields` — multipart field · `field_options` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `hide_text_tags` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `use_text_tags` — multipart field · `ignore_text_tags_extraction_errors` — multipart field · `populate_auto_fill_fields` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedErrorBody]`
- **Error**: `SignatureRequestCreateEmbeddedErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestSigner` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestSignerDict` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestGroupedSigners` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubSignatureRequestGroupedSignersDict` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestCreateEmbeddedErrorBody` | `dropbox_sign_api/errors/signature_request_create_embedded_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_create_embedded_with_template

- **Route**: `POST /signature_request/create_embedded_with_template`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_create_embedded_with_template(template_ids: list[str], client_id: str, signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_ids`, `client_id`, `signers`
- **Params**: `template_ids` — multipart field · `client_id` — multipart field · `signers` — multipart field · `allow_decline` — multipart field · `ccs` — multipart field · `custom_fields` — multipart field · `files` — multipart file · `file_urls` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `populate_auto_fill_fields` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestCreateEmbeddedWithTemplateErrorBody]`
- **Error**: `SignatureRequestCreateEmbeddedWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestTemplateSigner` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubSignatureRequestTemplateSignerDict` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestCreateEmbeddedWithTemplateErrorBody` | `dropbox_sign_api/errors/signature_request_create_embedded_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_edit

- **Route**: `PUT /signature_request/edit/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_edit(signature_request_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path · `files` — multipart file · `file_urls` — multipart field · `signers` — multipart field · `grouped_signers` — multipart field · `allow_decline` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_email_addresses` — multipart field · `client_id` — multipart field · `custom_fields` — multipart field · `field_options` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `hide_text_tags` — multipart field · `is_eid` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `use_text_tags` — multipart field · `ignore_text_tags_extraction_errors` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestEditErrorBody]`
- **Error**: `SignatureRequestEditErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestSigner` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestSignerDict` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestGroupedSigners` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubSignatureRequestGroupedSignersDict` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestEditErrorBody` | `dropbox_sign_api/errors/signature_request_edit_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_edit_embedded

- **Route**: `PUT /signature_request/edit_embedded/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_edit_embedded(signature_request_id: str, client_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, populate_auto_fill_fields: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`, `client_id`
- **Params**: `signature_request_id` — path · `client_id` — multipart field · `files` — multipart file · `file_urls` — multipart field · `signers` — multipart field · `grouped_signers` — multipart field · `allow_decline` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_email_addresses` — multipart field · `custom_fields` — multipart field · `field_options` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `hide_text_tags` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `use_text_tags` — multipart field · `ignore_text_tags_extraction_errors` — multipart field · `populate_auto_fill_fields` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedErrorBody]`
- **Error**: `SignatureRequestEditEmbeddedErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestSigner` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestSignerDict` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestGroupedSigners` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubSignatureRequestGroupedSignersDict` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestEditEmbeddedErrorBody` | `dropbox_sign_api/errors/signature_request_edit_embedded_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_edit_embedded_with_template

- **Route**: `PUT /signature_request/edit_embedded_with_template/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_edit_embedded_with_template(signature_request_id: str, template_ids: list[str], client_id: str, signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, populate_auto_fill_fields: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`, `template_ids`, `client_id`, `signers`
- **Params**: `signature_request_id` — path · `template_ids` — multipart field · `client_id` — multipart field · `signers` — multipart field · `allow_decline` — multipart field · `ccs` — multipart field · `custom_fields` — multipart field · `files` — multipart file · `file_urls` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `populate_auto_fill_fields` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestEditEmbeddedWithTemplateErrorBody]`
- **Error**: `SignatureRequestEditEmbeddedWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestTemplateSigner` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubSignatureRequestTemplateSignerDict` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestEditEmbeddedWithTemplateErrorBody` | `dropbox_sign_api/errors/signature_request_edit_embedded_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_edit_with_template

- **Route**: `PUT /signature_request/edit_with_template/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_edit_with_template(signature_request_id: str, template_ids: list[str], signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`, `template_ids`, `signers`
- **Params**: `signature_request_id` — path · `template_ids` — multipart field · `signers` — multipart field · `allow_decline` — multipart field · `ccs` — multipart field · `client_id` — multipart field · `custom_fields` — multipart field · `files` — multipart file · `file_urls` — multipart field · `is_eid` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestEditWithTemplateErrorBody]`
- **Error**: `SignatureRequestEditWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestTemplateSigner` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubSignatureRequestTemplateSignerDict` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestEditWithTemplateErrorBody` | `dropbox_sign_api/errors/signature_request_edit_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_files

- **Route**: `GET /signature_request/files/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_files(signature_request_id: str, *, file_type: FileTypeOrStr | None = FileType.PDF, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path · `file_type` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SignatureRequestFilesErrorBody]`
- **Error**: `SignatureRequestFilesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FileTypeOrStr` | `dropbox_sign_api/models/enums/file_type.py` |
| `SignatureRequestFilesErrorBody` | `dropbox_sign_api/errors/signature_request_files_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_files_as_data_uri

- **Route**: `GET /signature_request/files_as_data_uri/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_files_as_data_uri(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path
- **Returns (parsed)**: `FileResponseDataUri`
- **Returns (raw)**: `ApiResult[FileResponseDataUri, SignatureRequestFilesAsDataUriErrorBody]`
- **Error**: `SignatureRequestFilesAsDataUriErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FileResponseDataUri` | `dropbox_sign_api/models/file_response_data_uri.py` |
| `SignatureRequestFilesAsDataUriErrorBody` | `dropbox_sign_api/errors/signature_request_files_as_data_uri_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_files_as_file_url

- **Route**: `GET /signature_request/files_as_file_url/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_files_as_file_url(signature_request_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path · `force_download` — query
- **Returns (parsed)**: `FileResponseModel`
- **Returns (raw)**: `ApiResult[FileResponseModel, SignatureRequestFilesAsFileUrlErrorBody]`
- **Error**: `SignatureRequestFilesAsFileUrlErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FileResponseModel` | `dropbox_sign_api/models/file_response_model.py` |
| `SignatureRequestFilesAsFileUrlErrorBody` | `dropbox_sign_api/errors/signature_request_files_as_file_url_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_get

- **Route**: `GET /signature_request/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_get(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestGetErrorBody]`
- **Error**: `SignatureRequestGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestGetErrorBody` | `dropbox_sign_api/errors/signature_request_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_list

- **Route**: `GET /signature_request/list`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_list(*, account_id: str | None = None, page: int | None = 1, page_size: int | None = 20, query: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `account_id` — query · `page` — query · `page_size` — query · `query` — query
- **Returns (parsed)**: `SignatureRequestListResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestListResponse, SignatureRequestListErrorBody]`
- **Error**: `SignatureRequestListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestListResponse` | `dropbox_sign_api/models/signature_request_list_response.py` |
| `SignatureRequestListErrorBody` | `dropbox_sign_api/errors/signature_request_list_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_release_hold

- **Route**: `POST /signature_request/release_hold/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_release_hold(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestReleaseHoldErrorBody]`
- **Error**: `SignatureRequestReleaseHoldErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestReleaseHoldErrorBody` | `dropbox_sign_api/errors/signature_request_release_hold_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_remind

- **Route**: `POST /signature_request/remind/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_remind(signature_request_id: str, body: SignatureRequestRemindRequest | SignatureRequestRemindRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`, `body`
- **Params**: `signature_request_id` — path · `body` — JSON body
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestRemindErrorBody]`
- **Error**: `SignatureRequestRemindErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestRemindRequest` | `dropbox_sign_api/models/signature_request_remind_request.py` |
| `SignatureRequestRemindRequestDict` | `dropbox_sign_api/models/signature_request_remind_request.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestRemindErrorBody` | `dropbox_sign_api/errors/signature_request_remind_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_remove

- **Route**: `POST /signature_request/remove/{signature_request_id}`
- **Auth**: `api_key`
- **Signature**: `def signature_request_remove(signature_request_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`
- **Params**: `signature_request_id` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SignatureRequestRemoveErrorBody]`
- **Error**: `SignatureRequestRemoveErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestRemoveErrorBody` | `dropbox_sign_api/errors/signature_request_remove_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_send

- **Route**: `POST /signature_request/send`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_send(*, files: FileInput | None = None, file_urls: list[str] | None = None, signers: list[SubSignatureRequestSigner | SubSignatureRequestSignerDict] | None = None, grouped_signers: list[SubSignatureRequestGroupedSigners | SubSignatureRequestGroupedSignersDict] | None = None, allow_decline: bool | None = False, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_email_addresses: list[EmailStr] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, hide_text_tags: bool | None = False, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_text_tags: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `files` — multipart file · `file_urls` — multipart field · `signers` — multipart field · `grouped_signers` — multipart field · `allow_decline` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_email_addresses` — multipart field · `client_id` — multipart field · `custom_fields` — multipart field · `field_options` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `hide_text_tags` — multipart field · `is_eid` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `use_text_tags` — multipart field · `ignore_text_tags_extraction_errors` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestSendErrorBody]`
- **Error**: `SignatureRequestSendErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestSigner` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestSignerDict` | `dropbox_sign_api/models/sub_signature_request_signer.py` |
| `SubSignatureRequestGroupedSigners` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubSignatureRequestGroupedSignersDict` | `dropbox_sign_api/models/sub_signature_request_grouped_signers.py` |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestSendErrorBody` | `dropbox_sign_api/errors/signature_request_send_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_send_with_template

- **Route**: `POST /signature_request/send_with_template`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_send_with_template(template_ids: list[str], signers: list[SubSignatureRequestTemplateSigner | SubSignatureRequestTemplateSignerDict], *, allow_decline: bool | None = False, ccs: list[SubCc | SubCcDict] | None = None, client_id: str | None = None, custom_fields: list[SubCustomField | SubCustomFieldDict] | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, is_eid: bool | None = False, message: str | None = None, metadata: dict[str, Any] | None = None, signing_options: SubSigningOptions | SubSigningOptionsDict | None = None, signing_redirect_url: str | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, expires_at: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_ids`, `signers`
- **Params**: `template_ids` — multipart field · `signers` — multipart field · `allow_decline` — multipart field · `ccs` — multipart field · `client_id` — multipart field · `custom_fields` — multipart field · `files` — multipart file · `file_urls` — multipart field · `is_eid` — multipart field · `message` — multipart field · `metadata` — multipart field · `signing_options` — multipart field · `signing_redirect_url` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `expires_at` — multipart field
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestSendWithTemplateErrorBody]`
- **Error**: `SignatureRequestSendWithTemplateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubSignatureRequestTemplateSigner` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubSignatureRequestTemplateSignerDict` | `dropbox_sign_api/models/sub_signature_request_template_signer.py` |
| `SubCc` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCcDict` | `dropbox_sign_api/models/sub_cc.py` |
| `SubCustomField` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubCustomFieldDict` | `dropbox_sign_api/models/sub_custom_field.py` |
| `SubSigningOptions` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SubSigningOptionsDict` | `dropbox_sign_api/models/sub_signing_options.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestSendWithTemplateErrorBody` | `dropbox_sign_api/errors/signature_request_send_with_template_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.signature_request.signature_request_update

- **Route**: `POST /signature_request/update/{signature_request_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def signature_request_update(signature_request_id: str, body: SignatureRequestUpdateRequest | SignatureRequestUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `signature_request_id`, `body`
- **Params**: `signature_request_id` — path · `body` — JSON body
- **Returns (parsed)**: `SignatureRequestGetResponse`
- **Returns (raw)**: `ApiResult[SignatureRequestGetResponse, SignatureRequestUpdateErrorBody]`
- **Error**: `SignatureRequestUpdateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SignatureRequestUpdateRequest` | `dropbox_sign_api/models/signature_request_update_request.py` |
| `SignatureRequestUpdateRequestDict` | `dropbox_sign_api/models/signature_request_update_request.py` |
| `SignatureRequestGetResponse` | `dropbox_sign_api/models/signature_request_get_response.py` |
| `SignatureRequestUpdateErrorBody` | `dropbox_sign_api/errors/signature_request_update_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

