import cv2

from camera.webcam import Webcam
from detection.face_detector import FaceDetector


def main():
    webcam = Webcam()
    detector = FaceDetector()

    webcam.open()

    try:
        while True:
            frame = webcam.read_frame()

            if frame is None:
                break

            # Detect faces
            faces = detector.detect(frame)

            # Draw rectangles
            for (x, y, w, h) in faces:
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2,
                )

            cv2.imshow("VisionGuard AI", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        webcam.release()


if __name__ == "__main__":
    main()