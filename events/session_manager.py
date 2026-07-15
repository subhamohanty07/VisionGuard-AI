from datetime import datetime, timedelta

from events.session import Session


class SessionManager:

    def __init__(self):

        self.current_session = None

        self.next_session_id = 1

        self.session_timeout = timedelta(seconds=10)

    def update(self, unknown_detected: bool):

        now = datetime.now()

        # No active session
        if self.current_session is None:

            if unknown_detected:

                self.current_session = Session(
                    session_id=self.next_session_id,
                    start_time=now,
                    last_seen=now,
                )

                self.next_session_id += 1

                return "SESSION_STARTED"

            return "NO_SESSION"

        # Active session exists
        if unknown_detected:

            self.current_session.last_seen = now

            return "SESSION_ACTIVE"

        # Check timeout
        if now - self.current_session.last_seen > self.session_timeout:

            self.current_session.active = False

            self.current_session = None

            return "SESSION_ENDED"

        return "SESSION_ACTIVE"