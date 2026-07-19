import cv2

from camera.webcam import Webcam

from config import (
    APP_NAME,
    RECOGNITION_INTERVAL,
)

from events.event_manager import EventManager
from recognition.embedding_matcher import EmbeddingMatcher
from recognition.face_database import FaceDatabase
from recognition.face_encoder import FaceEncoder


class FaceRecognizer:
    """
    Main face recognition pipeline.
    """

    def __init__(self):

        self.webcam = Webcam()
        self.encoder = FaceEncoder()
        self.database = FaceDatabase()
        self.matcher = EmbeddingMatcher()
        self.event_manager = EventManager()

        self.database.load()

        self.frame_counter = 0
        self.cached_results = []

    def recognize(self, frame):
        """
        Recognize all faces in the current frame.
        """

        detected_faces = self.encoder.detect(frame)

        results = []

        for face in detected_faces:

            result = self.matcher.match(
                face.embedding,
                self.database.get_all(),
            )

            result.bbox = tuple(map(int, face.bbox))

            results.append(result)

        unknown_present = any(
            not result.is_known
            for result in results
        )

        self.event_manager.handle(
            unknown_present,
            results,
            frame,
        )

        return results

    def draw_results(self, frame):
        """
        Draw recognition results on the frame.
        """

        for result in self.cached_results:

            if result.bbox is None:
                continue

            x1, y1, x2, y2 = result.bbox

            color = (
                (0, 255, 0)
                if result.is_known
                else (0, 0, 255)
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                2,
            )

            cv2.putText(
                frame,
                f"{result.name} ({result.score:.2f})",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2,
            )

    def start(self):
        """
        Start the recognition loop.
        """

        self.webcam.open()

        try:

            while True:

                frame = self.webcam.read_frame()

                if frame is None:
                    break

                self.frame_counter += 1

                if (
                    self.frame_counter
                    % RECOGNITION_INTERVAL
                    == 0
                ):
                    self.cached_results = self.recognize(frame)

                self.draw_results(frame)

                cv2.imshow(APP_NAME, frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        finally:

            self.webcam.release()
            cv2.destroyAllWindows()