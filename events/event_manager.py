from datetime import datetime

from alerts.telegram_alert import TelegramAlert
from events.event import Event
from events.event_logger import EventLogger
from events.session_manager import SessionManager
from events.session_state import SessionState
from utils.image_saver import ImageSaver


class EventManager:
    """
    Handles security events based on session state.
    """

    def __init__(self):
        self.logger = EventLogger()
        self.image_saver = ImageSaver()
        self.session_manager = SessionManager()
        self.telegram = TelegramAlert()

    def handle(self, unknown_present, results, frame):
        """
        Process one recognition cycle.
        """

        state = self.session_manager.update(unknown_present)

        # --------------------------------------------------
        # New unknown session started
        # --------------------------------------------------
        if state == SessionState.STARTED:

            # Find the first unknown person
            unknown_result = next(
                (result for result in results if not result.is_known),
                None,
            )

            if unknown_result is None:
                return

            image_path = self.image_saver.save_unknown(frame)

            event = Event(
                event_type="UNKNOWN_PERSON",
                timestamp=datetime.now(),
                session_id=self.session_manager.current_session.session_id,
                person_name="Unknown",
                confidence=unknown_result.score,
                image_path=image_path,
            )


            self.logger.log(event)

            self.telegram.send_unknown_person_alert(event)

        # --------------------------------------------------
        # Session still active
        # --------------------------------------------------
        elif state == SessionState.ACTIVE:
            pass

        # --------------------------------------------------
        # Session ended
        # --------------------------------------------------
        elif state == SessionState.ENDED:

            self.logger.log_session_end(
                self.session_manager.last_completed_session
            )

        # --------------------------------------------------
        # No active session
        # --------------------------------------------------
        elif state == SessionState.NO_SESSION:
            pass