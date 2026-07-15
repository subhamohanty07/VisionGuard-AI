from datetime import datetime
import cv2

from config import UNKNOWN_FACES_DIR


class ImageSaver:

    def save_unknown(self, frame):

        filename = datetime.now().strftime(
            "unknown_%Y%m%d_%H%M%S.jpg"
        )

        image_path = UNKNOWN_FACES_DIR / filename

        cv2.imwrite(str(image_path), frame)

        return str(image_path)