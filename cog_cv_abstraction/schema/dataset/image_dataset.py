"""Coargus's Detected Object Schema."""

from __future__ import annotations

import abc
import dataclasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    import torch
    from torch.utils.data import Dataset


@dataclasses.dataclass
class CoargusImageDataset(abc.ABC):
    """Coargus's Image Dataset Schema."""

    unique_labels: list
    labels: list[list[str]]
    images: list[np.ndarray] | list[torch.Tensor] | Dataset

    @abc.abstractmethod
    def get_all_images_by_label(self, target_label: str) -> list[np.ndarray]:
        """Returns all images with the specified label from a dataset.

        Args:
            target_label (str): Label to filter images by.

        Returns:
        list[np.ndarray]: Images matching the target label.
        """
        raise NotImplementedError
