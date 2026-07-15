from dataclasses import dataclass
from datetime import datetime


@dataclass
class Event:
    event_type: str
    timestamp: datetime
    person_name: str
    confidence: float
    image_path: str | None = None