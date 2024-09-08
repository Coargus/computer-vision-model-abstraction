"""Package containing your_project name."""

from __future__ import annotations

from .enum import status
from .image import detection
from .schema import dataset, detected_object, video_frame

__all__ = ["detection", "status", "detected_object", "dataset", "video_frame"]
__version__ = "v0.0.4-dev"
