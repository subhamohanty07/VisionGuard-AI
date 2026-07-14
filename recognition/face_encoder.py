from pathlib import Path

import cv2
import numpy as np
from insightface.app import FaceAnalysis


class FaceEncoder:
    """
    Generates face embeddings using InsightFace.
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

    def encode(self, image: np.ndarray):
        """
        Returns the embedding of a single face.

        Returns:
            numpy.ndarray | None
        """

        faces = self.app.get(image)

        if len(faces) != 1:
            return None

        return faces[0].embedding