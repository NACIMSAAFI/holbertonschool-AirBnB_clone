#!/usr/bin/python3
"""
Unit tests for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_text(self):
        """
        Test Review text attribute
        """
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
