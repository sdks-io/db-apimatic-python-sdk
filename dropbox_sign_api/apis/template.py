from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncFileInput,
    AsyncRawClient,
    FileInput,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    file_part,
    json_body,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.template_add_user_error import TemplateAddUserErrorBody, template_add_user_error_mapper
from ..errors.template_create_embedded_draft_error import (
    TemplateCreateEmbeddedDraftErrorBody,
    template_create_embedded_draft_error_mapper,
)
from ..errors.template_create_error import TemplateCreateErrorBody, template_create_error_mapper
from ..errors.template_delete_error import TemplateDeleteErrorBody, template_delete_error_mapper
from ..errors.template_files_as_data_uri_error import (
    TemplateFilesAsDataUriErrorBody,
    template_files_as_data_uri_error_mapper,
)
from ..errors.template_files_as_file_url_error import (
    TemplateFilesAsFileUrlErrorBody,
    template_files_as_file_url_error_mapper,
)
from ..errors.template_files_error import TemplateFilesErrorBody, template_files_error_mapper
from ..errors.template_get_error import TemplateGetErrorBody, template_get_error_mapper
from ..errors.template_list_error import TemplateListErrorBody, template_list_error_mapper
from ..errors.template_remove_user_error import TemplateRemoveUserErrorBody, template_remove_user_error_mapper
from ..errors.template_update_files_error import TemplateUpdateFilesErrorBody, template_update_files_error_mapper
from ..models.enums.file_type import FileTypeOrStr
from ..models.file_response_data_uri import FileResponseDataUri
from ..models.file_response_model import FileResponseModel
from ..models.sub_attachment import SubAttachment, SubAttachmentDict
from ..models.sub_editor_options import SubEditorOptions, SubEditorOptionsDict
from ..models.sub_field_options import SubFieldOptions, SubFieldOptionsDict
from ..models.sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from ..models.sub_form_field_rule import SubFormFieldRule, SubFormFieldRuleDict
from ..models.sub_merge_field import SubMergeField, SubMergeFieldDict
from ..models.sub_template_role import SubTemplateRole, SubTemplateRoleDict
from ..models.template_add_user_request import TemplateAddUserRequest, TemplateAddUserRequestDict
from ..models.template_create_embedded_draft_response import TemplateCreateEmbeddedDraftResponse
from ..models.template_create_response import TemplateCreateResponse
from ..models.template_get_response import TemplateGetResponse
from ..models.template_list_response import TemplateListResponse
from ..models.template_remove_user_request import TemplateRemoveUserRequest, TemplateRemoveUserRequestDict
from ..models.template_update_files_response import TemplateUpdateFilesResponse
from ..models.unions.sub_form_fields_per_document_base import (
    SubFormFieldsPerDocumentBase,
    SubFormFieldsPerDocumentBaseDict,
)
from ..server.server import Server


