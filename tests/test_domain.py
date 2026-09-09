import sys
import unittest
from datetime import datetime, timezone
sys.path.insert(0, "src")
from course_scheduler.domain import constraint_ids, CourseSchedulerWindow

class DomainTest(unittest.TestCase):
    def test_first_occurrences(self):
        self.assertEqual(constraint_ids([{"id":"a"}, {"id":"a"}, {"id":"b"}]), ["a", "b"])
    def test_reverse_time_rejected(self):
        window = CourseSchedulerWindow("x", datetime(2026, 1, 1, tzinfo=timezone.utc), datetime(2026, 1, 1, tzinfo=timezone.utc))
        with self.assertRaises(ValueError):
            window.duration_seconds()

if __name__ == "__main__":
    unittest.main()
