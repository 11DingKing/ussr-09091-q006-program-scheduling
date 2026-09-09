from dataclasses import dataclass

@dataclass(frozen=True)
class Slot:
    room: str
    start_minute: int
    end_minute: int

def overlaps(left: Slot, right: Slot) -> bool:
    return left.room == right.room and left.start_minute < right.end_minute and right.start_minute < left.end_minute
