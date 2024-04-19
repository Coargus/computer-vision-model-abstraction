"""Coargus's Detected Object Schema."""

from __future__ import annotations

import dataclasses
from typing import Any

from cog_cv_abstraction.enum.status import Status


@dataclasses.dataclass
class DetectedObject:
    """Detected Object class."""

    name: str | None
    confidence: float = 0.0
    probability: float = 0.0
    confidence_of_all_obj: list[float] | None = None
    probability_of_all_obj: list[float] | None = None
    all_obj_detected: list[Any] | None = None
    number_of_detection: int = 0
    is_detected: bool | Status = Status.UNKNOWN
    model_name: str | None = None
    bounding_box_of_all_obj: list[Any] | None = None

    def __post_init__(self) -> None:
        """Post init."""
        if self.confidence_of_all_obj and len(self.confidence_of_all_obj) > 0:
            self.confidence = max(self.confidence_of_all_obj)
        if self.probability_of_all_obj and len(self.probability_of_all_obj) > 0:
            self.probability = max(self.probability_of_all_obj)
