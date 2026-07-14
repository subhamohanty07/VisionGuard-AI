from pathlib import Path

import cv2

from recognition.face_encoder import FaceEncoder


def main():

    image_path = Path(r"C:\Users\Subham Mohanty\OneDrive\Pictures\Gemini_Generated_Image_jczrrqjczrrqjczr.png")

    image = cv2.imread(str(image_path))

    if image is None:
        print("Image not found!")
    else:
        print(image.shape)

    encoder = FaceEncoder()

    embedding = encoder.encode(image)

    if embedding is None:
        print("No face detected.")
    else:
        print("Embedding Shape :", embedding.shape)
        print("Embedding Type  :", type(embedding))


if __name__ == "__main__":
    main()