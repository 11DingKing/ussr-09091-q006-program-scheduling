import unittest

from src.program_scheduling.domain import ProgramSlot, ProgramState


class ProgramSmokeTest(unittest.TestCase):
    def test_slot_starts_draft(self):
        self.assertEqual(ProgramSlot("demo", 20).state, ProgramState.DRAFT)


if __name__ == "__main__":
    unittest.main()
