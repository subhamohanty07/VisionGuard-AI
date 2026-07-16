from enum import Enum


class SessionState(Enum):
    NO_SESSION = "NO_SESSION"
    STARTED = "STARTED"
    ACTIVE = "ACTIVE"
    ENDED = "ENDED"