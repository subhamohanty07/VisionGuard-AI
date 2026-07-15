from datetime import datetime

from events.event import Event
from events.event_logger import EventLogger
from utils.image_saver import ImageSaver
from datetime import datetime, timedelta


class EventManager:

    def __init__(self):

        self.logger = EventLogger()
        self.image_saver = ImageSaver()
        self.last_unknown_event = None
        self.cooldown = timedelta(seconds=5)

    def handle(self, recognition_result, frame):

            if recognition_result.is_known:
                return

            now = datetime.now()

            if (
                self.last_unknown_event is not None
                and now - self.last_unknown_event < self.cooldown
            ):
                return

            self.last_unknown_event = now

            image_path = self.image_saver.save_unknown(frame)

            event = Event(
                event_type="UNKNOWN_PERSON",
                timestamp=now,
                person_name="Unknown",
                confidence=recognition_result.score,
                image_path=image_path,
            )

            self.logger.log(event)