"""Package containing your_project name."""

from __future__ import annotations

from .enum import status
from .image import detection
from .schema import detected_object

__all__ = ["detection", "status", "detected_object"]
__version__ = "0.0.1"
