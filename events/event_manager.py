from datetime import datetime

from events.event import Event
from events.event_logger import EventLogger


class EventManager:

    def __init__(self):

        self.logger = EventLogger()

    def handle(self, recognition_result):

        if recognition_result.is_known:
            return

        event = Event(
            event_type="UNKNOWN_PERSON",
            timestamp=datetime.now(),
            person_name="Unknown",
            confidence=recognition_result.score,
        )

        self.logger.log(event)