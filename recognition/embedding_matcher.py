import numpy as np

from config import FACE_MATCH_THRESHOLD
from recognition.recognition_result import RecognitionResult


class EmbeddingMatcher:
    """
    Matches a live face embedding against the known face database.
    """

    def __init__(self, threshold=FACE_MATCH_THRESHOLD):
        self.threshold = threshold

    @staticmethod
    def cosine_similarity(embedding1, embedding2):
        """
        Compute cosine similarity between two embeddings.
        """

        embedding1 = np.asarray(embedding1)
        embedding2 = np.asarray(embedding2)

        return np.dot(embedding1, embedding2) / (
            np.linalg.norm(embedding1)
            * np.linalg.norm(embedding2)
        )

    def match(self, live_embedding, database):
        """
        Match a live embedding against the database.

        Returns:
            RecognitionResult
        """

        best_name = "Unknown"
        best_score = -1.0

        for person_name, person_data in database.items():

            for stored_embedding in person_data["embeddings"]:

                score = self.cosine_similarity(
                    live_embedding,
                    stored_embedding,
                )

                if score > best_score:
                    best_score = score
                    best_name = person_name

        is_known = best_score >= self.threshold

        return RecognitionResult(
            name=best_name if is_known else "Unknown",
            score=best_score,
            is_known=is_known,
        )