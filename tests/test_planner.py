import sys
import unittest
sys.path.insert(0, "src")
from course_scheduler.constraints import Slot
from course_scheduler.planner import available

class PlannerTest(unittest.TestCase):
    def test_room_conflict(self):
        self.assertFalse(available(Slot("A", 600, 660), [Slot("A", 630, 690)]))
        self.assertTrue(available(Slot("B", 630, 690), [Slot("A", 630, 690)]))

if __name__ == "__main__": unittest.main()
