import numpy as np

from recognition.face_database import FaceDatabase
from recognition.matcher import FaceMatcher


def main():

    database = FaceDatabase()
    database.load()

    matcher = FaceMatcher()

    person = database.get_person("subh")

    if person is None:
        print("Subh not found.")
        return

    test_embedding = person["embeddings"][0]

    name, score = matcher.match(
        test_embedding,
        database.get_all(),
    )

    print(f"Matched Person : {name}")
    print(f"Similarity     : {score:.4f}")


if __name__ == "__main__":
    main()