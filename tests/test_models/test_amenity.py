#!/usr/bin/python3
"""
Unit tests for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_name(self):
        """
        Test Amenity name attribute
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
