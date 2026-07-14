from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"
STORAGE_DIR = BASE_DIR / "storage"
KNOWN_FACES_DIR = STORAGE_DIR / "known_faces"

HAAR_CASCADE_PATH = MODELS_DIR / "haarcascade_frontalface_default.xml"