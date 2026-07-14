import cv2
from config import HAAR_CASCADE_PATH


class FaceDetector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(str(HAAR_CASCADE_PATH))

        if self.face_cascade.empty():
            raise FileNotFoundError(
                f"Could not load Haar Cascade file: {HAAR_CASCADE_PATH}"
            )

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        return faces