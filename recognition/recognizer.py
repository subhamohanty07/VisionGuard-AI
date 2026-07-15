import cv2

from camera.webcam import Webcam
from recognition.face_encoder import FaceEncoder
from recognition.face_database import FaceDatabase
from recognition.matcher import FaceMatcher


class FaceRecognizer:

    def __init__(self):
        self.webcam = Webcam()
        self.encoder = FaceEncoder()
        self.database = FaceDatabase()
        self.matcher = FaceMatcher()

        self.database.load()

    def start(self):

        self.webcam.open()

        try:

            while True:

                frame = self.webcam.read_frame()

                if frame is None:
                    break

                detected_faces = self.encoder.detect(frame)

                for face in detected_faces:

                    embedding = face.embedding

                    name, score = self.matcher.match(
                        embedding,
                        self.database.get_all(),
                    )

                    x1, y1, x2, y2 = map(int, face.bbox)

                    color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        color,
                        2,
                    )

                    cv2.putText(
                        frame,
                        f"{name} ({score:.2f})",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        color,
                        2,
                    )

                cv2.imshow("VisionGuard AI", frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord("q"):
                    break

        finally:
            self.webcam.release()