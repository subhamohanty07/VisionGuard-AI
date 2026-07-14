from pathlib import Path

import cv2

from camera.webcam import Webcam
from detection.face_detector import FaceDetector
from config import KNOWN_FACES_DIR


class FaceRegistration:
    """
    Handles registration of a person's face by capturing
    and saving cropped face images.
    """

    def __init__(self, person_name: str):
        self.person_name = person_name.strip()
        self.webcam = Webcam()
        self.detector = FaceDetector()

    def create_person_folder(self) -> Path:
        """
        Create the folder for the person if it doesn't exist.
        """
        person_folder = KNOWN_FACES_DIR / self.person_name
        person_folder.mkdir(parents=True, exist_ok=True)
        return person_folder

    def get_next_image_number(self, person_folder: Path) -> int:
        """
        Returns the next image number based on existing images.
        Example:
            001.jpg
            002.jpg
            003.jpg
        Returns 4.
        """
        images = list(person_folder.glob("*.jpg"))
        return len(images) + 1

    def save_face(self, face, person_folder: Path):
        """
        Save the cropped face image.
        """
        image_number = self.get_next_image_number(person_folder)

        image_name = f"{image_number:03}.jpg"
        image_path = person_folder / image_name

        success = cv2.imwrite(str(image_path), face)

        if success:
            print(f"✅ Saved: {image_path}")
        else:
            print("❌ Failed to save image.")

    def start(self):
        """
        Start face registration.
        """
        person_folder = self.create_person_folder()

        print(f"\nRegistering: {self.person_name}")
        print("SPACE → Capture Face")
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
                        x, y, w, h = faces[0]

                        face = frame[y:y + h, x:x + w]

                        self.save_face(face, person_folder)

                    elif len(faces) == 0:
                        print("⚠ No face detected.")

                    else:
                        print("⚠ Multiple faces detected. Please keep only one face in front of the camera.")

                elif key == ord("q"):
                    print("\nRegistration closed.")
                    break

        finally:
            self.webcam.release()