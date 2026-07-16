import os

import requests
from dotenv import load_dotenv


class TelegramAlert:
    """
    Handles Telegram notifications.
    """

    def __init__(self):

        load_dotenv()

        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if not self.bot_token:
            raise ValueError("TELEGRAM_BOT_TOKEN not found in .env")

        if not self.chat_id:
            raise ValueError("TELEGRAM_CHAT_ID not found in .env")

    def send_message(self, message: str):
        """
        Send a text message to Telegram.
        """

        url = (
            f"https://api.telegram.org/bot"
            f"{self.bot_token}/sendMessage"
        )

        payload = {
            "chat_id": self.chat_id,
            "text": message,
        }

        try:
            response = requests.post(
                url,
                data=payload,
                timeout=10,
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            print(f"[Telegram] Failed to send message: {e}")
            return None

    def send_photo(self, image_path: str, caption: str = ""):
        """
        Send a photo with an optional caption.
        """

        url = (
            f"https://api.telegram.org/bot"
            f"{self.bot_token}/sendPhoto"
        )

        try:
            with open(image_path, "rb") as photo:

                response = requests.post(
                    url,
                    data={
                        "chat_id": self.chat_id,
                        "caption": caption,
                    },
                    files={
                        "photo": photo,
                    },
                    timeout=20,
                )

            response.raise_for_status()

            return response.json()

        except FileNotFoundError:
            print(f"[Telegram] Image not found: {image_path}")
            return None

        except requests.RequestException as e:
            print(f"[Telegram] Failed to send photo: {e}")
            return None

    def send_unknown_person_alert(self, event):
        """
        Send an alert when an unknown person is detected.
        """

        caption = (
            "🚨 VisionGuard AI Alert\n\n"
            "⚠️ Unknown Person Detected\n\n"
            f"🕒 Time: {event.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"📊 Confidence: {event.confidence:.2f}"
        )

        return self.send_photo(
            image_path=event.image_path,
            caption=caption,
        )