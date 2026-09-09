from dataclasses import dataclass
from enum import StrEnum


class ProgramState(StrEnum):
    DRAFT = "draft"
    PROPOSED = "proposed"
    LOCKED = "locked"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class ProgramSlot:
    slot_id: str
    capacity: int
    state: ProgramState = ProgramState.DRAFT