class Template:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TemplateWithRawResponse(client, server, auth)

    def template_add_user(
        self,
        template_id: str,
        body: TemplateAddUserRequest | TemplateAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateGetResponse:
        """Gives the specified Account access to the specified Template. The specified Account must be a part of your
        Team.

        Args:
            template_id: The id of the Template to give the Account access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.template_add_user(template_id, body, request_options=request_options))

    def template_create(
        self,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict],
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict],
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        client_id: str | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateCreateResponse:
        """Creates a template that can be used in future signature requests.

        If ``client_id`` is provided, the template will be created as an embedded template. Embedded templates can be
        used for embedded signature requests and can be edited later by generating a new ``edit_url`` with
        `/embedded/edit_url/{template_id} </api/reference/operation/embeddedEditUrl/>`__.

        Template creation may complete asynchronously after the initial request is accepted. It is recommended that a
        callback be implemented to listen for the callback event. A ``template_created`` event indicates the template is
        ready to use, while a ``template_error`` event indicates there was a problem while creating the template. If a
        callback handler has been configured and the event has not been received within 60 minutes of making the call,
        check the status of the request in the API dashboard and retry the request if necessary.

        Args:
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.template_create(
                form_fields_per_document,
                signer_roles,
                files=files,
                file_urls=file_urls,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_roles=cc_roles,
                client_id=client_id,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                merge_fields=merge_fields,
                message=message,
                metadata=metadata,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_preexisting_fields=use_preexisting_fields,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                request_options=request_options,
            ),
        )

    def template_create_embedded_draft(
        self,
        client_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict] | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateCreateEmbeddedDraftResponse:
        """The first step in an embedded template workflow. Creates a draft template that can then be further set up in
        the template 'edit' stage.

        Args:
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when creating a template.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.template_create_embedded_draft(
                client_id,
                files=files,
                file_urls=file_urls,
                allow_ccs=allow_ccs,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_roles=cc_roles,
                editor_options=editor_options,
                field_options=field_options,
                force_signer_roles=force_signer_roles,
                force_subject_message=force_subject_message,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                merge_fields=merge_fields,
                message=message,
                metadata=metadata,
                show_preview=show_preview,
                show_progress_stepper=show_progress_stepper,
                signer_roles=signer_roles,
                skip_me_now=skip_me_now,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_preexisting_fields=use_preexisting_fields,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                request_options=request_options,
            ),
        )

    def template_delete(self, template_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Completely deletes the template specified from the account.

        Args:
            template_id: The id of the Template to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.template_delete(template_id, request_options=request_options))

    def template_files(
        self,
        template_id: str,
        *,
        file_type: FileTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a PDF or ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.template_files(template_id, file_type=file_type, request_options=request_options)
        )

    def template_files_as_data_uri(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponseDataUri:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.template_files_as_data_uri(template_id, request_options=request_options))

    def template_files_as_file_url(
        self, template_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponseModel:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.template_files_as_file_url(
                template_id, force_download=force_download, request_options=request_options
            ),
        )

    def template_get(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TemplateGetResponse:
        """Returns the Template specified by the ``template_id`` parameter.

        Args:
            template_id: The id of the Template to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.template_get(template_id, request_options=request_options))

    def template_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateListResponse:
        """Returns a list of the Templates that are accessible by you.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying templates.

        Args:
            account_id: Which account to return Templates for. Must be a team member. Use ``all`` to indicate all team
                members. Defaults to your account.
            page: Which page number of the Template List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the Template objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.template_list(
                account_id=account_id, page=page, page_size=page_size, query=query, request_options=request_options
            ),
        )

    def template_remove_user(
        self,
        template_id: str,
        body: TemplateRemoveUserRequest | TemplateRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateGetResponse:
        """Removes the specified Account's access to the specified Template.

        Args:
            template_id: The id of the Template to remove the Account's access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(self._with_raw_response.template_remove_user(template_id, body, request_options=request_options))

    def template_update_files(
        self,
        template_id: str,
        *,
        client_id: str | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateUpdateFilesResponse:
        """Overlays a new file with the overlay of an existing template. The new file(s) must:

        1. have the same or higher page count
        2. the same orientation as the file(s) being replaced.

        This will not overwrite or in any way affect the existing template. Both the existing template and new template
        will be available for use after executing this endpoint. Also note that this will decrement your template quota.

        Overlaying new files is asynchronous and a successful call to this endpoint will return 200 OK response if the
        request passes initial validation checks.

        It is recommended that a callback be implemented to listen for the callback event. A ``template_created`` event
        will be sent when the files are updated or a ``template_error`` event will be sent if there was a problem while
        updating the files. If a callback handler has been configured and the event has not been received within 60
        minutes of making the call, check the status of the request in the API dashboard and retry the request if
        necessary.

        If the page orientation or page count is different from the original template document, we will notify you with
        a ``template_error`` `callback event <https://app.hellosign.com/api/eventsAndCallbacksWalkthrough>`__.

        Args:
            template_id: The ID of the template whose files to update.
            client_id: Client id of the app you're using to update this template.
            files: Use ``files[]`` to indicate the uploaded file(s) to use for the template. This endpoint requires
                either **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to use for the template. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The new default template email message.
            subject: The new default template email subject.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            self._with_raw_response.template_update_files(
                template_id,
                client_id=client_id,
                files=files,
                file_urls=file_urls,
                message=message,
                subject=subject,
                test_mode=test_mode,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> TemplateWithRawResponse:
        return self._with_raw_response


class AsyncTemplate:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTemplateWithRawResponse(client, server, auth)

    async def template_add_user(
        self,
        template_id: str,
        body: TemplateAddUserRequest | TemplateAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateGetResponse:
        """Gives the specified Account access to the specified Template. The specified Account must be a part of your
        Team.

        Args:
            template_id: The id of the Template to give the Account access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_add_user(template_id, body, request_options=request_options)
        )

    async def template_create(
        self,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict],
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict],
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        client_id: str | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateCreateResponse:
        """Creates a template that can be used in future signature requests.

        If ``client_id`` is provided, the template will be created as an embedded template. Embedded templates can be
        used for embedded signature requests and can be edited later by generating a new ``edit_url`` with
        `/embedded/edit_url/{template_id} </api/reference/operation/embeddedEditUrl/>`__.

        Template creation may complete asynchronously after the initial request is accepted. It is recommended that a
        callback be implemented to listen for the callback event. A ``template_created`` event indicates the template is
        ready to use, while a ``template_error`` event indicates there was a problem while creating the template. If a
        callback handler has been configured and the event has not been received within 60 minutes of making the call,
        check the status of the request in the API dashboard and retry the request if necessary.

        Args:
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_create(
                form_fields_per_document,
                signer_roles,
                files=files,
                file_urls=file_urls,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_roles=cc_roles,
                client_id=client_id,
                field_options=field_options,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                merge_fields=merge_fields,
                message=message,
                metadata=metadata,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_preexisting_fields=use_preexisting_fields,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                request_options=request_options,
            ),
        )

    async def template_create_embedded_draft(
        self,
        client_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict] | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateCreateEmbeddedDraftResponse:
        """The first step in an embedded template workflow. Creates a draft template that can then be further set up in
        the template 'edit' stage.

        Args:
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when creating a template.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_create_embedded_draft(
                client_id,
                files=files,
                file_urls=file_urls,
                allow_ccs=allow_ccs,
                allow_reassign=allow_reassign,
                attachments=attachments,
                cc_roles=cc_roles,
                editor_options=editor_options,
                field_options=field_options,
                force_signer_roles=force_signer_roles,
                force_subject_message=force_subject_message,
                form_field_groups=form_field_groups,
                form_field_rules=form_field_rules,
                form_fields_per_document=form_fields_per_document,
                merge_fields=merge_fields,
                message=message,
                metadata=metadata,
                show_preview=show_preview,
                show_progress_stepper=show_progress_stepper,
                signer_roles=signer_roles,
                skip_me_now=skip_me_now,
                subject=subject,
                test_mode=test_mode,
                title=title,
                use_preexisting_fields=use_preexisting_fields,
                ignore_text_tags_extraction_errors=ignore_text_tags_extraction_errors,
                request_options=request_options,
            ),
        )

    async def template_delete(self, template_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Completely deletes the template specified from the account.

        Args:
            template_id: The id of the Template to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.template_delete(template_id, request_options=request_options))

    async def template_files(
        self,
        template_id: str,
        *,
        file_type: FileTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a PDF or ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_files(
                template_id, file_type=file_type, request_options=request_options
            ),
        )

    async def template_files_as_data_uri(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponseDataUri:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_files_as_data_uri(template_id, request_options=request_options)
        )

    async def template_files_as_file_url(
        self, template_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponseModel:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_files_as_file_url(
                template_id, force_download=force_download, request_options=request_options
            ),
        )

    async def template_get(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TemplateGetResponse:
        """Returns the Template specified by the ``template_id`` parameter.

        Args:
            template_id: The id of the Template to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(await self._with_raw_response.template_get(template_id, request_options=request_options))

    async def template_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateListResponse:
        """Returns a list of the Templates that are accessible by you.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying templates.

        Args:
            account_id: Which account to return Templates for. Must be a team member. Use ``all`` to indicate all team
                members. Defaults to your account.
            page: Which page number of the Template List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the Template objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_list(
                account_id=account_id, page=page, page_size=page_size, query=query, request_options=request_options
            ),
        )

    async def template_remove_user(
        self,
        template_id: str,
        body: TemplateRemoveUserRequest | TemplateRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateGetResponse:
        """Removes the specified Account's access to the specified Template.

        Args:
            template_id: The id of the Template to remove the Account's access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_remove_user(template_id, body, request_options=request_options)
        )

    async def template_update_files(
        self,
        template_id: str,
        *,
        client_id: str | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TemplateUpdateFilesResponse:
        """Overlays a new file with the overlay of an existing template. The new file(s) must:

        1. have the same or higher page count
        2. the same orientation as the file(s) being replaced.

        This will not overwrite or in any way affect the existing template. Both the existing template and new template
        will be available for use after executing this endpoint. Also note that this will decrement your template quota.

        Overlaying new files is asynchronous and a successful call to this endpoint will return 200 OK response if the
        request passes initial validation checks.

        It is recommended that a callback be implemented to listen for the callback event. A ``template_created`` event
        will be sent when the files are updated or a ``template_error`` event will be sent if there was a problem while
        updating the files. If a callback handler has been configured and the event has not been received within 60
        minutes of making the call, check the status of the request in the API dashboard and retry the request if
        necessary.

        If the page orientation or page count is different from the original template document, we will notify you with
        a ``template_error`` `callback event <https://app.hellosign.com/api/eventsAndCallbacksWalkthrough>`__.

        Args:
            template_id: The ID of the template whose files to update.
            client_id: Client id of the app you're using to update this template.
            files: Use ``files[]`` to indicate the uploaded file(s) to use for the template. This endpoint requires
                either **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to use for the template. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The new default template email message.
            subject: The new default template email subject.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            successful operation

        Raises:
            ApiError: failed_operation ``error`` is ``ErrorResponse | RawError``."""
        return unwrap(
            await self._with_raw_response.template_update_files(
                template_id,
                client_id=client_id,
                files=files,
                file_urls=file_urls,
                message=message,
                subject=subject,
                test_mode=test_mode,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTemplateWithRawResponse:
        return self._with_raw_response


class TemplateWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def template_add_user(
        self,
        template_id: str,
        body: TemplateAddUserRequest | TemplateAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateGetResponse, TemplateAddUserErrorBody]:
        """Gives the specified Account access to the specified Template. The specified Account must be a part of your
        Team.

        Args:
            template_id: The id of the Template to give the Account access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/add_user/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TemplateAddUserRequest | TemplateAddUserRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateGetResponse],
            error_mapper=template_add_user_error_mapper,
            request_options=request_options,
        )

    def template_create(
        self,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict],
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict],
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        client_id: str | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateCreateResponse, TemplateCreateErrorBody]:
        """Creates a template that can be used in future signature requests.

        If ``client_id`` is provided, the template will be created as an embedded template. Embedded templates can be
        used for embedded signature requests and can be edited later by generating a new ``edit_url`` with
        `/embedded/edit_url/{template_id} </api/reference/operation/embeddedEditUrl/>`__.

        Template creation may complete asynchronously after the initial request is accepted. It is recommended that a
        callback be implemented to listen for the callback event. A ``template_created`` event indicates the template is
        ready to use, while a ``template_error`` event indicates there was a problem while creating the template. If a
        callback handler has been configured and the event has not been received within 60 minutes of making the call,
        check the status of the request in the API dashboard and retry the request if necessary.

        Args:
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict]](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[list[SubTemplateRole | SubTemplateRoleDict]]("signer_roles", signer_roles),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[str] | None]("cc_roles", cc_roles),
                param[str | None]("client_id", client_id),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubMergeField | SubMergeFieldDict] | None]("merge_fields", merge_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateCreateResponse],
            error_mapper=template_create_error_mapper,
            request_options=request_options,
        )

    def template_create_embedded_draft(
        self,
        client_id: str,
        *,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict] | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateCreateEmbeddedDraftResponse, TemplateCreateEmbeddedDraftErrorBody]:
        """The first step in an embedded template workflow. Creates a draft template that can then be further set up in
        the template 'edit' stage.

        Args:
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when creating a template.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/create_embedded_draft"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_ccs", allow_ccs),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[str] | None]("cc_roles", cc_roles),
                param[SubEditorOptions | SubEditorOptionsDict | None]("editor_options", editor_options),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[bool | None]("force_signer_roles", force_signer_roles),
                param[bool | None]("force_subject_message", force_subject_message),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[list[SubMergeField | SubMergeFieldDict] | None]("merge_fields", merge_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[bool | None]("show_preview", show_preview),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubTemplateRole | SubTemplateRoleDict] | None]("signer_roles", signer_roles),
                param[bool | None]("skip_me_now", skip_me_now),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateCreateEmbeddedDraftResponse],
            error_mapper=template_create_embedded_draft_error_mapper,
            request_options=request_options,
        )

    def template_delete(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, TemplateDeleteErrorBody]:
        """Completely deletes the template specified from the account.

        Args:
            template_id: The id of the Template to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/delete/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[Any],
            error_mapper=template_delete_error_mapper,
            request_options=request_options,
        )

    def template_files(
        self,
        template_id: str,
        *,
        file_type: FileTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, TemplateFilesErrorBody]:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a PDF or ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/files/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            query_params=[param[FileTypeOrStr | None]("file_type", file_type)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=empty_response,
            error_mapper=template_files_error_mapper,
            request_options=request_options,
        )

    def template_files_as_data_uri(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponseDataUri, TemplateFilesAsDataUriErrorBody]:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/files_as_data_uri/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[FileResponseDataUri],
            error_mapper=template_files_as_data_uri_error_mapper,
            request_options=request_options,
        )

    def template_files_as_file_url(
        self, template_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponseModel, TemplateFilesAsFileUrlErrorBody]:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/files_as_file_url/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            query_params=[param[int | None]("force_download", force_download)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[FileResponseModel],
            error_mapper=template_files_as_file_url_error_mapper,
            request_options=request_options,
        )

    def template_get(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TemplateGetResponse, TemplateGetErrorBody]:
        """Returns the Template specified by the ``template_id`` parameter.

        Args:
            template_id: The id of the Template to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateGetResponse],
            error_mapper=template_get_error_mapper,
            request_options=request_options,
        )

    def template_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateListResponse, TemplateListErrorBody]:
        """Returns a list of the Templates that are accessible by you.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying templates.

        Args:
            account_id: Which account to return Templates for. Must be a team member. Use ``all`` to indicate all team
                members. Defaults to your account.
            page: Which page number of the Template List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the Template objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/list"),
            query_params=[
                param[str | None]("account_id", account_id),
                param[int | None]("page", page),
                param[int | None]("page_size", page_size),
                param[str | None]("query", query),
            ],
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateListResponse],
            error_mapper=template_list_error_mapper,
            request_options=request_options,
        )

    def template_remove_user(
        self,
        template_id: str,
        body: TemplateRemoveUserRequest | TemplateRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateGetResponse, TemplateRemoveUserErrorBody]:
        """Removes the specified Account's access to the specified Template.

        Args:
            template_id: The id of the Template to remove the Account's access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/remove_user/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TemplateRemoveUserRequest | TemplateRemoveUserRequestDict](body),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateGetResponse],
            error_mapper=template_remove_user_error_mapper,
            request_options=request_options,
        )

    def template_update_files(
        self,
        template_id: str,
        *,
        client_id: str | None = None,
        files: FileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateUpdateFilesResponse, TemplateUpdateFilesErrorBody]:
        """Overlays a new file with the overlay of an existing template. The new file(s) must:

        1. have the same or higher page count
        2. the same orientation as the file(s) being replaced.

        This will not overwrite or in any way affect the existing template. Both the existing template and new template
        will be available for use after executing this endpoint. Also note that this will decrement your template quota.

        Overlaying new files is asynchronous and a successful call to this endpoint will return 200 OK response if the
        request passes initial validation checks.

        It is recommended that a callback be implemented to listen for the callback event. A ``template_created`` event
        will be sent when the files are updated or a ``template_error`` event will be sent if there was a problem while
        updating the files. If a callback handler has been configured and the event has not been received within 60
        minutes of making the call, check the status of the request in the API dashboard and retry the request if
        necessary.

        If the page orientation or page count is different from the original template document, we will notify you with
        a ``template_error`` `callback event <https://app.hellosign.com/api/eventsAndCallbacksWalkthrough>`__.

        Args:
            template_id: The ID of the template whose files to update.
            client_id: Client id of the app you're using to update this template.
            files: Use ``files[]`` to indicate the uploaded file(s) to use for the template. This endpoint requires
                either **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to use for the template. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The new default template email message.
            subject: The new default template email subject.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/update_files/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str | None]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[str | None]("message", message),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
            ),
            auth_scheme=AnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=json_decoder[TemplateUpdateFilesResponse],
            error_mapper=template_update_files_error_mapper,
            request_options=request_options,
        )


class AsyncTemplateWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def template_add_user(
        self,
        template_id: str,
        body: TemplateAddUserRequest | TemplateAddUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateGetResponse, TemplateAddUserErrorBody]:
        """Gives the specified Account access to the specified Template. The specified Account must be a part of your
        Team.

        Args:
            template_id: The id of the Template to give the Account access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/add_user/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TemplateAddUserRequest | TemplateAddUserRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateGetResponse],
            error_mapper=template_add_user_error_mapper,
            request_options=request_options,
        )

    async def template_create(
        self,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict],
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict],
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        client_id: str | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateCreateResponse, TemplateCreateErrorBody]:
        """Creates a template that can be used in future signature requests.

        If ``client_id`` is provided, the template will be created as an embedded template. Embedded templates can be
        used for embedded signature requests and can be edited later by generating a new ``edit_url`` with
        `/embedded/edit_url/{template_id} </api/reference/operation/embeddedEditUrl/>`__.

        Template creation may complete asynchronously after the initial request is accepted. It is recommended that a
        callback be implemented to listen for the callback event. A ``template_created`` event indicates the template is
        ready to use, while a ``template_error`` event indicates there was a problem while creating the template. If a
        callback handler has been configured and the event has not been received within 60 minutes of making the call,
        check the status of the request in the API dashboard and retry the request if necessary.

        Args:
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            field_options: This allows the requester to specify field options for a signature request.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict]](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[list[SubTemplateRole | SubTemplateRoleDict]]("signer_roles", signer_roles),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[str] | None]("cc_roles", cc_roles),
                param[str | None]("client_id", client_id),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubMergeField | SubMergeFieldDict] | None]("merge_fields", merge_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateCreateResponse],
            error_mapper=template_create_error_mapper,
            request_options=request_options,
        )

    async def template_create_embedded_draft(
        self,
        client_id: str,
        *,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        allow_ccs: bool | None = True,
        allow_reassign: bool | None = False,
        attachments: list[SubAttachment | SubAttachmentDict] | None = None,
        cc_roles: list[str] | None = None,
        editor_options: SubEditorOptions | SubEditorOptionsDict | None = None,
        field_options: SubFieldOptions | SubFieldOptionsDict | None = None,
        force_signer_roles: bool | None = False,
        force_subject_message: bool | None = False,
        form_field_groups: list[SubFormFieldGroup | SubFormFieldGroupDict] | None = None,
        form_field_rules: list[SubFormFieldRule | SubFormFieldRuleDict] | None = None,
        form_fields_per_document: list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None = None,
        merge_fields: list[SubMergeField | SubMergeFieldDict] | None = None,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
        show_preview: bool | None = False,
        show_progress_stepper: bool | None = True,
        signer_roles: list[SubTemplateRole | SubTemplateRoleDict] | None = None,
        skip_me_now: bool | None = False,
        subject: str | None = None,
        test_mode: bool | None = False,
        title: str | None = None,
        use_preexisting_fields: bool | None = False,
        ignore_text_tags_extraction_errors: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateCreateEmbeddedDraftResponse, TemplateCreateEmbeddedDraftErrorBody]:
        """The first step in an embedded template workflow. Creates a draft template that can then be further set up in
        the template 'edit' stage.

        Args:
            client_id: Client id of the app you're using to create this draft. Used to apply the branding and callback
                url defined for the app.
            files: Use ``files[]`` to indicate the uploaded file(s) to send for signature. This endpoint requires either
                **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to send for signature. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            allow_ccs: This allows the requester to specify whether the user is allowed to provide email addresses to CC
                when creating a template.
            allow_reassign: Allows signers to reassign their signature requests to other signers if set to ``true``.
                Defaults to ``false``. **NOTE:** Only available for Premium plan and higher.
            attachments: A list describing the attachments
            cc_roles: The CC roles that must be assigned when using the template to send a signature request
            editor_options: This allows the requester to specify editor options when a preparing a document
            field_options: This allows the requester to specify field options for a signature request.
            force_signer_roles: Provide users the ability to review/edit the template signer roles.
            force_subject_message: Provide users the ability to review/edit the template subject and message.
            form_field_groups: Group information for fields defined in ``form_fields_per_document``. String-indexed JSON
                array with ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields
                referencing a group defined in ``form_field_groups``.
            form_field_rules: Conditional Logic rules for fields defined in ``form_fields_per_document``.
            form_fields_per_document: The fields that should appear on the document, expressed as an array of objects.
                (For more details you can read about it here: `Using Form Fields per Document
                </docs/openapi/form-fields-per-document>`__.) **NOTE:** Fields like **text**, **dropdown**,
                **checkbox**, **radio**, and **hyperlink** have additional required and optional parameters. Check out
                the list of `additional parameters </api/reference/constants/#form-fields-per-document>`__ for these
                field types. * Text Field use ``SubFormFieldsPerDocumentText`` * Dropdown Field use
                ``SubFormFieldsPerDocumentDropdown`` * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink`` *
                Checkbox Field use ``SubFormFieldsPerDocumentCheckbox`` * Radio Field use
                ``SubFormFieldsPerDocumentRadio`` * Signature Field use ``SubFormFieldsPerDocumentSignature`` * Date
                Signed Field use ``SubFormFieldsPerDocumentDateSigned`` * Initials Field use
                ``SubFormFieldsPerDocumentInitials`` * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge`` *
                Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``
            merge_fields: Add merge fields to the template. Merge fields are placed by the user creating the template
                and used to pre-fill data by passing values into signature requests with the ``custom_fields``
                parameter. If the signature request using that template *does not* pass a value into a merge field, then
                an empty field remains in the document.
            message: The default template email message.
            metadata: Key-value data that should be attached to the signature request. This metadata is included in all
                API responses and events involving the signature request. For example, use the metadata field to store a
                signer's order number for look up when receiving events for the signature request. Each request can
                include up to 10 metadata keys (or 50 nested metadata keys), with key names up to 40 characters long and
                values up to 1000 characters long.
            show_preview: This allows the requester to enable the editor/preview experience. - ``show_preview=true``:
                Allows requesters to enable the editor/preview experience. - ``show_preview=false``: Allows requesters
                to disable the editor/preview experience.
            show_progress_stepper: When only one step remains in the signature request process and this parameter is set
                to ``false`` then the progress stepper will be hidden.
            signer_roles: An array of the designated signer roles that must be specified when sending a SignatureRequest
                using this Template.
            skip_me_now: Disables the "Me (Now)" option for the person preparing the document. Does not work with type
                ``send_document``. Defaults to ``false``.
            subject: The template title (alias).
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            title: The title you want to assign to the SignatureRequest.
            use_preexisting_fields: Enable the detection of predefined PDF fields by setting the
                ``use_preexisting_fields`` to ``true`` (defaults to disabled, or ``false``).
            ignore_text_tags_extraction_errors: Sent with a value of ``true`` to ignore the validation errors from text
                tags extraction. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/create_embedded_draft"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[bool | None]("allow_ccs", allow_ccs),
                param[bool | None]("allow_reassign", allow_reassign),
                param[list[SubAttachment | SubAttachmentDict] | None]("attachments", attachments),
                param[list[str] | None]("cc_roles", cc_roles),
                param[SubEditorOptions | SubEditorOptionsDict | None]("editor_options", editor_options),
                param[SubFieldOptions | SubFieldOptionsDict | None]("field_options", field_options),
                param[bool | None]("force_signer_roles", force_signer_roles),
                param[bool | None]("force_subject_message", force_subject_message),
                param[list[SubFormFieldGroup | SubFormFieldGroupDict] | None]("form_field_groups", form_field_groups),
                param[list[SubFormFieldRule | SubFormFieldRuleDict] | None]("form_field_rules", form_field_rules),
                param[list[SubFormFieldsPerDocumentBase | SubFormFieldsPerDocumentBaseDict] | None](
                    "form_fields_per_document", form_fields_per_document
                ),
                param[list[SubMergeField | SubMergeFieldDict] | None]("merge_fields", merge_fields),
                param[str | None]("message", message),
                param[dict[str, Any] | None]("metadata", metadata),
                param[bool | None]("show_preview", show_preview),
                param[bool | None]("show_progress_stepper", show_progress_stepper),
                param[list[SubTemplateRole | SubTemplateRoleDict] | None]("signer_roles", signer_roles),
                param[bool | None]("skip_me_now", skip_me_now),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
                param[str | None]("title", title),
                param[bool | None]("use_preexisting_fields", use_preexisting_fields),
                param[bool | None]("ignore_text_tags_extraction_errors", ignore_text_tags_extraction_errors),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateCreateEmbeddedDraftResponse],
            error_mapper=template_create_embedded_draft_error_mapper,
            request_options=request_options,
        )

    async def template_delete(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, TemplateDeleteErrorBody]:
        """Completely deletes the template specified from the account.

        Args:
            template_id: The id of the Template to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/delete/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[Any],
            error_mapper=template_delete_error_mapper,
            request_options=request_options,
        )

    async def template_files(
        self,
        template_id: str,
        *,
        file_type: FileTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, TemplateFilesErrorBody]:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a PDF or ZIP file.

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            file_type: Set to ``pdf`` for a single merged document or ``zip`` for a collection of individual documents.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/files/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            query_params=[param[FileTypeOrStr | None]("file_type", file_type)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_empty_response,
            error_mapper=template_files_error_mapper,
            request_options=request_options,
        )

    async def template_files_as_data_uri(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponseDataUri, TemplateFilesAsDataUriErrorBody]:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a ``data_uri`` representing the base64 encoded file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/files_as_data_uri/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[FileResponseDataUri],
            error_mapper=template_files_as_data_uri_error_mapper,
            request_options=request_options,
        )

    async def template_files_as_file_url(
        self, template_id: str, *, force_download: int | None = 1, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponseModel, TemplateFilesAsFileUrlErrorBody]:
        """Obtain a copy of the current documents specified by the ``template_id`` parameter. Returns a JSON object with
        a url to the file (PDFs only).

        If the files are currently being prepared, a status code of ``409`` will be returned instead. In this case
        please wait for the ``template_created`` callback event.

        Args:
            template_id: The id of the template files to retrieve.
            force_download: By default when opening the ``file_url`` a browser will download the PDF and save it
                locally. When set to ``0`` the PDF file will be displayed in the browser.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/files_as_file_url/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            query_params=[param[int | None]("force_download", force_download)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[FileResponseModel],
            error_mapper=template_files_as_file_url_error_mapper,
            request_options=request_options,
        )

    async def template_get(
        self, template_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TemplateGetResponse, TemplateGetErrorBody]:
        """Returns the Template specified by the ``template_id`` parameter.

        Args:
            template_id: The id of the Template to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateGetResponse],
            error_mapper=template_get_error_mapper,
            request_options=request_options,
        )

    async def template_list(
        self,
        *,
        account_id: str | None = None,
        page: int | None = 1,
        page_size: int | None = 20,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateListResponse, TemplateListErrorBody]:
        """Returns a list of the Templates that are accessible by you.

        Take a look at our `search guide </api/reference/search/>`__ to learn more about querying templates.

        Args:
            account_id: Which account to return Templates for. Must be a team member. Use ``all`` to indicate all team
                members. Defaults to your account.
            page: Which page number of the Template List to return. Defaults to ``1``.
            page_size: Number of objects to be returned per page. Must be between ``1`` and ``100``. Default is ``20``.
            query: String that includes search terms and/or fields to be used to filter the Template objects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/template/list"),
            query_params=[
                param[str | None]("account_id", account_id),
                param[int | None]("page", page),
                param[int | None]("page_size", page_size),
                param[str | None]("query", query),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateListResponse],
            error_mapper=template_list_error_mapper,
            request_options=request_options,
        )

    async def template_remove_user(
        self,
        template_id: str,
        body: TemplateRemoveUserRequest | TemplateRemoveUserRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateGetResponse, TemplateRemoveUserErrorBody]:
        """Removes the specified Account's access to the specified Template.

        Args:
            template_id: The id of the Template to remove the Account's access to.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/remove_user/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TemplateRemoveUserRequest | TemplateRemoveUserRequestDict](body),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateGetResponse],
            error_mapper=template_remove_user_error_mapper,
            request_options=request_options,
        )

    async def template_update_files(
        self,
        template_id: str,
        *,
        client_id: str | None = None,
        files: AsyncFileInput | None = None,
        file_urls: list[str] | None = None,
        message: str | None = None,
        subject: str | None = None,
        test_mode: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TemplateUpdateFilesResponse, TemplateUpdateFilesErrorBody]:
        """Overlays a new file with the overlay of an existing template. The new file(s) must:

        1. have the same or higher page count
        2. the same orientation as the file(s) being replaced.

        This will not overwrite or in any way affect the existing template. Both the existing template and new template
        will be available for use after executing this endpoint. Also note that this will decrement your template quota.

        Overlaying new files is asynchronous and a successful call to this endpoint will return 200 OK response if the
        request passes initial validation checks.

        It is recommended that a callback be implemented to listen for the callback event. A ``template_created`` event
        will be sent when the files are updated or a ``template_error`` event will be sent if there was a problem while
        updating the files. If a callback handler has been configured and the event has not been received within 60
        minutes of making the call, check the status of the request in the API dashboard and retry the request if
        necessary.

        If the page orientation or page count is different from the original template document, we will notify you with
        a ``template_error`` `callback event <https://app.hellosign.com/api/eventsAndCallbacksWalkthrough>`__.

        Args:
            template_id: The ID of the template whose files to update.
            client_id: Client id of the app you're using to update this template.
            files: Use ``files[]`` to indicate the uploaded file(s) to use for the template. This endpoint requires
                either **files** or **file_urls[]**, but not both.
            file_urls: Use ``file_urls[]`` to have Dropbox Sign download the file(s) to use for the template. This
                endpoint requires either **files** or **file_urls[]**, but not both.
            message: The new default template email message.
            subject: The new default template email subject.
            test_mode: Whether this is a test, the signature request created from this draft will not be legally binding
                if set to ``true``. Defaults to ``false``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/template/update_files/{template_id}"),
            path_params=[param[str]("template_id", template_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(
                param[str | None]("client_id", client_id),
                file_part("files", files) if files is not None else None,
                param[list[str] | None]("file_urls", file_urls),
                param[str | None]("message", message),
                param[str | None]("subject", subject),
                param[bool | None]("test_mode", test_mode),
            ),
            auth_scheme=AsyncAnySchemes(self._auth.api_key, self._auth.oauth2),
            decoder=async_json_decoder[TemplateUpdateFilesResponse],
            error_mapper=template_update_files_error_mapper,
            request_options=request_options,
        )
