from __future__ import annotations

from typing import TypeAlias

DetectionMode: TypeAlias = str | str
"""The field detection method to use. Set to ``annotations`` to detect PDF form annotations or ``text_tags`` to detect
Dropbox Sign text tags."""

DetectionModeDict: TypeAlias = str | str
