import numpy as np

from recognition.recognition_result import RecognitionResult


class EmbeddingMatcher:

    def __init__(self, threshold=0.6):
        self.threshold = threshold

    def cosine_similarity(self, embedding1, embedding2):

        embedding1 = np.asarray(embedding1)
        embedding2 = np.asarray(embedding2)

        return np.dot(embedding1, embedding2) / (
            np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
        )

    def match(self, live_embedding, database):

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