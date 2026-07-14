from registration.face_registration import FaceRegistration


def main():
    person_name = input("Enter person's name: ").strip()

    if not person_name:
        print("Person name cannot be empty.")
        return

    registration = FaceRegistration(person_name)
    registration.start()


if __name__ == "__main__":
    main()