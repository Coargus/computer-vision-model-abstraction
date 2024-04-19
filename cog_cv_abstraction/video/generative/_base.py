from __future__ import annotations

import abc


class GenerativeComputerVisionModelBase(abc.ABC):
    """Abstract base class for generative computer vision models.

    This class defines the basic API for a video generative model, ensuring that
    any subclass implements the essential operational methods.
    """

    @abc.abstractmethod
    def generate(self) -> any:
        """Generate output using the model's generative capabilities.

        This abstract method should be implemented by subclasses to produce
        outputs such as video sequences or images using generative techniques,
        based on the model's trained parameters and
        potentially provided input data.

        Returns:
            The generative output, which could be in various formats such as a
            numpy array, a PIL image, or a video file depending on
            the implementation.

        Raises:
            NotImplementedError: If not implemented in a subclass.
        """
