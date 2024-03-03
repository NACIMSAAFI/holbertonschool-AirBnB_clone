#!/usr/bin/python3
"""
Unit tests for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_name(self):
        """
        Test Place name attribute
        """
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")


if __name__ == "__main__":
    unittest.main()
