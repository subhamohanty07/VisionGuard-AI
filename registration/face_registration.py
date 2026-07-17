from pathlib import Path

import cv2

from camera.webcam import Webcam
from config import APP_NAME, KNOWN_FACES_DIR
from detection.face_detector import FaceDetector


class FaceRegistration:
    """
    Registers a person's face by capturing webcam frames.
    """

    def __init__(self, person_name: str):

        self.person_name = person_name.strip()

        self.webcam = Webcam()
        self.detector = FaceDetector()

    def create_person_directory(self) -> Path:
        """
        Create the person's directory if it does not exist.
        """

        person_directory = KNOWN_FACES_DIR / self.person_name

        person_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return person_directory

    def get_next_frame_number(
        self,
        person_directory: Path,
    ) -> int:
        """
        Returns the next frame number.
        """

        frames = list(
            person_directory.glob("frame_*.jpg")
        )

        return len(frames) + 1

    def save_frame(
        self,
        frame,
        person_directory: Path,
    ):
        """
        Save the current webcam frame.
        """

        frame_number = self.get_next_frame_number(
            person_directory
        )

        image_path = (
            person_directory
            / f"frame_{frame_number:03}.jpg"
        )

        success = cv2.imwrite(
            str(image_path),
            frame,
        )

        if success:
            print(f"✅ Saved: {image_path.name}")
        else:
            print("❌ Failed to save frame.")

    def start(self):
        """
        Start the registration process.
        """

        person_directory = self.create_person_directory()

        print(f"\nRegistering: {self.person_name}")
        print("SPACE → Capture Frame")
        print("Q → Quit\n")

        self.webcam.open()

        try:

            while True:

                frame = self.webcam.read_frame()

                if frame is None:
                    print("❌ Failed to read frame.")
                    break

                faces = self.detector.detect(frame)

                self.detector.draw_faces(
                    frame,
                    faces,
                )

                cv2.imshow(
                    f"{APP_NAME} - Registration",
                    frame,
                )

                key = cv2.waitKey(1) & 0xFF

                if key == ord(" "):

                    if len(faces) == 1:

                        self.save_frame(
                            frame,
                            person_directory,
                        )

                    elif len(faces) == 0:

                        print("⚠ No face detected.")

                    else:

                        print(
                            "⚠ Multiple faces detected. "
                            "Please keep only one face "
                            "in front of the camera."
                        )

                elif key == ord("q"):

                    print("\nRegistration closed.")

                    break

        finally:

            self.webcam.release()
            cv2.destroyAllWindows()