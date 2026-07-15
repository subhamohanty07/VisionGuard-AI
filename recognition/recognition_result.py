from dataclasses import dataclass


@dataclass
class RecognitionResult:
    name: str
    score: float
    is_known: bool