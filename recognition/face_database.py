import pickle

from config import DATABASE_DIR


class FaceDatabase:
    """
    Handles loading, saving, and managing the face embedding database.
    """

    def __init__(self):

        DATABASE_DIR.mkdir(exist_ok=True)

        self.database_path = DATABASE_DIR / "face_database.pkl"

        self.face_database = {}

    def load(self):
        """
        Load the face database from disk.
        """

        if not self.database_path.exists():
            return self.face_database

        try:
            with open(self.database_path, "rb") as file:
                self.face_database = pickle.load(file)

        except (pickle.PickleError, EOFError):
            print("[Database] Failed to load database.")

            self.face_database = {}

        return self.face_database

    def save(self):
        """
        Save the face database to disk.
        """

        with open(self.database_path, "wb") as file:
            pickle.dump(self.face_database, file)

    def person_exists(self, person_name: str):
        """
        Check whether a person already exists.
        """

        return person_name in self.face_database

    def add_embedding(self, person_name: str, embedding):
        """
        Add an embedding for a person.
        """

        if not self.person_exists(person_name):

            self.face_database[person_name] = {
                "embeddings": [],
                "image_count": 0,
            }

        self.face_database[person_name]["embeddings"].append(
            embedding
        )

        self.face_database[person_name]["image_count"] += 1

    def get_person(self, person_name: str):
        """
        Return a single person.
        """

        return self.face_database.get(person_name)

    def get_all(self):
        """
        Return the complete database.
        """

        return self.face_database