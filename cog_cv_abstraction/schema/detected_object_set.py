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

    def __getitem__(self, item: str) -> DetectedObject | None:
        """Get item."""
        return self.detected_object_set.get(item)

    def __iter__(self) -> iter[DetectedObject]:
        """Iterate through detected objects."""
        return iter(self.detected_object_set)

    def get(
        self, key: str, default: str | None = None
    ) -> DetectedObject | None:
        """Get item with a default value."""
        return self.detected_object_set.get(key, default)

    def keys(self) -> list[str]:
        """Get keys."""
        return self.detected_object_set.keys()

    def values(self) -> list[DetectedObject]:
        """Get values."""
        return self.detected_object_set.values()

    def items(self) -> dict[str, DetectedObject]:
        """Get items."""
        return self.detected_object_set.items()

    def get_object_of_interest(
        self, object_of_interest: list[str]
    ) -> dict[str, DetectedObject]:
        """Get object of interest."""
        object_of_interest_output = {}
        for object_name in object_of_interest:
            if self.detected_object_set.get(object_name):
                object_of_interest_output[object_name] = (
                    self.detected_object_set[object_name]
                )
        return object_of_interest_output
