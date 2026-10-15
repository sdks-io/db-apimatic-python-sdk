from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error_response_error import ErrorResponseError, ErrorResponseErrorDict
from .sub_form_field_group import SubFormFieldGroup, SubFormFieldGroupDict
from .unions.detection_mode1 import DetectionMode1, DetectionMode1Dict
from .unions.sub_form_fields_per_document_base import SubFormFieldsPerDocumentBase, SubFormFieldsPerDocumentBaseDict
from .warning_response import WarningResponse, WarningResponseDict


class DocumentFieldDetectionResponseDetectionResult(SdkBaseModel):
    document_hash: str
    """The SHA-256 hash of the analyzed document."""

    detection_mode: DetectionMode1
    """The field detection method used to analyze the document: ``annotations`` or ``text_tags``."""

    page_count: int
    """The total number of pages in the document."""

    pages_analyzed: str
    """The zero-based page indexes analyzed, represented by the requested ``page_range``, or ``all`` when every page was
    analyzed."""

    detected_at: int
    """The Unix timestamp when the field detection result was generated."""

    form_fields_per_document: list[SubFormFieldsPerDocumentBase]
    """The fields that should appear on the document, expressed as an array of objects. (For more details you can read
    about it here: `Using Form Fields per Document </docs/openapi/form-fields-per-document>`__.)

    **NOTE:** Fields like **text**, **dropdown**, **checkbox**, **radio**, and **hyperlink** have additional required
    and optional parameters. Check out the list of `additional parameters
    </api/reference/constants/#form-fields-per-document>`__ for these field types.

    * Text Field use ``SubFormFieldsPerDocumentText``
    * Dropdown Field use ``SubFormFieldsPerDocumentDropdown``
    * Hyperlink Field use ``SubFormFieldsPerDocumentHyperlink``
    * Checkbox Field use ``SubFormFieldsPerDocumentCheckbox``
    * Radio Field use ``SubFormFieldsPerDocumentRadio``
    * Signature Field use ``SubFormFieldsPerDocumentSignature``
    * Date Signed Field use ``SubFormFieldsPerDocumentDateSigned``
    * Initials Field use ``SubFormFieldsPerDocumentInitials``
    * Text Merge Field use ``SubFormFieldsPerDocumentTextMerge``
    * Checkbox Merge Field use ``SubFormFieldsPerDocumentCheckboxMerge``"""

    form_field_groups: list[SubFormFieldGroup]
    """Group information for fields defined in ``form_fields_per_document``. String-indexed JSON array with
    ``group_label`` and ``requirement`` keys. ``form_fields_per_document`` must contain fields referencing a group
    defined in ``form_field_groups``."""

    warnings: list[WarningResponse]
    """Non-fatal issues encountered during field detection."""

    errors: list[ErrorResponseError]
    """Errors encountered during field detection. Successfully detected fields may still be included in the response."""

    suggestions: list[str]
    """Suggestions for improving the field detection results."""


class DocumentFieldDetectionResponseDetectionResultDict(TypedDict):
    document_hash: str
    detection_mode: DetectionMode1Dict
    page_count: int
    pages_analyzed: str
    detected_at: int
    form_fields_per_document: list[SubFormFieldsPerDocumentBaseDict]
    form_field_groups: list[SubFormFieldGroupDict]
    warnings: list[WarningResponseDict]
    errors: list[ErrorResponseErrorDict]
    suggestions: list[str]
