import cv2

from camera.webcam import Webcam
from recognition.face_encoder import FaceEncoder
from recognition.face_database import FaceDatabase
from recognition.embedding_matcher import EmbeddingMatcher
from events.event_manager import EventManager


class FaceRecognizer:

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

        detected_faces = self.encoder.detect(frame)

        results = []

        for face in detected_faces:

            result = self.matcher.match(
                face.embedding,
                self.database.get_all(),
            )
            self.event_manager.handle(result)

            result.bbox = tuple(map(int, face.bbox))

            results.append(result)

        return results

    def start(self):

        self.webcam.open()

        try:

            while True:

                frame = self.webcam.read_frame()

                if frame is None:
                    break

                self.frame_counter += 1

                if self.frame_counter % 5 == 0:
                    self.cached_results = self.recognize(frame)

                for result in self.cached_results:

                    x1, y1, x2, y2 = result.bbox

                    color = (0, 255, 0) if result.is_known else (0, 0, 255)

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

                cv2.imshow("VisionGuard AI", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

        finally:
            self.webcam.release()