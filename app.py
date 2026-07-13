import cv2
from camera.webcam import Webcam


def main():

    webcam = Webcam()

    webcam.open()

    try:

        while True:

            frame = webcam.read_frame()

            if frame is None:
                break

            cv2.imshow("VisionGuard AI", frame)

            key = cv2.waitKey(1)

            if key == ord("q"):
                break

    finally:
        webcam.release()


if __name__ == "__main__":
    main()