from datetime import datetime, timedelta

from config import SESSION_TIMEOUT_SECONDS
from events.session import Session
from events.session_state import SessionState


class SessionManager:
    """
    Manages the lifecycle of an unknown person session.
    """

    def __init__(self):
        self.current_session = None
        self.last_completed_session = None

        self.next_session_id = 1

        self.session_timeout = timedelta(
            seconds=SESSION_TIMEOUT_SECONDS
        )

    def update(self, unknown_present: bool):
        """
        Updates the current session based on whether an unknown
        person is currently visible.

        Returns:
            SessionState
        """

        now = datetime.now()

        # --------------------------------------------------
        # No active session
        # --------------------------------------------------
        if self.current_session is None:

            if unknown_present:

                self.current_session = Session(
                    session_id=self.next_session_id,
                    start_time=now,
                    last_seen=now,
                )

                self.next_session_id += 1

                return SessionState.STARTED

            return SessionState.NO_SESSION

        # --------------------------------------------------
        # Active session exists
        # --------------------------------------------------
        if unknown_present:

            self.current_session.last_seen = now

            return SessionState.ACTIVE

        # --------------------------------------------------
        # Unknown person disappeared
        # --------------------------------------------------
        if now - self.current_session.last_seen > self.session_timeout:

            self.current_session.active = False

            # Save completed session before clearing it
            self.last_completed_session = self.current_session

            self.current_session = None

            return SessionState.ENDED

        return SessionState.ACTIVE