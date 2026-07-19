from pathlib import Path

# ==================================================
# Project Paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"
KNOWN_FACES_DIR = BASE_DIR / "known_faces"
UNKNOWN_FACES_DIR = BASE_DIR / "unknown_faces"
DATABASE_DIR = BASE_DIR / "database"
LOGS_DIR = BASE_DIR / "logs"

# ==================================================
# Models
# ==================================================

HAAR_CASCADE_PATH = MODELS_DIR / "haarcascade_frontalface_default.xml"

# ==================================================
# Recognition
# ==================================================

FACE_MATCH_THRESHOLD = 0.60
RECOGNITION_INTERVAL = 5

# ==================================================
# Session
# ==================================================

SESSION_TIMEOUT_SECONDS = 10

# ==================================================
# Camera
# ==================================================

CAMERA_INDEX = 0

# ==================================================
# ESP8266
# ==================================================

ESP8266_PORT = "COM3"
ESP8266_BAUDRATE = 115200

# ==================================================
# Telegram
# ==================================================

ENABLE_TELEGRAM_ALERTS = True

# ==================================================
# Application
# ==================================================

APP_NAME = "VisionGuard AI"
VERSION = "0.6"

