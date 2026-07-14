from recognition.face_database import FaceDatabase


def main():

    database = FaceDatabase()

    database.load()

    print(database.get_all())


if __name__ == "__main__":
    main()