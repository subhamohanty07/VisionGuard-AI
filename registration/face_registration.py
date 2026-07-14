from pathlib import Path

import cv2

from camera.webcam import Webcam
from detection.face_detector import FaceDetector
from config import KNOWN_FACES_DIR


class FaceRegistration:
    """
    Handles registration of a person's face by capturing
    and saving full webcam frames.
    """

    def __init__(self, person_name: str):
        self.person_name = person_name.strip()
        self.webcam = Webcam()
        self.detector = FaceDetector()

    def create_person_directory(self) -> Path:
        """
        Create the directory for the person if it doesn't exist.
        """
        person_directory = KNOWN_FACES_DIR / self.person_name
        person_directory.mkdir(parents=True, exist_ok=True)
        return person_directory

    def get_next_frame_number(self, person_directory: Path) -> int:
        """
        Returns the next frame number.

        Example:
            frame_001.jpg
            frame_002.jpg
            frame_003.jpg

        Returns:
            4
        """
        frames = list(person_directory.glob("frame_*.jpg"))
        return len(frames) + 1

    def save_frame(self, frame, person_directory: Path):
        """
        Save the full webcam frame.
        """
        frame_number = self.get_next_frame_number(person_directory)

        image_name = f"frame_{frame_number:03}.jpg"
        image_path = person_directory / image_name

        success = cv2.imwrite(str(image_path), frame)

        if success:
            print(f"✅ Saved: {image_name}")
        else:
            print("❌ Failed to save frame.")

    def start(self):
        """
        Start face registration.
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
                    print("Failed to read frame.")
                    break

                faces = self.detector.detect(frame)

                self.detector.draw_faces(frame, faces)

                cv2.imshow("Face Registration", frame)

                key = cv2.waitKey(1) & 0xFF

                if key == ord(" "):

                    if len(faces) == 1:
                        self.save_frame(frame, person_directory)

                    elif len(faces) == 0:
                        print("⚠ No face detected.")

                    else:
                        print("⚠ Multiple faces detected. Please keep only one face in front of the camera.")

                elif key == ord("q"):
                    print("\nRegistration closed.")
                    break

        finally:
            self.webcam.release()