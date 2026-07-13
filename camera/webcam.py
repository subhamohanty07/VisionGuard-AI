import cv2


class Webcam:
    """
    Handles all webcam operations.
    """

    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.cap = None

    def open(self):
        """Open the webcam."""
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise Exception("Could not open webcam.")

    def read_frame(self):
        """Read one frame from the webcam."""
        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def release(self):
        """Release webcam resources."""
        if self.cap:
            self.cap.release()

        cv2.destroyAllWindows()