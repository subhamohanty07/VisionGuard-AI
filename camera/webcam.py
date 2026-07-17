import cv2

from config import CAMERA_INDEX


class Webcam:
    """
    Handles webcam operations.
    """

    def __init__(self):

        self.camera_index = CAMERA_INDEX
        self.cap = None

    def open(self):
        """
        Open the webcam.
        """

        self.cap = cv2.VideoCapture(
            self.camera_index
        )

        if not self.cap.isOpened():
            raise RuntimeError(
                "Could not open webcam."
            )

    def read_frame(self):
        """
        Read one frame from the webcam.
        """

        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def release(self):
        """
        Release webcam resources.
        """

        if self.cap is not None:
            self.cap.release()

        cv2.destroyAllWindows()