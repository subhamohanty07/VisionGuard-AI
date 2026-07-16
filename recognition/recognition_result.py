from dataclasses import dataclass
from typing import Optional


@dataclass
class RecognitionResult:
    """
    Represents the recognition result of a single detected face.
    """

    name: str
    score: float
    is_known: bool

    # (x1, y1, x2, y2)
    bbox: Optional[tuple[int, int, int, int]] = None