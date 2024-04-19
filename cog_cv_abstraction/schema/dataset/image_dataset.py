"""Coargus's Detected Object Schema."""

from __future__ import annotations

import abc
import dataclasses
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    import torch


@dataclasses.dataclass
class CoargusImageDataset(abc.ABC):
    """Coargus's Image Dataset Schema."""

    unique_labels: list
    labels: list[list[str]]
    images: list[np.ndarray] | list[torch.Tensor]
