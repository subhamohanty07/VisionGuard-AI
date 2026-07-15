from pathlib import Path

import cv2

from config import KNOWN_FACES_DIR
from recognition.face_database import FaceDatabase
from recognition.face_encoder import FaceEncoder


def main():

    encoder = FaceEncoder()
    database = FaceDatabase()

    database.load()

    for person_directory in KNOWN_FACES_DIR.iterdir():

        if not person_directory.is_dir():
            continue

        person_name = person_directory.name

        print(f"\nProcessing {person_name}...")

        for image_path in person_directory.glob("*.jpg"):

            image = cv2.imread(str(image_path))

            if image is None:
                print(f"Could not read {image_path.name}")
                continue

            embedding = encoder.encode(image)

            if embedding is None:
                print(f"No face detected : {image_path.name}")
                continue

            database.add_embedding(person_name, embedding)

            print(f"Encoded : {image_path.name}")

    database.save()

    print("\nFace database generated successfully!")


if __name__ == "__main__":
    main()