"""Video Diffusion Model Abstraction (API)."""

from __future__ import annotations

import abc

from cv_api.video.generative import GenerativeComputerVisionModelBase


class VideoDiffusionModelBase(GenerativeComputerVisionModelBase):
    """Abstract base for video diffusion models in generative computer vision.

    This class serves as an interface for video diffusion models,
    specialized in generating or manipulating video content.
    Subclasses should implement methods for generating video frames
    using diffusion processes.

    Attributes:
        Inherits all attributes from GenerativeComputerVisionModelBase.

    Methods:
        generate_frames(**kargs): Abstract method for frame generation.
    """

    @abc.abstractmethod
    def generate_frames(self, **kargs) -> any:  # noqa: ANN003
        """Generates video frames using diffusion model logic.

        To be implemented in subclasses, this method defines how to generate
        frames via data processing, diffusion, and denoising steps.

        Parameters:
            **kargs (dict): Keyword arguments for generation,
            including frame count, resolution, and settings.

        Returns:
            any: Outputs may vary based on the implementation.

        Raises:
            NotImplementedError: If not implemented in a subclass.
        """
