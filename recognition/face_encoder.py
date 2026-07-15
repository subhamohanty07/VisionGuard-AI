import numpy as np
from insightface.app import FaceAnalysis


class FaceEncoder:
    """
    Face detection + embedding generation using InsightFace.
    """

    def __init__(self):

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"],
        )

        self.app.prepare(
            ctx_id=0,
            det_size=(640, 640),
        )

    def detect(self, image: np.ndarray):
        """
        Detect all faces in an image.

        Returns:
            list[Face]
        """
        return self.app.get(image)

    def encode(self, image: np.ndarray):
        """
        Returns the embedding when exactly one face is present.
        Used during registration/database generation.
        """

        faces = self.detect(image)

        if len(faces) != 1:
            return None

        return faces[0].embedding