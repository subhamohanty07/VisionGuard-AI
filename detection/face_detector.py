import cv2

from config import BOX_THICKNESS, HAAR_CASCADE_PATH


class FaceDetector:
    """
    Detects faces using OpenCV's Haar Cascade classifier.
    """

    def __init__(self):

        self.face_cascade = cv2.CascadeClassifier(
            str(HAAR_CASCADE_PATH)
        )

        if self.face_cascade.empty():
            raise FileNotFoundError(
                f"Could not load Haar Cascade file: "
                f"{HAAR_CASCADE_PATH}"
            )

    def detect(self, frame):
        """
        Detect all faces in a frame.
        """

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY,
        )

        return self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

    def draw_faces(self, frame, faces):
        """
        Draw bounding boxes around detected faces.
        """

        for (x, y, w, h) in faces:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                BOX_THICKNESS,
            )