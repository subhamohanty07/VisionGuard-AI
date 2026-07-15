from dataclasses import dataclass
from datetime import datetime


@dataclass
class Session:
    session_id: int
    start_time: datetime
    last_seen: datetime
    active: bool = True