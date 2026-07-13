import unittest
from datetime import datetime, timedelta, timezone

from src.review_window import is_review_stale


class ReviewWindowTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime(2026, 7, 4, tzinfo=timezone.utc)

    def test_review_is_stale_at_exact_boundary(self):
        self.assertTrue(is_review_stale(self.now - timedelta(days=5), self.now))

    def test_recent_review_is_not_stale(self):
        self.assertFalse(is_review_stale(self.now - timedelta(days=4), self.now))

    def test_negative_threshold_is_rejected(self):
        with self.assertRaises(ValueError):
            is_review_stale(self.now, self.now, stale_after_days=-1)

    def test_mixed_timezone_awareness_is_rejected(self):
        naive_updated_at = datetime(2026, 7, 1)
        with self.assertRaises(ValueError):
            is_review_stale(naive_updated_at, self.now)


if __name__ == "__main__":
    unittest.main()
