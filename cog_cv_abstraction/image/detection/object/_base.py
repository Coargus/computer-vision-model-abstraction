from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class ObjectDetectionModelBase(abc.ABC):
    """Abstract base class for object detection models in computer vision.

    This class establishes a standard API for object detection models, ensuring
    that all derived classes implement necessary methods for detection operations.
    """  # noqa: E501

    @abc.abstractmethod
    def detect(
        self,
        image: np.ndarray,
        object_classes: list[str],
    ) -> any:
        """Perform object detection using the model.

        Subclasses must implement this method to identify and locate objects in
        images, leveraging the model's training on specific object classes. The
        method should interpret and analyze the provided image data to determine
        the presence and location of specified object classes.

        Returns:
            The detection results, which could be in various formats such as
            bounding boxes, class labels, or confidence scores, depending on the
            implementation.
        """
