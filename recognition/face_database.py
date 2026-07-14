from pathlib import Path
import pickle

from config import BASE_DIR


class FaceDatabase:
    def __init__(self):
        self.database_directory = BASE_DIR / "database"
        self.database_directory.mkdir(exist_ok=True)

        self.database_path = self.database_directory / "face_database.pkl"

        self.face_database = {}

    def load(self):
        if self.database_path.exists():
            with open(self.database_path, "rb") as file:
                self.face_database = pickle.load(file)

        return self.face_database

    def save(self):
        with open(self.database_path, "wb") as file:
            pickle.dump(self.face_database, file)

    def person_exists(self, person_name: str):
        return person_name in self.face_database

    def add_embedding(self, person_name: str, embedding):

        if not self.person_exists(person_name):

            self.face_database[person_name] = {
                "embeddings": [],
                "image_count": 0,
            }

        self.face_database[person_name]["embeddings"].append(embedding)
        self.face_database[person_name]["image_count"] += 1

    def get_person(self, person_name: str):
        return self.face_database.get(person_name)

    def get_all(self):
        return self.face_database