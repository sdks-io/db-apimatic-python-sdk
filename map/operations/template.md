<!-- Generated file — do not edit; regenerated with the SDK. -->

# Template — operations

Accessor: `client.template` · Source: `dropbox_sign_api/apis/template.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.template.template_add_user

- **Route**: `POST /template/add_user/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_add_user(template_id: str, body: TemplateAddUserRequest | TemplateAddUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`, `body`
- **Params**: `template_id` — path · `body` — JSON body
- **Returns (parsed)**: `TemplateGetResponse`
- **Returns (raw)**: `ApiResult[TemplateGetResponse, TemplateAddUserErrorBody]`
- **Error**: `TemplateAddUserErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateAddUserRequest` | `dropbox_sign_api/models/template_add_user_request.py` |
| `TemplateAddUserRequestDict` | `dropbox_sign_api/models/template_add_user_request.py` |
| `TemplateGetResponse` | `dropbox_sign_api/models/template_get_response.py` |
| `TemplateAddUserErrorBody` | `dropbox_sign_api/errors/template_add_user_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_create

- **Route**: `POST /template/create`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_create(form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict], signer_roles: list[SubTemplateRole | SubTemplateRoleDict], *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_roles: list[str] | None = None, client_id: str | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_preexisting_fields: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `form_fields_per_document`, `signer_roles`
- **Params**: `form_fields_per_document` — multipart field · `signer_roles` — multipart field · `files` — multipart file · `file_urls` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_roles` — multipart field · `client_id` — multipart field · `field_options` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `merge_fields` — multipart field · `message` — multipart field · `metadata` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `use_preexisting_fields` — multipart field · `ignore_text_tags_extraction_errors` — multipart field
- **Returns (parsed)**: `TemplateCreateResponse`
- **Returns (raw)**: `ApiResult[TemplateCreateResponse, TemplateCreateErrorBody]`
- **Error**: `TemplateCreateErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubTemplateRole` | `dropbox_sign_api/models/sub_template_role.py` |
| `SubTemplateRoleDict` | `dropbox_sign_api/models/sub_template_role.py` |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubMergeField` | `dropbox_sign_api/models/sub_merge_field.py` |
| `SubMergeFieldDict` | `dropbox_sign_api/models/sub_merge_field.py` |
| `TemplateCreateResponse` | `dropbox_sign_api/models/template_create_response.py` |
| `TemplateCreateErrorBody` | `dropbox_sign_api/errors/template_create_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_create_embedded_draft

- **Route**: `POST /template/create_embedded_draft`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_create_embedded_draft(client_id: str, *, files: FileInput | None = None, file_urls: list[str] | None = None, allow_ccs: bool | None = True, allow_reassign: bool | None = False, attachments: list[SubAttachment | SubAttachmentDict] | None = None, cc_roles: list[str] | None = None, editor_options: SubEditorOptions | SubEditorOptionsDict | None = None, field_options: SubFieldOptions | SubFieldOptionsDict | None = None, force_signer_roles: bool | None = False, force_subject_message: bool | None = False, form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None, form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None, form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None, merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None, message: str | None = None, metadata: dict[str, Any] | None = None, show_preview: bool | None = False, show_progress_stepper: bool | None = True, signer_roles: list[SubTemplateRole | SubTemplateRoleDict] | None = None, skip_me_now: bool | None = False, subject: str | None = None, test_mode: bool | None = False, title: str | None = None, use_preexisting_fields: bool | None = False, ignore_text_tags_extraction_errors: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `client_id`
- **Params**: `client_id` — multipart field · `files` — multipart file · `file_urls` — multipart field · `allow_ccs` — multipart field · `allow_reassign` — multipart field · `attachments` — multipart field · `cc_roles` — multipart field · `editor_options` — multipart field · `field_options` — multipart field · `force_signer_roles` — multipart field · `force_subject_message` — multipart field · `form_field_groups` — multipart field · `form_field_rules` — multipart field · `form_fields_per_document` — multipart field · `merge_fields` — multipart field · `message` — multipart field · `metadata` — multipart field · `show_preview` — multipart field · `show_progress_stepper` — multipart field · `signer_roles` — multipart field · `skip_me_now` — multipart field · `subject` — multipart field · `test_mode` — multipart field · `title` — multipart field · `use_preexisting_fields` — multipart field · `ignore_text_tags_extraction_errors` — multipart field
- **Returns (parsed)**: `TemplateCreateEmbeddedDraftResponse`
- **Returns (raw)**: `ApiResult[TemplateCreateEmbeddedDraftResponse, TemplateCreateEmbeddedDraftErrorBody]`
- **Error**: `TemplateCreateEmbeddedDraftErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubAttachment` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubAttachmentDict` | `dropbox_sign_api/models/sub_attachment.py` |
| `SubEditorOptions` | `dropbox_sign_api/models/sub_editor_options.py` |
| `SubEditorOptionsDict` | `dropbox_sign_api/models/sub_editor_options.py` |
| `SubFieldOptions` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFieldOptionsDict` | `dropbox_sign_api/models/sub_field_options.py` |
| `SubFormFieldGroup` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldGroupDict` | `dropbox_sign_api/models/sub_form_field_group.py` |
| `SubFormFieldRule` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldRuleDict` | `dropbox_sign_api/models/sub_form_field_rule.py` |
| `SubFormFieldsPerDocumentBase` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubFormFieldsPerDocumentBaseDict` | `dropbox_sign_api/models/unions/sub_form_fields_per_document_base.py` |
| `SubMergeField` | `dropbox_sign_api/models/sub_merge_field.py` |
| `SubMergeFieldDict` | `dropbox_sign_api/models/sub_merge_field.py` |
| `SubTemplateRole` | `dropbox_sign_api/models/sub_template_role.py` |
| `SubTemplateRoleDict` | `dropbox_sign_api/models/sub_template_role.py` |
| `TemplateCreateEmbeddedDraftResponse` | `dropbox_sign_api/models/template_create_embedded_draft_response.py` |
| `TemplateCreateEmbeddedDraftErrorBody` | `dropbox_sign_api/errors/template_create_embedded_draft_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_delete

- **Route**: `POST /template/delete/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_delete(template_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`
- **Params**: `template_id` — path
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, TemplateDeleteErrorBody]`
- **Error**: `TemplateDeleteErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateDeleteErrorBody` | `dropbox_sign_api/errors/template_delete_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_files

- **Route**: `GET /template/files/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_files(template_id: str, *, file_type: FileTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`
- **Params**: `template_id` — path · `file_type` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, TemplateFilesErrorBody]`
- **Error**: `TemplateFilesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FileTypeOrStr` | `dropbox_sign_api/models/enums/file_type.py` |
| `TemplateFilesErrorBody` | `dropbox_sign_api/errors/template_files_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_files_as_data_uri

- **Route**: `GET /template/files_as_data_uri/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_files_as_data_uri(template_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`
- **Params**: `template_id` — path
- **Returns (parsed)**: `FileResponseDataUri`
- **Returns (raw)**: `ApiResult[FileResponseDataUri, TemplateFilesAsDataUriErrorBody]`
- **Error**: `TemplateFilesAsDataUriErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FileResponseDataUri` | `dropbox_sign_api/models/file_response_data_uri.py` |
| `TemplateFilesAsDataUriErrorBody` | `dropbox_sign_api/errors/template_files_as_data_uri_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_files_as_file_url

- **Route**: `GET /template/files_as_file_url/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_files_as_file_url(template_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`
- **Params**: `template_id` — path · `force_download` — query
- **Returns (parsed)**: `FileResponseModel`
- **Returns (raw)**: `ApiResult[FileResponseModel, TemplateFilesAsFileUrlErrorBody]`
- **Error**: `TemplateFilesAsFileUrlErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FileResponseModel` | `dropbox_sign_api/models/file_response_model.py` |
| `TemplateFilesAsFileUrlErrorBody` | `dropbox_sign_api/errors/template_files_as_file_url_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_get

- **Route**: `GET /template/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_get(template_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`
- **Params**: `template_id` — path
- **Returns (parsed)**: `TemplateGetResponse`
- **Returns (raw)**: `ApiResult[TemplateGetResponse, TemplateGetErrorBody]`
- **Error**: `TemplateGetErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateGetResponse` | `dropbox_sign_api/models/template_get_response.py` |
| `TemplateGetErrorBody` | `dropbox_sign_api/errors/template_get_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_list

- **Route**: `GET /template/list`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_list(*, account_id: str | None = None, page: int | None = 1, page_size: int | None = 20, query: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `account_id` — query · `page` — query · `page_size` — query · `query` — query
- **Returns (parsed)**: `TemplateListResponse`
- **Returns (raw)**: `ApiResult[TemplateListResponse, TemplateListErrorBody]`
- **Error**: `TemplateListErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateListResponse` | `dropbox_sign_api/models/template_list_response.py` |
| `TemplateListErrorBody` | `dropbox_sign_api/errors/template_list_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_remove_user

- **Route**: `POST /template/remove_user/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_remove_user(template_id: str, body: TemplateRemoveUserRequest | TemplateRemoveUserRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`, `body`
- **Params**: `template_id` — path · `body` — JSON body
- **Returns (parsed)**: `TemplateGetResponse`
- **Returns (raw)**: `ApiResult[TemplateGetResponse, TemplateRemoveUserErrorBody]`
- **Error**: `TemplateRemoveUserErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateRemoveUserRequest` | `dropbox_sign_api/models/template_remove_user_request.py` |
| `TemplateRemoveUserRequestDict` | `dropbox_sign_api/models/template_remove_user_request.py` |
| `TemplateGetResponse` | `dropbox_sign_api/models/template_get_response.py` |
| `TemplateRemoveUserErrorBody` | `dropbox_sign_api/errors/template_remove_user_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

### client.template.template_update_files

- **Route**: `POST /template/update_files/{template_id}`
- **Auth**: `api_key` OR `oauth2`
- **Signature**: `def template_update_files(template_id: str, *, client_id: str | None = None, files: FileInput | None = None, file_urls: list[str] | None = None, message: str | None = None, subject: str | None = None, test_mode: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `template_id`
- **Params**: `template_id` — path · `client_id` — multipart field · `files` — multipart file · `file_urls` — multipart field · `message` — multipart field · `subject` — multipart field · `test_mode` — multipart field
- **Returns (parsed)**: `TemplateUpdateFilesResponse`
- **Returns (raw)**: `ApiResult[TemplateUpdateFilesResponse, TemplateUpdateFilesErrorBody]`
- **Error**: `TemplateUpdateFilesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [4XX] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TemplateUpdateFilesResponse` | `dropbox_sign_api/models/template_update_files_response.py` |
| `TemplateUpdateFilesErrorBody` | `dropbox_sign_api/errors/template_update_files_error.py` |
| `ErrorResponse` | `dropbox_sign_api/models/error_response.py` |

