from datetime import datetime

import cv2

from config import UNKNOWN_FACES_DIR


class ImageSaver:
    """
    Saves images of unknown people.
    """

    def save_unknown(self, frame):

        # Create the folder if it doesn't exist
        UNKNOWN_FACES_DIR.mkdir(parents=True, exist_ok=True)

        filename = datetime.now().strftime(
            "unknown_%Y%m%d_%H%M%S.jpg"
        )

        image_path = UNKNOWN_FACES_DIR / filename

        success = cv2.imwrite(str(image_path), frame)

        if not success:
            raise RuntimeError(
                f"Failed to save image: {image_path}"
            )

        return str(image_path)