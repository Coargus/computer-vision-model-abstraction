"""Coargus's Detected Object Schema."""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from cog_cv_abstraction.schema.detected_object import DetectedObject


@dataclasses.dataclass
class DetectedObjectSet:
    """Detected Object Set Class."""

    objects: list[str] = dataclasses.field(default_factory=list)
    detected_object: list[DetectedObject] = dataclasses.field(
        default_factory=list
    )
    detected_object_set: dict[str, DetectedObject] = dataclasses.field(
        default_factory=dict
    )

    def __setitem__(
        self, object_name: str, detected_obj: DetectedObject
    ) -> None:
        """Set item."""
        self.detected_object_set[object_name] = detected_obj
        self.objects.append(object_name)
        self.detected_object.append(detected_obj)

    def __getitem__(self, item: str) -> DetectedObject:
        """Get item."""
        return self.detected_object_set.get(item, None)

    def __iter__(self) -> iter[DetectedObject]:
        """Iterate through detected objects."""
        return iter(self.detected_object_set)

    def keys(self) -> list[str]:
        """Get keys."""
        return self.detected_object_set.keys()

    def values(self) -> list[DetectedObject]:
        """Get values."""
        return self.detected_object_set.values()

    def items(self) -> dict[str, DetectedObject]:
        """Get items."""
        return self.detected_object_set.items()
