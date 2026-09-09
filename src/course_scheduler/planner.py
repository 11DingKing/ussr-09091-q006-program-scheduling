from .constraints import Slot, overlaps

def available(candidate: Slot, occupied: list[Slot]) -> bool:
    return all(not overlaps(candidate, existing) for existing in occupied)
